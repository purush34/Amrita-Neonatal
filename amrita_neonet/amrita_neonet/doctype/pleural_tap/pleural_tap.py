# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Pleuraltap(Document):
	pass

@frappe.whitelist()
def create_pleuraltap(baby_id,mother_name):
	pleuraltap = frappe.new_doc('Pleuraltap')
	pleuraltap.baby_id = baby_id
	pleuraltap.mother_name = mother_name
	pleuraltap.save()

@frappe.whitelist()
def delete_pleuraltap(doc, method):
	pleuraltap = frappe.get_doc('Pleuraltap', {'baby_id': doc.baby_id})
	pleuraltap.delete()

