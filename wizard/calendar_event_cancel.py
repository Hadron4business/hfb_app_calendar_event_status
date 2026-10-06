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
"""	@version	19.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Cancel meeting wizard
	Asks for a reason before a meeting is set to Cancelled, stores it on the
	meeting and posts it in the chatter.
"""
from odoo import _, fields, models


class CalendarEventCancel(models.TransientModel):
    _name = 'calendar.event.cancel'
    _description = "Cancel Meeting"

    event_id = fields.Many2one('calendar.event', string="Meeting", required=True, ondelete='cascade')
    reason = fields.Char(string="Reason", required=True)

    def action_confirm(self):
        self.ensure_one()
        event = self.event_id
        event.write({'meeting_state': 'cancel', 'cancel_reason': self.reason})
        event.message_post(body=_("Meeting cancelled. Reason: %s") % self.reason)
        return {'type': 'ir.actions.act_window_close'}

#EoF
