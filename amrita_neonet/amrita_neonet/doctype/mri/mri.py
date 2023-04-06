# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MRI(Document):
	pass


@frappe.whitelist()
def create_mri(baby_id,mother_name):
	mri = frappe.new_doc('MRI')
	mri.baby_id = baby_id
	mri.mother_name = mother_name
	mri.save()

@frappe.whitelist()
def delete_mri(doc, method):
	mri = frappe.get_doc('MRI', {'baby_id': doc.baby_id})
	mri.delete()
	