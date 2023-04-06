# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NGtubeinsertion(Document):
	pass

@frappe.whitelist()
def create_ng_tube_insertion(baby_id,mother_name):
	ng_tube_insertion = frappe.new_doc('NG tube insertion')
	ng_tube_insertion.baby_id = baby_id
	ng_tube_insertion.mother_name = mother_name
	ng_tube_insertion.save()

@frappe.whitelist()
def delete_ng_tube_insertion(doc, method):
	ng_tube_insertion = frappe.get_doc('NG tube insertion', {'baby_id': doc.baby_id})
	ng_tube_insertion.delete()
	