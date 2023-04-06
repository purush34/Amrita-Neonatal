# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Intubation_child(Document):
	pass

@frappe.whitelist()
def create_intubation_child(baby_id,mother_name):
	intubation_child = frappe.new_doc('Intubation_child')
	intubation_child.baby_id = baby_id
	intubation_child.mother_name = mother_name
	intubation_child.save()

@frappe.whitelist()
def delete_intubation_child(doc, method):
	intubation_child = frappe.get_doc('Intubation_child', {'baby_id': doc.baby_id})
	intubation_child.delete()
	