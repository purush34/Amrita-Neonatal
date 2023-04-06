# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Umbiilicallines(Document):
	pass

@frappe.whitelist()
def create_umbiilical_lines(baby_id,mother_name):
	umbiilical_lines = frappe.new_doc('Umbiilical Lines')
	umbiilical_lines.baby_id = baby_id
	umbiilical_lines.mother_name = mother_name
	umbiilical_lines.save()

@frappe.whitelist()
def delete_umbiilical_lines(doc, method):
	umbiilical_lines = frappe.get_doc('Umbiilical Lines', {'baby_id': doc.baby_id})
	umbiilical_lines.delete()
	
