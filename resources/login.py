from flask import request
from flask_restful import Resource
from Model import db, Usuario, UsuarioSchema
import hashlib

usuarios_schema = UsuarioSchema(many=True)
usuario_schema = UsuarioSchema()

class LoginResource(Resource):

    def encrypt_string(self, hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

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
            if usuario.senha == self.encrypt_string(data['senha']):
                return {'message': 'success', 'data': usuario.id}, 200
            else:
                return {'message': 'Login ou Senha invalido'}, 400
        else:
            return {'message': 'Usuario não encontrado'}, 404
