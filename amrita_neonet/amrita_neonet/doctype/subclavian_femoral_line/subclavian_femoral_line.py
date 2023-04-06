# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Subclavian_femoralline(Document):
	pass

@frappe.whitelist()
def create_subclavian_femoral_line(baby_id,mother_name):
	subclavian_femoral_line = frappe.new_doc('Subclavian Femoral Line')
	subclavian_femoral_line.baby_id = baby_id
	subclavian_femoral_line.mother_name = mother_name
	subclavian_femoral_line.save()

@frappe.whitelist()
def delete_subclavian_femoral_line(doc, method):
	subclavian_femoral_line = frappe.get_doc('Subclavian Femoral Line', {'baby_id': doc.baby_id})
	subclavian_femoral_line.delete()
	