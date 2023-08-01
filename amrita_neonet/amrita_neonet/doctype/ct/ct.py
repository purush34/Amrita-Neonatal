# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CT(Document):
	pass

@frappe.whitelist()
def create_ct(baby_id,mother_name):
	ct = frappe.new_doc('CT')
	ct.baby_id = baby_id
	ct.mother_name = mother_name
	ct.save()

@frappe.whitelist()
def delete_ct(doc, method):
	ct = frappe.get_doc('CT', {'baby_id': doc.baby_id})
	ct.delete()
	