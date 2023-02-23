#_*_coding:utf-8*-*-
from odoo import models,fields

class rutar (models.Model):
    _name = 'basurafuera.rutar'

    name = fields.Char(string='Identificador de la ruta')
    fechainicio = fields.Char(String='Fecha de inicio')
    fechafinal = fields.Char(string='Fecha del final')
    camion = fields.Many2one('basurafuera.camiones',string='Camion')
    posiciones = fields.One2many('basurafuera.rutaposreal','ruta',string='Ruta Posicion Real')

    _sql_constraints = [
        ('unique_rutar','unique (name)','Esta ruta ya existe!')
    ]