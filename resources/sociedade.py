import json
from flask import request
from flask_restful import Resource
from Model import db, Usuario, Profissoes, Atributos, Enderecos, UsuarioSchema, AtributosSchema, ProfissaoSchema, EnderecosSchema

usuario_schema = UsuarioSchema()
atributo_schema = AtributosSchema()
profissao_schema = ProfissaoSchema()
endereco_schema = EnderecosSchema()

class SociedadeResource(Resource):
    def get(self):
        usuarios = Usuario.query.filter_by(id=1).first()
        usuarios = usuario_schema.dump(usuarios).data
        atributos = Atributos.query.filter_by(usuario_id=1).first()
        atributos = atributo_schema.dump(atributos).data
        profissoes = Profissoes.query.filter_by(atributos_id=1).first()
        profissoes = profissao_schema.dump(profissoes).data
        enderecos = Enderecos.query.filter_by(atributos_id=1).first()
        enderecos = endereco_schema.dump(enderecos).data

        sociedadeData = {
            "usuarios": usuarios,
            "atributos": atributos,
            "enderecos": enderecos,
            "profissoes": profissoes
        }

        result = sociedadeData
        
        return {'status': 'success', 'data': result}, 200
