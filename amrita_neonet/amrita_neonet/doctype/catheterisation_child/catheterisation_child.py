# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Catheterisation_child(Document):
	pass

@frappe.whitelist()
def create_catheterisation_child(baby_id,mother_name):
	catheterisation_child = frappe.new_doc('Catheterisation_child')
	catheterisation_child.baby_id = baby_id
	catheterisation_child.mother_name = mother_name
	catheterisation_child.save()

@frappe.whitelist()
def delete_catheterisation_child(doc, method):
	catheterisation_child = frappe.get_doc('Catheterisation_child', {'baby_id': doc.baby_id})
	catheterisation_child.delete()
