# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Electroencephalography(Document):
	pass

@frappe.whitelist()
def create_electroencephalography(baby_id,mother_name):
	electroencephalography = frappe.new_doc('Electroencephalography')
	electroencephalography.baby_id = baby_id
	electroencephalography.mother_name = mother_name
	electroencephalography.save()

@frappe.whitelist()
def delete_electroencephalography(doc, method):
	electroencephalography = frappe.get_doc('Electroencephalography', {'baby_id': doc.baby_id})
	electroencephalography.delete()