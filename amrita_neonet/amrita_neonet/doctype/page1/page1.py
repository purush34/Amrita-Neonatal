# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class page1(Document):
	pass

@frappe.whitelist()
def create_page1(baby_id,mother_name):
	page1 = frappe.new_doc('page1')
	page1.baby_id = baby_id
	page1.mother_name = mother_name
	page1.save()

@frappe.whitelist()
def delete_page1(doc, method):
	page1 = frappe.get_doc('page1', {'baby_id': doc.baby_id})
	page1.delete()
	

@frappe.whitelist()
def say_hello():
	return "Hello"
