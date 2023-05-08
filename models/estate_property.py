
from odoo import models, fields


class EstateProperty(models.Model):
    _inherit = "estate.property"

    property_line_ids = fields.One2many(
        "estate.property.product", "property_line_id", string="Ordine di vendita")

    def action_do_sold(self):

        res = super(EstateProperty, self).action_do_sold()

        # creare ordine di vendita
        sale_o = self.env['sale.order'].sudo().create({
            "name": self.name,
            "partner_id": self.partner_id.id,
        })

        # creazione linee prodotti
        for record in self:
            for line in record.property_line_ids:
                self.env['sale.order.line'].create({
                    "product_id": line.product_id.id,
                    #"name": line.product_name or '',
                    "price_unit": line.price_unit,
                    "tax_id":line.tax_ids,
                    "product_uom_qty": line.qty,
                    'order_id': sale_o.id,
                })

        return res
    


    # def action_do_sold(self):
    #     res = super(EstateProperty, self).action_do_sold()

    #     # journal = self.env['sale.order'].with_context(
    #     #     default_move_type='out_invoice')._get_default_journal()

    #     self.env['sale.order'].sudo().create({
    #         "name": self.name,
    #         "partner_id": self.partner_id.id,

    #         "order_line": [
    #             (
    #                 0,
    #                 0,
    #                 {
    #                     "product_id": 'Trattenute per commissione',
    #                     "name": 'Trattenute per commissione',
    #                     "price_unit": self.selling_price * 6 / 100,
    #                 }
    #             ),
    #         ],
    #     })

    # # for record in self:
    # #     record.env['sale.order'].sudo().create({
    # #         'move_type': 'out_invoice',
    # #         'partner_id': record.partner_id,
    # #         'journal_id': journal.id,
    # #         "order_line": [
    # #             (
    # #                 0,
    # #                 0,
    # #                 {
    # #                     "product_id": 30,
    # #                     "name": record.partner_id.name,
    # #                     "product_uom_qty": 1,
    # #                     "price_unit": record.selling_price * 6 / 100,
    # #                 }

    # #             ),
    # #         ],
    # #     })

    #     return res

