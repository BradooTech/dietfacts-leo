# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_product_template(models.Model):
    _inherit = 'product.template'
    _name = 'product.template'

    calories = fields.Integer("Calories")
    servingsize = fields.Float("Serving size")
    lastupdate = fields.Date("Last Update")
    teste = fields.Integer("Teste")
    dietitem = fields.Boolean("dietitem")
    nutrient_ids = fields.One2many('product.template.nutrient','product_id','Nutrients')


    @api.one
    @api.depends('nutrient_ids','nutrient_ids.value')
    def _calcscore(self):
        currentscore = 0
        for nutrient in self.nutrient_ids:
            currentscore = currentscore + nutrient.value
        self.nutrition_score = currentscore
    nutrition_score = fields.Float(string="Nutrition Score",store='1' ,compute="_calcscore")
