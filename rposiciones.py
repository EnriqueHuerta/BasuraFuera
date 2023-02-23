#_*_coding:utf-8*-*-
from odoo import models,fields

class rposiciones (models.Model):
    _name = 'basurafuera.rposiciones'

    name = fields.Char(String='Tipo de Posicion')
    longitud = fields.Char(string='Longitud')
    latitud = fields.Char(string='Latitud')
    ruta = fields.Many2one('basurafuera.rutap',string='Ruta posicion')
    
    _sql_constraints = [
        ('unique_rposiciones','unique (name)','Esta ruta ya existe!')
    ]