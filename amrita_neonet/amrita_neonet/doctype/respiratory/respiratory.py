# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Respiratory(Document):
	pass

@frappe.whitelist()
def create_respiratory(baby_id,mother_name):
	respiratory = frappe.new_doc('Respiratory')
	respiratory.baby_id = baby_id
	respiratory.mother_name = mother_name
	respiratory.save()

@frappe.whitelist()
def delete_respiratory(doc, method):
	respiratory = frappe.get_doc('Respiratory', {'baby_id': doc.baby_id})
	respiratory.delete()
	