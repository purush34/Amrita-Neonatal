# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Renal(Document):
	pass

@frappe.whitelist()
def create_renal(baby_id,mother_name):
	renal = frappe.new_doc('Renal')
	renal.baby_id = baby_id
	renal.mother_name = mother_name
	renal.save()

@frappe.whitelist()
def delete_renal(doc, method):
	renal = frappe.get_doc('Renal', {'baby_id': doc.baby_id})
	renal.delete()
	