# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dischargeletter(Document):
	pass

@frappe.whitelist()
def create_dischargeletter(baby_id,mother_name):
	dischargeletter = frappe.new_doc('Dischargeletter')
	dischargeletter.baby_id = baby_id
	dischargeletter.mother_name = mother_name
	dischargeletter.save()

@frappe.whitelist()
def delete_dischargeletter(doc, method):
	dischargeletter = frappe.get_doc('Dischargeletter', {'baby_id': doc.baby_id})
	dischargeletter.delete()
	