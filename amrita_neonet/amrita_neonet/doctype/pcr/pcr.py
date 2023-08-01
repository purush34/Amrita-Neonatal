# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PCR(Document):
	pass

@frappe.whitelist()
def create_pcr(baby_id,mother_name):
	pcr = frappe.new_doc('PCR')
	pcr.baby_id = baby_id
	pcr.mother_name = mother_name
	pcr.save()

@frappe.whitelist()
def delete_pcr(doc, method):
	pcr = frappe.get_doc('PCR', {'baby_id': doc.baby_id})
	pcr.delete()
	
