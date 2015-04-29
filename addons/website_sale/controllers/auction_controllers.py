__author__ = 'vwvolodya'

from openerp import http
from openerp.http import request


class AuctionController(http.Controller):
    @http.route(['/auction/place_bid'], type='http', auth='user')
    def register_new_bid(self):
        pass

    def check_bid(self):
        pass