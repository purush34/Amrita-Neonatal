# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Neogen(Document):
	pass

@frappe.whitelist()
def create_neogen(baby_id,mother_name):
	neogen = frappe.new_doc('Neogen')
	neogen.baby_id = baby_id
	neogen.mother_name = mother_name
	neogen.save()

@frappe.whitelist()
def delete_neogen(doc, method):
	neogen = frappe.get_doc('Neogen', {'baby_id': doc.baby_id})
	neogen.delete()
