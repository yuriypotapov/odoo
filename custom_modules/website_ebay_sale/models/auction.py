__author__ = 'vwvolodya'


from openerp import models, fields


class Auctions(models.Model):
    _name = 'ebay_like.auctions'

    start_date = fields.Datetime(string='Beginning of auction', required=True)
    end_date = fields.Datetime(string='End of auction', required=True)
    product_id = fields.Many2one('product.product')

    computed_min_lot_price = fields.Float(compute='compute_min_price')

    def compute_min_price(self):
        pass


class Bids(models.Model):
    _name = 'ebay_like.bids'

    user_id = fields.Many2one('res.partner')
    auction_id = fields.Many2one('ebay_like.auctions')
    price = fields.Float(required=True)
