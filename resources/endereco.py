from flask import request
from flask_restful import Resource
from Model import db, Enderecos, EnderecosSchema

enderecos_schema = EnderecosSchema(many=True)
endereco_schema = EnderecosSchema()


class EnderecoResource(Resource):
    def get(self):
        enderecos = Enderecos.query.all()
        enderecos = enderecos_schema.dump(enderecos).data
        return {'status': 'success', 'data': enderecos}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = endereco_schema.load(json_data)
        if errors:
            return errors, 422
        endereco = Enderecos.query.filter_by(numero=data['numero']).first()
        if endereco:
            return {'message': 'Este endereco já existe'}, 400
        endereco = Enderecos(
            cep=json_data['cep'],
            bairro=json_data['bairro'],
            cidade=json_data['cidade'],
            estado=json_data['estado'],
            numero=json_data['numero'],
            complemento=json_data['complemento'],
            atributos_id=json_data['atributos_id']
        )

        db.session.add(endereco)
        db.session.commit()

        result = endereco_schema.dump(endereco).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = endereco_schema.load(json_data)
        if errors:
            return errors, 422
        endereco = Enderecos.query.filter_by(id=data['id']).first()
        if not endereco:
            return {'message': 'Este endereco já existe'}, 400
        endereco.name = data['name']
        db.session.commit()

        result = endereco_schema.dump(endereco).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Não foi detectado um Input'}, 400
        # Validate and deserialize input
        data, errors = endereco_schema.load(json_data)
        if errors:
            return errors, 422
        endereco = Enderecos.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = endereco_schema.dump(endereco).data

        return {"status": 'success', 'data': result}, 204
