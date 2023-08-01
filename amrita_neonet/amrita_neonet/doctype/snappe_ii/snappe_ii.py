# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SnappeII(Document):
	pass

@frappe.whitelist()
def create_snappe_ii(baby_id,mother_name):
	snappe_ii = frappe.new_doc('Snappe II')
	snappe_ii.baby_id = baby_id
	snappe_ii.mother_name = mother_name
	snappe_ii.save()

@frappe.whitelist()
def delete_snappe_ii(doc, method):
	snappe_ii = frappe.get_doc('Snappe II', {'baby_id': doc.baby_id})
	snappe_ii.delete()
	