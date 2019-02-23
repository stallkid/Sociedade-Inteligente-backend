from flask import request
from flask_restful import Resource
from Model import db, Atributos, AtributosSchema

atributos_schema = AtributosSchema(many=True)
atributo_schema = AtributosSchema()


class AtributoResource(Resource):
    def get(self):
        atributos = Atributos.query.all()
        atributos = atributos_schema.dump(atributos).data
        return {'status': 'success', 'data': atributos}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = atributo_schema.load(json_data)
        if errors:
            return errors, 422
        atributo = Atributos.query.filter_by(nome=data['nome']).first()
        if atributo:
            return {'message': 'Este atributo já existe'}, 400
        atributo = Atributos(
            nome=json_data['nome'],
            idade=json_data['idade'],
            cpf=json_data['cpf'],
            rg=json_data['rg'],
            estadoCivil=json_data['estadoCivil'],
            sexo=json_data['sexo'],
            dataDeNascimento=json_data['dataDeNascimento'],
            usuario_id=json_data['usuario_id'],
        )

        db.session.add(atributo)
        db.session.commit()

        result = atributo_schema.dump(atributo).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = atributo_schema.load(json_data)
        if errors:
            return errors, 422
        atributo = Atributos.query.filter_by(id=data['id']).first()
        if not atributo:
            return {'message': 'Este atributo já existe'}, 400
        atributo.name = data['name']
        db.session.commit()

        result = atributo_schema.dump(atributo).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = atributo_schema.load(json_data)
        if errors:
            return errors, 422
        atributo = Atributos.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = atributo_schema.dump(atributo).data

        return {"status": 'success', 'data': result}, 204
