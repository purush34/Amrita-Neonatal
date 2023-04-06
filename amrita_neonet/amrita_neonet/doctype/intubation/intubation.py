# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Intubation(Document):
	pass

@frappe.whitelist()
def create_intubation(baby_id,mother_name):
	intubation = frappe.new_doc('Intubation')
	intubation.baby_id = baby_id
	intubation.mother_name = mother_name
	intubation.save()

@frappe.whitelist()
def delete_intubation(doc, method):
	intubation = frappe.get_doc('Intubation', {'baby_id': doc.baby_id})
	intubation.delete()
	