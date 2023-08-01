# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Endocrineandmetabolic(Document):
	pass


@frappe.whitelist()
def create_endocrineandmetabolic(baby_id,mother_name):
	endocrineandmetabolic = frappe.new_doc('Endocrineandmetabolic')
	endocrineandmetabolic.baby_id = baby_id
	endocrineandmetabolic.mother_name = mother_name
	endocrineandmetabolic.save()

@frappe.whitelist()
def delete_endocrineandmetabolic(doc, method):
	endocrineandmetabolic = frappe.get_doc('Endocrineandmetabolic', {'baby_id': doc.baby_id})
	endocrineandmetabolic.delete()
	