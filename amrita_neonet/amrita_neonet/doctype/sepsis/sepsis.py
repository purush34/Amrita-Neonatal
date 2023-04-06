# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sepsis(Document):
	pass


@frappe.whitelist()
def create_sepsis(baby_id,mother_name):
	sepsis = frappe.new_doc('Sepsis')
	sepsis.baby_id = baby_id
	sepsis.mother_name = mother_name
	sepsis.save()

@frappe.whitelist()
def delete_sepsis(doc, method):
	sepsis = frappe.get_doc('Sepsis', {'baby_id': doc.baby_id})
	sepsis.delete()
	