import json
from flask import request
from flask_restful import Resource
from Model import db, Usuario, Profissoes, Atributos, Enderecos, UsuarioSchema, AtributosSchema, ProfissaoSchema, EnderecosSchema, Delitos, DelitosSchema, DelitosUsuario, DelitosUsuarioSchema

usuario_schema = UsuarioSchema()
atributo_schema = AtributosSchema()
profissao_schema = ProfissaoSchema()
endereco_schema = EnderecosSchema()
delito_schema = DelitosSchema()
delitos_usuario_schema = DelitosUsuarioSchema()

class SociedadeResource(Resource):

    def get(self, person_id):

        usuarios = Usuario.query.filter_by(id=person_id).first()
        usuarios = usuario_schema.dump(usuarios).data

        nivel = usuarios["permissao"]["nivel"]

        if nivel == "policial":
            contador = 0
            leve = 0
            medio = 0
            grave = 0

            usuario = Usuario.query.filter_by(id=person_id).first()
            usuario = usuario_schema.dump(usuario).data
            # delitos = usuario.delitos
            # delitos = delito_schema.dump(delitos).data
            # delitos = delito_schema.dump(delitos).data

            # delitoUsuario = DelitosUsuario.query.filter_by(usuario_id=usuarios["id"]).first()
            # print(delitoUsuario)
            # delitoUsuario = delitos_usuario_schema.dump(delitoUsuario).data
            # print(delitoUsuario)

            for delito in usuario["delitos"]:
                if delito["artigo"] == 121:
                    grave = grave + 1
                elif delito["artigo"] == 12:
                    medio = medio + 1
                elif delito["artigo"] == 0:
                    leve = leve + 1

            # sociedadeData = {
            #     "usuario_id": usuarios["id"],
            #     "ficha_criminal": usuarios["delitos"],
            #     "gravidade": {
            #         "leve": leve,
            #         "medio": medio,
            #         "grave": grave
            #     }
            sociedadeData = {
                "teste": usuario
            }
            # }
        else:
            sociedadeData = {
                "usuario": usuarios,
            }

        if usuarios:
        #     atributos = Atributos.query.filter_by(usuario_id=usuarios["id"]).first()
        #     atributos = atributo_schema.dump(atributos).data

            # profissoes = Profissoes.query.filter_by(atributos_id=atributos["id"]).first()
            # profissoes = profissao_schema.dump(profissoes).data

            # enderecos = Enderecos.query.filter_by(atributos_id=atributos["id"]).first()
            # enderecos = endereco_schema.dump(enderecos).data

            # sociedadeData = {
            #     "usuarios": usuarios,
            #     "atributos": atributos,
            #     # "enderecos": enderecos,
            #     # "profissoes": profissoes
            # }
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
        

        
