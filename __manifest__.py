# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Calendar Meeting Status",
    'summary': "Track whether a meeting is unconfirmed, confirmed, done or cancelled, with a cancellation reason",
    'description': """
Calendar Meeting Status
=======================

Odoo's calendar knows whether each attendee accepted an invitation, but not
what became of the meeting itself. This app gives every meeting a status:

* **Unconfirmed** - a new meeting,
* **Confirmed** - it is going ahead,
* **Done** - it took place,
* **Cancelled** - it will not happen; you are asked for a reason, which is
  stored on the meeting and written to the chatter.

The status bar and its buttons are on the meeting form. The list view shows
the status as a colored badge and can be filtered and grouped by it.
""",
    'version': "17.0.1.0.1",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Productivity/Calendar",
    'depends': [
        'calendar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/calendar_event_views.xml',
        'wizard/calendar_event_cancel_views.xml',
    ],
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
