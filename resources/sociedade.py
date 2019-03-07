import json
from flask import request
from flask_restful import Resource
from Model import db, Usuario, Profissoes, Atributos, Enderecos, UsuarioSchema, AtributosSchema, ProfissaoSchema, EnderecosSchema

usuario_schema = UsuarioSchema()
atributo_schema = AtributosSchema()
profissao_schema = ProfissaoSchema()
endereco_schema = EnderecosSchema()

class SociedadeResource(Resource):

    def get(self, person_id):

        usuarios = Usuario.query.filter_by(id=person_id).first()
        usuarios = usuario_schema.dump(usuarios).data

        if usuarios:
            atributos = Atributos.query.filter_by(usuario_id=usuarios["id"]).first()
            atributos = atributo_schema.dump(atributos).data

            profissoes = Profissoes.query.filter_by(atributos_id=atributos["id"]).first()
            profissoes = profissao_schema.dump(profissoes).data

            enderecos = Enderecos.query.filter_by(atributos_id=atributos["id"]).first()
            enderecos = endereco_schema.dump(enderecos).data

            sociedadeData = {
                "usuarios": usuarios,
                "atributos": atributos,
                "enderecos": enderecos,
                "profissoes": profissoes
            }
            status = "sucesso"
            result = sociedadeData
            response_status = 200
        
            
            pass
        else:
            status = "erro"
            result = "Usuario não encontrado"
            response_status = 404
            pass

        return {'status': status, 'data': result }, response_status
        

        
