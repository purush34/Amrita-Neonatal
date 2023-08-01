# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Opthalmology(Document):
	pass

@frappe.whitelist()
def create_opthalmology(baby_id,mother_name):
	opthalmology = frappe.new_doc('Opthalmology')
	opthalmology.baby_id = baby_id
	opthalmology.mother_name = mother_name
	opthalmology.save()

@frappe.whitelist()
def delete_opthalmology(doc, method):
	opthalmology = frappe.get_doc('Opthalmology', {'baby_id': doc.baby_id})
	opthalmology.delete()
