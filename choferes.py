#_*_coding:utf-8*-*-
from odoo import models,fields

class choferes (models.Model):
    _name = 'basurafuera.choferes'

    name = fields.Char(String='Nombre del Chofer')
    NumTel = fields.Char(string='Numero de Telefono')
    edad = fields.Char(string ='Edad')


    _sql_constraints = [
        ('unique_choferes','unique (name)','Este Chofer ya existe!')
    ]