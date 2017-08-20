# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

# TODO Think about journals, prefixs, overlaps etc

class MtoSequence(models.Model):

    _name = 'mto.sequence'
    _description = 'Mto Sequence'  # TODO
    _rec_name = 'sale_id'

    sale_id = fields.Many2one(
        comodel_name='sale.order',
        required=True,
        index=True
    )
    purchase_next_val = fields.Integer(default=0)
    delivery_next_val = fields.Integer(default=0)
    incoming_next_val = fields.Integer(default=0)
    invoice_next_val = fields.Integer(default=0)
    production_next_val = fields.Integer(default=0)

    def sequence_codes(self):
        return ['purchase', 'delivery', 'incoming', 'invoice', 'production']

    @api.model
    def next_by_code(self, sale_id, sequence_code):
        seq_codes = self.sequence_codes()
        if sequence_code not in self.sequence_codes():
            return
        seq = self.sudo().search([('sale_id', '=', sale_id)])
        if not seq:
            seq = self.create(default={'sale_id': sale_id})
        val = seq.sale_id.name.replace()