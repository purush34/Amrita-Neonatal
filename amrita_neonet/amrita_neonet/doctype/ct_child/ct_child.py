# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CT_child(Document):
	pass

@frappe.whitelist()
def create_ct_child(baby_id,mother_name):
	ct_child = frappe.new_doc('CT_child')
	ct_child.baby_id = baby_id
	ct_child.mother_name = mother_name
	ct_child.save()

@frappe.whitelist()
def delete_ct_child(doc, method):
	ct_child = frappe.get_doc('CT_child', {'baby_id': doc.baby_id})
	ct_child.delete()

	