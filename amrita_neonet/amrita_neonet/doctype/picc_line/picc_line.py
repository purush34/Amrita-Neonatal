# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PICCline(Document):
	pass

@frappe.whitelist()
def create_picc_line(baby_id,mother_name):
	picc_line = frappe.new_doc('PICCline')
	picc_line.baby_id = baby_id
	picc_line.mother_name = mother_name
	picc_line.save()

@frappe.whitelist()
def delete_picc_line(doc, method):
	picc_line = frappe.get_doc('PICCline', {'baby_id': doc.baby_id})
	picc_line.delete()
	