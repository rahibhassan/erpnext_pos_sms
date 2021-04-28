from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, getdate, today
from frappe import throw, _
from frappe.utils.nestedset import NestedSet, get_ancestors_of, get_descendants_of
import json
from erpnext_pos_sms import url_shorten



def send_sms(doc, event):
    mobile_number = frappe.db.get_value('Customer', {'name': doc.customer}, ['mobile_number'])
    from frappe.core.doctype.sms_settings.sms_settings import send_sms
    #url = 
    url = "http://store1.frapino.in/files/{}.pdf".format(doc.name)
    url_short = url_shorten.make_shorten(url)
    message = "Thank you for your purchase at Frapino. You have spent Rs " + str(doc.grand_total) +"via cash on "+ (doc.posting_date)+" "+"."+" Click the link to view your invoice "+ url_short+"."
    send_sms([mobile_number], msg=message)
    

    