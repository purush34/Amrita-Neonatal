# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ENTandSwallow(Document):
	pass

@frappe.whitelist()
def create_ent_and_swallow(baby_id,mother_name):
	ent_and_swallow = frappe.new_doc('ENTandSwallow')
	ent_and_swallow.baby_id = baby_id
	ent_and_swallow.mother_name = mother_name
	ent_and_swallow.save()

@frappe.whitelist()
def delete_ent_and_swallow(doc, method):
	ent_and_swallow = frappe.get_doc('ENTandSwallow', {'baby_id': doc.baby_id})
	ent_and_swallow.delete()
	