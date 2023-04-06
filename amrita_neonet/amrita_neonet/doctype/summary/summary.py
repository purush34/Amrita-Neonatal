# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Summary(Document):
	pass

@frappe.whitelist()
def create_summary(baby_id,mother_name):
	summary = frappe.new_doc('Summary')
	summary.baby_id = baby_id
	summary.mother_name = mother_name
	summary.save()

@frappe.whitelist()
def delete_summary(doc, method):
	summary = frappe.get_doc('Summary', {'baby_id': doc.baby_id})
	summary.delete()
	