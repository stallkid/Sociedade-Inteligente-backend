import json
import pandas as pd
import artificial_intelligence.logistic_regression as lr
import artificial_intelligence.neural_network as nn

from flask import request
from flask_restful import Resource
from Model import db, Usuario, Profissoes, Atributos, Enderecos, UsuarioSchema, AtributosSchema, ProfissaoSchema, EnderecosSchema, Delitos, DelitosSchema, DelitosUsuario, DelitosUsuarioSchema

usuario_schema = UsuarioSchema()
atributo_schema = AtributosSchema()
profissao_schema = ProfissaoSchema()
endereco_schema = EnderecosSchema()
delito_schema = DelitosSchema()
delitos_usuario_schema = DelitosUsuarioSchema(many=True)

class SociedadeResource(Resource):

    def get(self, person_id):

        usuario = Usuario.query.filter_by(id=person_id).first()
        usuario = usuario_schema.dump(usuario).data

        nivel = usuario["permissao"]["nivel"]

        if nivel == "policial":
            contador = 0
            leve = 0
            medio = 0
            grave = 0

            ficha_criminal = DelitosUsuario.query.filter_by(usuario_id=usuario["id"]).all()
            ficha_criminal = delitos_usuario_schema.dump(ficha_criminal).data
            
            # MONTANDO DATAFRAME NO PANDAS PARA IMPLEMENTAR IA
            cols = ["Artigo", "Gravidade"]
            rows = []
            for data in ficha_criminal:
                artigo = data["delito"]["artigo"]
                if artigo == 121:
                    peso = 3
                elif artigo == 12:
                    peso = 2
                else:
                    peso = 1
                rows.append([artigo, peso])

            if(len(ficha_criminal) > 0):
                reg = nn.NeuralNetworkIA(cols, rows)
                test = reg.neural_network()
                print(test)
            # x = df.iloc[:,1]
            # y = df.iloc[:,:1]

            # RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
            # RF.fit(x,y)
            # RF.predict(x.iloc[2:,:])
            # print(round(RF.score(x,y), 4))
            # LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(x, y)
            # LR.predict(x.iloc[2:,:])
            # print(round(LR.score(x,y), 2))

            # FINAL DO DATAFRAME

            for ficha in ficha_criminal:
                if ficha["delito"]["artigo"] == 121:
                    grave = grave + 1
                elif ficha["delito"]["artigo"] == 12:
                    medio = medio + 1
                elif ficha["delito"]["artigo"] == 0:
                    leve = leve + 1

            if grave > 0:
                status_policial = "Alto risco"
            elif medio > 0:
                status_policial = "Risco moderado"
            else:
                status_policial = "Risco leve"

            sociedadeData = {
                "usuario_id": usuario["id"],
                "status_policial": status_policial,
                "gravidade": {
                    "leve": leve,
                    "medio": medio,
                    "grave": grave
                }
            }
        else:
            sociedadeData = {
                "usuario": usuario,
            }

        if usuario:
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
        

        
