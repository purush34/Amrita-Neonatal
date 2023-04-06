# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class page3(Document):
	pass

@frappe.whitelist()
def create_page3(baby_id,mother_name):
	page3 = frappe.new_doc('page3')
	page3.baby_id = baby_id
	page3.mother_name = mother_name
	page3.save()

@frappe.whitelist()
def delete_page3(doc, method):
	page3 = frappe.get_doc('page3', {'baby_id': doc.baby_id})
	page3.delete()
	