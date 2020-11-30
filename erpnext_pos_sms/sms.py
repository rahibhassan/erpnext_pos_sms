from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, getdate, today
from frappe import throw, _
from frappe.utils.nestedset import NestedSet, get_ancestors_of, get_descendants_of
import json 



def send_sms(doc, event):
    mobile_number = frappe.db.get_value('Customer', {'name': doc.customer}, ['mobile_number'])
    from frappe.core.doctype.sms_settings.sms_settings import send_sms
    message = "Thank you for your purchase at Frapino. You have spent Rs " + str(doc.grand_total) + " via Cash on : "  + (doc.posting_date)
    send_sms([mobile_number], msg=message)

    