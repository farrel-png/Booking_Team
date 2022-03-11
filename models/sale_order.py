from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    is_booking_order = fields.Boolean(string='Is Booking Order', default=True)
    team = fields.Many2one(comodel_name='service.team', string='Team')
    team_leader = fields.Many2one('res.users', string='Team Leader')
    team_members = fields.Many2many('res.users', string='Team Members')
    
    booking_start = fields.Date('Booking Start', default = lambda self:fields.Date.Today())
    booking_end = fields.Date(string='Booking End')
    
    
    
    
