# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class testBabies(Document):
	pass

"""
page1
page2
page3
"""

@frappe.whitelist()
def before_insert(doc, method):
    frappe.enqueue('amrita_neonet.amrita_neonet.doctype.page1.page1.create_page1', args=(doc.baby_id, doc.mother_name), method='POST')
