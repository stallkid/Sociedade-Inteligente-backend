from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

class UsuarioSchema(ma.Schema):
    id = fields.Integer()
    # login = fields.String(required=True)
    # senha = fields.String(required=True)

class Atributos(db.Model):
    __tablename__ = 'atributos'
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(250), unique=True, nullable=False)
    cpf = db.Column(db.String(30), unique=True, nullable=False)
    rg = db.Column(db.String(30), unique=True, nullable=False)
    idade = db.Column(db.Integer,nullable=False)
    sexo = db.Column(db.String(15), nullable=False)
    estadoCivil = db.Column(db.String(50), nullable=False)
    dataDeNascimento = db.Column(db.Date, nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id',
                                                         ondelete='CASCADE'), nullable=True)
    usuario = db.relationship('Usuario', backref=db.backref('atributos',
                                                                     lazy='dynamic'))

    # fichaMedica_id = db.Column(db.Integer, db.ForeignKey('fichaMedica.id',
    # ondelete='CASCADE'), nullable=True)
    # fichaMedicas = db.relationship('FichaMedica', backref=db.backref('atributos',
    # lazy='dynamic'))

    def __init__(self, nome, cpf, rg, idade, sexo, estadoCivil, dataDeNascimento, usuario_id):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataDeNascimento = dataDeNascimento
        self.usuario_id = usuario_id


class AtributosSchema(ma.Schema):
    id = fields.Integer()
    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    rg = fields.String(required=True)
    idade = fields.Integer(required=True)
    sexo = fields.String(required=True)
    estadoCivil = fields.String(required=True)
    dataDeNascimento = fields.Date(required=True)
    usuario_id = fields.Integer(required=True)

class Enderecos(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(30), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(150), nullable=False)

    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
    ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('enderecos',
    lazy='dynamic'))
    # fk_cidade_id
    # fk_ceprua_id

    def __init__(self, cep, bairro, cidade, estado, numero, complemento, atributos_id):
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento
        self.atributos_id = atributos_id

class EnderecosSchema(ma.Schema):
    id = fields.Integer()
    cep = fields.String(required=True)
    bairro = fields.String(required=True)
    cidade = fields.String(required=True)
    estado = fields.String(required=True)
    numero = fields.Integer(required=True)
    complemento = fields.String(required=True)
    atributos_id = fields.Integer(required=True)

class Telefones(db.Model):
    __tablename__ = 'telefones'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(30), nullable=False)
    ddd = db.Column(db.String(5), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    operadora = db.Column(db.String(50), nullable=True)

    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
                                                       ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('telefones',
                                                            lazy='dynamic'))

    def __init__(self, tipo, ddd, numero, operadora, atributos_id):
        self.tipo = tipo
        self.ddd = ddd
        self.numero = numero
        self.operadora = operadora
        self.atributos_id = atributos_id

class TelefonesSchema(ma.Schema):
    id = fields.Integer()
    tipo = fields.String(required=True)
    ddd = fields.String(required=True)
    numero = fields.String(required=True)
    operadora = fields.String(required=False)
    atributos_id = fields.Integer(required=True)

class Familiares(db.Model):
    __tablename__ = 'familiares'
    id = db.Column(db.Integer, primary_key=True)
    relacao = db.Column(db.String(150), nullable=False)

    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
                                                       ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('familiares',
                                                            lazy='dynamic'))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id',
                                                     ondelete='CASCADE'), nullable=True)
    usuario = db.relationship('Usuario', backref=db.backref('familiares',
                                                            lazy='dynamic'))

    def __init__(self, relacao, atributos_id, usuario_id):
        self.relacao = relacao
        self.atributos_id = atributos_id
        self.usuario_id = usuario_id

class FamiliaresSchema(ma.Schema):
    id = fields.Integer()
    relacao = fields.String(required=True)
    atributos_id = fields.Integer(required=True)
    usuario_id = fields.Integer(required=True)

class Profissoes(db.Model):
    __tablename__ = 'profissoes'
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(250), nullable=False)
    cargo = db.Column(db.String(250), nullable=False)
    dataInicio = db.Column(db.Date, nullable=False)
    dataTermino = db.Column(db.Date, nullable=True)
    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
                                                       ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('profissoes',
                                                                lazy='dynamic'))

    def __init__(self, empresa, cargo, dataInicio, dataTermino, atributos_id):
        self.empresa = empresa
        self.cargo = cargo
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.atributos_id = atributos_id

class ProfissaoSchema(ma.Schema):
    id = fields.Integer()
    empresa = fields.String(required=True)
    cargo = fields.String(required=True)
    dataInicio = fields.Date(required=True)
    dataTermino = fields.Date(required=False)
    atributos_id = fields.Integer(required=True)

class Escolaridade(db.Model):
    __tablename__ = 'escolaridade'
    id = db.Column(db.Integer, primary_key=True)
    instituicao = db.Column(db.String(250), nullable=False)
    curso = db.Column(db.String(150), nullable=False)
    grau = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    termino = db.Column(db.Date, nullable=False)
    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
                                                       ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('escolaridade',
                                                                lazy='dynamic'))

    def __init__(self, instituicao, curso, grau, status, inicio, termino, atributos_id):
        self.instituicao = instituicao
        self.curso = curso
        self.grau = grau
        self.status = status
        self.inicio = inicio
        self.termino = termino
        self.atributos_id = atributos_id

class EscolaridadeSchema(ma.Schema):
    id = fields.Integer()
    instituicao = fields.String(required=True)
    curso = fields.String(required=True)
    grau = fields.String(required=True)
    status = fields.String(required=True)
    inicio = fields.Date(required=True)
    termino = fields.Date(required=True)

class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
                                                       ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('email',
                                                                lazy='dynamic'))

    def __init__(self, email, atributos_id):
        self.email = email
        self.atributos_id = atributos_id

class EmailSchema(ma.Schema):
    id = fields.Integer()
    email = fields.String(required=True)
    atributos_id = fields.Integer(required=True)



###################
#     EXAMPLE     #
###################

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('comments', lazy='dynamic' ))

    def __init__(self, comment, category_id):
        self.comment = comment
        self.category_id = category_id


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
