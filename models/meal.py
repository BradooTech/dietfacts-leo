# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    edit_button = fields.Char("Editar")
    name = fields.Char("Meal name")
    meal_date = fields.Datetime("Meal Date")
    item_ids = fields.One2many('res.users.mealitem','meal_id')
    user_id = fields.Many2one('res.users','Meal User')
    notes = fields.Text("Notes")

    @api.one
    @api.depends('item_ids','item_ids.servings')
    def _calcCalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
        self.totalcalories = currentcalories

    totalcalories = fields.Integer(string="Total calories",store="1", compute="_calcCalories")

class Dietfacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Menu item')
    calories = fields.Integer(related='item_id.calories',string='Calories per Serving',store='1',readonly='1')
    servings = fields.Float('Servings')
    notes = fields.Text('Meal item notes')
