# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RetinopathyofPrematurity(Document):
	pass

@frappe.whitelist()
def create_retinopathyofprematurity(baby_id,mother_name):
	retinopathyofprematurity = frappe.new_doc('RetinopathyofPrematurity')
	retinopathyofprematurity.baby_id = baby_id
	retinopathyofprematurity.mother_name = mother_name
	retinopathyofprematurity.save()

@frappe.whitelist()
def delete_retinopathyofprematurity(doc, method):
	retinopathyofprematurity = frappe.get_doc('RetinopathyofPrematurity', {'baby_id': doc.baby_id})
	retinopathyofprematurity.delete()
	