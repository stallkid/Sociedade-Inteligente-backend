from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.usuario import UsuarioResource
from resources.atributo import AtributoResource
from resources.endereco import EnderecoResource
from resources.profissao import ProfissaoResource
from resources.sociedade import SociedadeResource
from resources.login import LoginResource
from resources.uploadFaces import UploadFacesResource
from resources.permissao import PermissaoResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/hello',)
api.add_resource(UsuarioResource, '/usuario')
api.add_resource(AtributoResource, '/atributos')
api.add_resource(EnderecoResource, '/endereco')
api.add_resource(ProfissaoResource, '/profissoes')
api.add_resource(PermissaoResource, '/permissao')
# api.add_resource(PermissaoResource, '/get/permissao/<user_id>')
api.add_resource(SociedadeResource, '/sociedade', '/sociedade/<person_id>')
api.add_resource(LoginResource, '/login')
api.add_resource(UploadFacesResource, '/upload-face')
