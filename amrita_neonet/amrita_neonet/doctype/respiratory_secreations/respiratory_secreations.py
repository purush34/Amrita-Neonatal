# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Respiratorysecreations(Document):
	pass

@frappe.whitelist()
def create_respiratory_secreations(baby_id,mother_name):
	respiratory_secreations = frappe.new_doc('Respiratorysecreations')
	respiratory_secreations.baby_id = baby_id
	respiratory_secreations.mother_name = mother_name
	respiratory_secreations.save()

@frappe.whitelist()
def delete_respiratory_secreations(doc, method):
	respiratory_secreations = frappe.get_doc('Respiratorysecreations', {'baby_id': doc.baby_id})
	respiratory_secreations.delete()

