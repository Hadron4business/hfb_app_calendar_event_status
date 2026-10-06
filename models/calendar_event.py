# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
"""	@version	20.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Meeting status
	Adds a status (unconfirmed, confirmed, done, cancelled) and a cancellation
	reason to calendar events, with the actions behind the status bar buttons.
"""
from odoo import _, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    meeting_state = fields.Selection(
        [
            ('draft', "Unconfirmed"),
            ('open', "Confirmed"),
            ('done', "Done"),
            ('cancel', "Cancelled"),
        ],
        string="Meeting Status", default='draft', required=True,
        tracking=True, copy=False, index=True,
    )
    cancel_reason = fields.Char(string="Cancellation Reason", copy=False)

    def action_meeting_draft(self):
        self.write({'meeting_state': 'draft', 'cancel_reason': False})

    def action_meeting_open(self):
        self.write({'meeting_state': 'open', 'cancel_reason': False})

    def action_meeting_done(self):
        self.write({'meeting_state': 'done', 'cancel_reason': False})

    def action_meeting_cancel(self):
        """Opens the wizard asking for the cancellation reason."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _("Cancel Meeting"),
            'res_model': 'calendar.event.cancel',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_event_id': self.id},
        }

#EoF
