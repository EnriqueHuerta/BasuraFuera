#_*_coding:utf-8*-*-
from odoo import models,fields

class camiones (models.Model):
    _name = 'basurafuera.camiones'

    name = fields.Char(String='Placas')
    descripccion = fields.Char(string='Descripccion De La Unidad')
    chofer = fields.Many2one('basurafuera.choferes',string='Chofer')

    _sql_constraints = [
        ('unique_camiones','unique (name)','Este camion ya existe!')
        
    ]
