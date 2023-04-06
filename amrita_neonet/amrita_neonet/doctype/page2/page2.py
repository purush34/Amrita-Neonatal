# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class page2(Document):
	pass

@frappe.whitelist()
def create_page2(baby_id,mother_name):
	page2 = frappe.new_doc('page2')
	page2.baby_id = baby_id
	page2.mother_name = mother_name
	page2.save()

@frappe.whitelist()
def delete_page2(doc, method):
	page2 = frappe.get_doc('page2', {'baby_id': doc.baby_id})
	page2.delete()
	