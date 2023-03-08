# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta, time

from odoo import  fields, models, _


class HolidaysRequest(models.Model):
    _inherit = "hr.leave"
    

    def action_approve(self):
        # ~ Send mail to approve
        mail = self.env['mail.mail'].create({
                'subject': "Notification to approve",
                'email_from': self.env.user.login,
                'email_to': self.employee_id.work_email,
                'body_html': "description",
            })
        mail.send()
        return True

    def action_refuse(self):
        # ~ Send mail to refuse
        mail = self.env['mail.mail'].create({
                'subject': "Notification to refuse",
                'email_from': self.env.user.login,
                'email_to': self.employee_id.work_email,
                'body_html': "description",
            })
        mail.send()
        return True
