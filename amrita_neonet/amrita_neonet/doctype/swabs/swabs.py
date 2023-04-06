# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Swabs(Document):
	pass


@frappe.whitelist()
def create_swabs(baby_id,mother_name):
	swabs = frappe.new_doc('Swabs')
	swabs.baby_id = baby_id
	swabs.mother_name = mother_name
	swabs.save()

@frappe.whitelist()
def delete_swabs(doc, method):
	swabs = frappe.get_doc('Swabs', {'baby_id': doc.baby_id})
	swabs.delete()
	