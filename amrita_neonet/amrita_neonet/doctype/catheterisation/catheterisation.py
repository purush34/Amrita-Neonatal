# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Catheterisation(Document):
	pass


@frappe.whitelist()
def create_catheterisation(baby_id,mother_name):
	catheterisation = frappe.new_doc('Catheterisation')
	catheterisation.baby_id = baby_id
	catheterisation.mother_name = mother_name
	catheterisation.save()

@frappe.whitelist()
def delete_catheterisation(doc, method):
	catheterisation = frappe.get_doc('Catheterisation', {'baby_id': doc.baby_id})
	catheterisation.delete()
	