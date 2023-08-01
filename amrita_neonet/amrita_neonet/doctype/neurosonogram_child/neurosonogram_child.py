# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Neurosonogram_child(Document):
	pass

@frappe.whitelist()
def create_neurosonogram_child(baby_id,mother_name):
	neurosonogram_child = frappe.new_doc('Neurosonogram_child')
	neurosonogram_child.baby_id = baby_id
	neurosonogram_child.mother_name = mother_name
	neurosonogram_child.save()

@frappe.whitelist()
def delete_neurosonogram_child(doc, method):
	neurosonogram_child = frappe.get_doc('Neurosonogram_child', {'baby_id': doc.baby_id})
	neurosonogram_child.delete()
	