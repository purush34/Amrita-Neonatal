# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Pericardialtap(Document):
	pass

@frappe.whitelist()
def create_pericardialtap(baby_id,mother_name):
	pericardialtap = frappe.new_doc('Pericardialtap')
	pericardialtap.baby_id = baby_id
	pericardialtap.mother_name = mother_name
	pericardialtap.save()

@frappe.whitelist()
def delete_pericardialtap(doc, method):
	pericardialtap = frappe.get_doc('Pericardialtap', {'baby_id': doc.baby_id})
	pericardialtap.delete()
	
