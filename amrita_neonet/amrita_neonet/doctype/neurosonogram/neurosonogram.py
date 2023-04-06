# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Neurosonogram(Document):
	pass

@frappe.whitelist()
def create_neurosonogram(baby_id,mother_name):
	neurosonogram = frappe.new_doc('Neurosonogram')
	neurosonogram.baby_id = baby_id
	neurosonogram.mother_name = mother_name
	neurosonogram.save()

@frappe.whitelist()
def delete_neurosonogram(doc, method):
	neurosonogram = frappe.get_doc('Neurosonogram', {'baby_id': doc.baby_id})
	neurosonogram.delete()

