#_*_coding:utf-8*-*-
from operator import mod
from odoo import models,fields

class rutaposreal (models.Model):
    _name = 'basurafuera.rutaposreal'

    name = fields.Char(String='Tipo de ruta')
    longitud = fields.Char(string='longitud')
    latitud = fields.Char(string='latitud')
    ruta= fields.Many2one('basurafuera.rutar',string='Ruta Real')
    

    _sql_constraints = [
        ('unique_rutaposreal','unique (name)','Esta ruta ya existe!')
    ]