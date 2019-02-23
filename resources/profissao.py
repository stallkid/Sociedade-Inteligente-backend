from flask import request
from flask_restful import Resource
from Model import db, Profissoes, ProfissaoSchema

profissoes_schema = ProfissaoSchema(many=True)
profissao_schema = ProfissaoSchema()


class ProfissaoResource(Resource):
    def get(self):
        profissoes = Profissoes.query.all()
        profissoes = profissoes_schema.dump(profissoes).data
        return {'status': 'success', 'data': profissoes}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = profissao_schema.load(json_data)
        if errors:
            return errors, 422
        profissao = Profissoes(
            empresa=json_data['empresa'],
            cargo=json_data['cargo'],
            dataInicio=json_data['dataInicio'],
            dataTermino=json_data['dataTermino'],
            atributos_id=json_data['atributos_id'],
        )

        db.session.add(profissao)
        db.session.commit()

        result = profissao_schema.dump(profissao).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = profissao_schema.load(json_data)
        if errors:
            return errors, 422
        profissao = Profissoes.query.filter_by(id=data['id']).first()
        if not profissao:
            return {'message': 'Esta profissao já existe'}, 400
        profissao.name = data['name']
        db.session.commit()

        result = profissao_schema.dump(profissao).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = profissao_schema.load(json_data)
        if errors:
            return errors, 422
        profissao = Profissoes.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = profissao_schema.dump(profissao).data

        return {"status": 'success', 'data': result}, 204
