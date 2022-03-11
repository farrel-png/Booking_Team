from odoo import api, fields, models


class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'Work Order'

    wo_number = fields.Char(string='WO Number', readonly=True, copy=False)
    
    booking_order_reference = fields.Many2one('sale.order', string='Booking Order Reference')
    team = fields.Many2one(comodel_name='service_team', string='Team', required=True)
    team_members = fields.Many2many(comodel_name='res.users', string='Team Member')
    planned_start = fields.Datetime('Planned Start', required=True, default=lambda self: fields.Date.Today())
    planned_end = fields.Datetime('Planned End', required=True)
    date_start = fields.Datetime('Date Start', readonly=True)
    date_end = fields.Datetime('Date End', readonly=True)
    state = fields.Selection(string='State', selection=[
        ('pending', 'Pending'), 
        ('in progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
        ])
    notes = fields.Text(string='Notes')
    
    
    
