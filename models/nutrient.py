# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char('Nutrient Name')
    uom_id = fields.Many2one('product.uom','Unit of measure')


class Dieftfacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient',string='Product Nutrient')
    product_id = fields.Many2one('product.template')
    uom = fields.Char(related='nutrient_id.uom_id.name',string='UOM',readyonly=True)
    value = fields.Float('Nutrient Value')
    # dailypercent = fields.Float('Daily Recommended Value')
    dailyRecommended = fields.Float('Daily Recommended')
    dailypercent = fields.Float(string="Daily Percent", compute="_calcDailyPercent")

    @api.one
    @api.depends('dailyRecommended','value')
    def _calcDailyPercent(self):
        if self.dailyRecommended != 0:
            self.dailypercent =  (self.value/self.dailyRecommended) * 100
        else:
            self.dailypercent =  (self.value/1) * 100
