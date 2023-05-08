from odoo import models, fields, api

class EstatePropertyProduct(models.Model):
    
    _name = "estate.property.product"
    _description ="Prodotti"
    
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_name = fields.Char(string='Description')
    price_unit = fields.Float(string='Price Unit')
    tax_ids = fields.Many2many('account.tax', string='Taxes', related="product_id.taxes_id")
    qty = fields.Integer(string='Quantity', default=1)
    property_line_id =fields.Many2one('estate.property',string="Property Line ID")
    