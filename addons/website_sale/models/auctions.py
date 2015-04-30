__author__ = 'vwvolodya'
from openerp import models, fields


class Auctions(models.Model):
    """Auctions class called"""
    _name = 'auction.edit'

    _description = 'Set parameters of auctions'

    def get_default_value_bit(self):
        val = 0
        return val

    auction_name = fields.Char(string="Name auctions", required=True)
    start_auction_date_time = fields.Datetime(string="Start date auction", required=True)
    stop_auction_date_time = fields.Datetime(strring="Stop date auction", required=True)
    minimum_bid = fields.Integer(default=get_default_value_bit, string="Minimum bit", required=True)

    description_auction = fields.Text(string="Auction Description", help="The not require field, but need for informational")

    # computed_min_lot_price = fields.Float(compute='compute_min_price')
    #
    # def compute_min_price(self):
    #     pass


class Bids(models.Model):
    _name = 'ebay_like.bids'
    user_id = fields.Many2one('res.partner')
    auction_id = fields.Many2one('ebay_like.auctions')
    price = fields.Float(required=True)
