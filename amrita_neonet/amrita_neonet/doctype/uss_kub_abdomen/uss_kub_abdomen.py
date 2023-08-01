# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class USSKUB_Abdomen(Document):
	pass

@frappe.whitelist()
def create_uss_kub_abdomen(baby_id,mother_name):
	uss_kub_abdomen = frappe.new_doc('USS KUB Abdomen')
	uss_kub_abdomen.baby_id = baby_id
	uss_kub_abdomen.mother_name = mother_name
	uss_kub_abdomen.save()

@frappe.whitelist()
def delete_uss_kub_abdomen(doc, method):
	uss_kub_abdomen = frappe.get_doc('USS KUB Abdomen', {'baby_id': doc.baby_id})
	uss_kub_abdomen.delete()
