# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Echocardiography(Document):
	pass

@frappe.whitelist()
def create_echocardiography(baby_id,mother_name):
	echocardiography = frappe.new_doc('Echocardiography')
	echocardiography.baby_id = baby_id
	echocardiography.mother_name = mother_name
	echocardiography.save()

@frappe.whitelist()
def delete_echocardiography(doc, method):
	echocardiography = frappe.get_doc('Echocardiography', {'baby_id': doc.baby_id})
	echocardiography.delete()
	