# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Haematology(Document):
	pass

@frappe.whitelist()
def create_haematology(baby_id,mother_name):
	haematology = frappe.new_doc('Haematology')
	haematology.baby_id = baby_id
	haematology.mother_name = mother_name
	haematology.save()

@frappe.whitelist()
def delete_haematology(doc, method):
	haematology = frappe.get_doc('Haematology', {'baby_id': doc.baby_id})
	haematology.delete()
