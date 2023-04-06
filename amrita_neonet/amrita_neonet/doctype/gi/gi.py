# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GI(Document):
	pass

@frappe.whitelist()
def create_gi(baby_id,mother_name):
	gi = frappe.new_doc('GI')
	gi.baby_id = baby_id
	gi.mother_name = mother_name
	gi.save()

@frappe.whitelist()
def delete_gi(doc, method):
	gi = frappe.get_doc('GI', {'baby_id': doc.baby_id})
	gi.delete()
