# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CNS(Document):
	pass


@frappe.whitelist()
def create_cns(baby_id,mother_name):
	cns = frappe.new_doc('CNS')
	cns.baby_id = baby_id
	cns.mother_name = mother_name
	cns.save()

@frappe.whitelist()
def delete_cns(doc, method):
	cns = frappe.get_doc('CNS', {'baby_id': doc.baby_id})
	cns.delete()