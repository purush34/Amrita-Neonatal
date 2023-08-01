# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PeripheralArterialline(Document):
	pass

@frappe.whitelist()
def create_peripheral_arterial_line(baby_id,mother_name):
	peripheral_arterial_line = frappe.new_doc('Peripheral Arterial Line')
	peripheral_arterial_line.baby_id = baby_id
	peripheral_arterial_line.mother_name = mother_name
	peripheral_arterial_line.save()

@frappe.whitelist()
def delete_peripheral_arterial_line(doc, method):
	peripheral_arterial_line = frappe.get_doc('Peripheral Arterial Line', {'baby_id': doc.baby_id})
	peripheral_arterial_line.delete()
	