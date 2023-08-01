# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Peritonealdrain(Document):
	pass


@frappe.whitelist()
def create_peritonealdrain(baby_id,mother_name):
	peritonealdrain = frappe.new_doc('Peritonealdrain')
	peritonealdrain.baby_id = baby_id
	peritonealdrain.mother_name = mother_name
	peritonealdrain.save()

@frappe.whitelist()
def delete_peritonealdrain(doc, method):
	peritonealdrain = frappe.get_doc('Peritonealdrain', {'baby_id': doc.baby_id})
	peritonealdrain.delete()
	