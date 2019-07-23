# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PerDiemFields(models.Model):
  _inherit = 'hr.expense.sheet'

  delivery_amount = fields.Monetary(string='Cantidad de Entrega')
  prove_amount = fields.Monetary(related='total_amount', string='Cantidad Comprobada')
  returned = fields.Monetary(string='Devuelto')
  diferency = fields.Monetary(string='Diferencia', compute="_total_mejoras")
  approved = fields.Boolean(string='Aprovado')

  @api.one
  @api.depends('prove_amount','returned','diferency','delivery_amount')
  def _total_mejoras(self):
    self.diferency = (float(self.delivery_amount)) - (float(self.prove_amount)) - (float(self.returned))