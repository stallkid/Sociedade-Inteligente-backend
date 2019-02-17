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
    atributos_id = db.Column(db.Integer, db.ForeignKey('atributos.id',
    ondelete='CASCADE'), nullable=False)
    atributos = db.relationship('Atributos', backref=db.backref('usuarios',
    lazy='dynamic' ))

    def __init__(self, login, senha, atributos_id):
        self.login = login
        self.senha = senha
        self.atributos_id = atributos_id

class UsuariosSchema(ma.Schema):
    id = fields.Integer()
    login = fields.String(required=True)
    senha = fields.String(required=True)
    atributos_id = fields.Integer(required=True)

class Atributos(db.Model):
    __tablename__ = 'atributos'
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(250), unique=True, nullable=False)
    cpf = db.Column(db.String(30), unique=True, nullable=False)
    rg = db.Column(db.String(30), unique=True, nullable=False)
    idade = db.Column(db.Integer,nullable=False)
    sexo = db.Column(db.String(15), nullable=False)
    estadoCivil = db.Column(db.String(50), nullable=False)
    dataDeNascimento = db.Column(db.DateTime, nullable=False)

    endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id',
    ondelete='CASCADE'), nullable=True)
    enderecos = db.relationship('Enderecos', backref=db.backref('atributos',
    lazy='dynamic'))

    telefone_id = db.Column(db.Integer, db.ForeignKey('telefones.id',
    ondelete='CASCADE'), nullable=True)
    telefones = db.relationship('Telefones', backref=db.backref('atributos',
    lazy='dynamic'))

    # fichaMedica_id = db.Column(db.Integer, db.ForeignKey('fichaMedica.id',
    # ondelete='CASCADE'), nullable=True)
    # fichaMedicas = db.relationship('FichaMedica', backref=db.backref('atributos',
    # lazy='dynamic'))
    
    # familiares_id = db.Column(db.Integer, db.ForeignKey('familiares.id',
    # ondelete='CASCADE'), nullable=True)
    # familiares = db.relationship('Familiares', backref=db.backref('atributos',
    # lazy='dynamic'))

    # profissao_id = db.Column(db.Integer, db.ForeignKey('profissao.id',
    # ondelete='CASCADE'), nullable=True)
    # profissao = db.relationship('Profissao', backref=db.backref('atributos',
    # lazy='dynamic'))

    # escolaridade_id = db.Column(db.Integer, db.ForeignKey('escolaridade.id',
    # ondelete='CASCADE'), nullable=True)
    # escolaridade = db.relationship('Escolaridade', backref=db.backref('atributos',
    # lazy='dynamic'))

    # email_id = db.Column(db.Integer, db.ForeignKey('email.id',
    # ondelete='CASCADE'), nullable=True)
    # email = db.relationship('Email', backref=db.backref('atributos',
    # lazy='dynamic'))

    def __init__(self, nome, cpf, rg, idade, sexo, estadoCivil, dataDeNascimento, endereco_id, telefone_id, fichaMedica_id, familiares_id, profissao_id, escolaridade_id, email_id):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataDeNascimento = dataDeNascimento
        self.endereco_id = endereco_id
        self.telefone_id = telefone_id
        self.fichaMedica_id = fichaMedica_id
        self.familiares_id = familiares_id
        self.profissao_id = profissao_id
        self.escolaridade_id = escolaridade_id
        self.email_id = email_id


class AtributosSchema(ma.Schema):
    id = fields.Integer()
    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    rg = fields.String(required=True)
    idade = fields.Integer(required=True)
    sexo = fields.String(required=True)
    estadoCivil = fields.String(required=True)
    dataDeNascimento = fields.DateTime()
    endereco_id = fields.Integer(required=False)
    telefone_id = fields.Integer(required=False)
    # fichaMedica_id = fields.Integer(required=False)
    # familiares_id = fields.Integer(required=False)
    # profissao_id = fields.Integer(required=False)
    # escolaridade_id = fields.Integer(required=False)
    # email_id = fields.Integer(required=False)

class Enderecos(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(150), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(150), nullable=False)
    # fk_cidade_id
    # fk_ceprua_id

    def __init__(self, logradouro, endereco, numero, complemento):
        self.logradouro = logradouro
        self.endereco - endereco
        self.numero = numero
        self.complemento = complemento

class EnderecosSchema(ma.Schema):
    id = fields.Integer()
    logradouro = fields.String(required=True)
    endereco = fields.String(required=True)
    numero = fields.Integer(required=True)
    complemento = fields.String(required=True)

class Telefones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(30), nullable=False)
    ddd = db.Column(db.String(5), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    operadora = db.Column(db.String(50), nullable=True)

    def __init__(self, tipo, ddd, numero, operadora):
        self.tipo = tipo
        self.ddd = ddd
        self.numero = numero
        self.operadora = operadora

class TelefonesSchema(ma.Schema):
    id = fields.Integer()
    tipo = fields.String(required=True)
    ddd = fields.String(required=True)
    numero = fields.String(required=True)
    operadora = fields.String(required=False)



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
