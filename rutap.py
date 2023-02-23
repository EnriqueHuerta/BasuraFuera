#_*_coding:utf-8*-*-
from odoo import models,fields

class rutap (models.Model):
    _name = 'basurafuera.rutap'

    name = fields.Char(string='Nombre de la ruta')
    horario = fields.Char(string='Horario')
    dias = fields.Char(string='Dias')
    camion = fields.Many2one('basurafuera.camiones',string='Camion')
    posiciones = fields.One2many('basurafuera.rposiciones','ruta',string='Ruta Posiciones')

    _sql_constraints = [
        ('unique_rutap','unique (name)','Esta Ruta ya existe!')
    ]
    

