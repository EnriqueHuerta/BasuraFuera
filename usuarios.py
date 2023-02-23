#_*_coding:utf-8*-*-
from odoo import models,fields

class usuarios (models.Model):
    _name = 'basurafuera.usuarios'

    name = fields.Char(String='Nombre del Usuario')
    correo = fields.Char(string='Correo Electronico')
    contraseña = fields.Char(string='Contraseña')
    direccion = fields.Char(string='Direccion')
    latitud = fields.Char(string='Latitud')
    longitud = fields.Char(string='Longitud')
    

    _sql_constraints = [
        ('unique_usuarios','unique (name)','Este usuario ya existe!')
    ]