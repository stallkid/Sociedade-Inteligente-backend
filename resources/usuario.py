from flask import request
from flask_restful import Resource
from Model import db, Usuario, UsuarioSchema

usuarios_schema = UsuarioSchema(many=True)
usuario_schema = UsuarioSchema()


class UsuarioResource(Resource):
    def get(self):
        usuarios = Usuario.query.all()
        usuarios = usuarios_schema.dump(usuarios).data
        return {'status': 'success', 'data': usuarios}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = usuario_schema.load(json_data)
        if errors:
            return errors, 422
        usuario = Usuario.query.filter_by(login=data['login']).first()
        if usuario:
            return {'message': 'Este usuario já existe'}, 400
        usuario = Usuario(
            login=json_data['login'],
            senha=json_data['senha']
        )

        db.session.add(usuario)
        db.session.commit()

        result = usuario_schema.dump(usuario).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = usuario_schema.load(json_data)
        if errors:
            return errors, 422
        usuario = Usuario.query.filter_by(id=data['id']).first()
        if not usuario:
            return {'message': 'Este usuario já existe'}, 400
        usuario.name = data['name']
        db.session.commit()

        result = usuario_schema.dump(usuario).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = usuario_schema.load(json_data)
        if errors:
            return errors, 422
        usuario = Usuario.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = usuario_schema.dump(usuario).data

        return {"status": 'success', 'data': result}, 204
