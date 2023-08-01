# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Lumbarpuncture(Document):
	pass

@frappe.whitelist()
def create_lumbarpuncture(baby_id,mother_name):
	lumbarpuncture = frappe.new_doc('Lumbarpuncture')
	lumbarpuncture.baby_id = baby_id
	lumbarpuncture.mother_name = mother_name
	lumbarpuncture.save()

@frappe.whitelist()
def delete_lumbarpuncture(doc, method):
	lumbarpuncture = frappe.get_doc('Lumbarpuncture', {'baby_id': doc.baby_id})
	lumbarpuncture.delete()