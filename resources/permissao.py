from flask import request
from flask_restful import Resource
from Model import db, Permissao, PermissaoSchema

permissoes_schema = PermissaoSchema(many=True)
permissao_schema = PermissaoSchema()


class PermissaoResource(Resource):
    def get(self):
        
        usuarios = Usuario.query.filter_by(id=person_id).first()
        usuarios = usuario_schema.dump(usuarios).data

        permissoes = Permissao.query.all()
        permissoes = permissoes_schema.dump(permissoes).data
        return {'status': 'success', 'data': permissoes}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = permissao_schema.load(json_data)
        if errors:
            return errors, 422
        permissao = Permissao.query.filter_by(nivel=data['nivel']).first()
        if permissao:
            return {'message': 'Este permissao já existe'}, 400
        permissao = Permissao(
            nivel=json_data['nivel']
        )

        db.session.add(permissao)
        db.session.commit()

        result = permissao_schema.dump(permissao).data

        return {"status": 'success', 'data': result}, 201