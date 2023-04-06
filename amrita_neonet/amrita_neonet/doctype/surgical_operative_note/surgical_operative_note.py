# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SurgicalOperativeNote(Document):
	pass

@frappe.whitelist()
def create_surgical_operative_note(baby_id,mother_name):
	surgical_operative_note = frappe.new_doc('Surgical Operative Note')
	surgical_operative_note.baby_id = baby_id
	surgical_operative_note.mother_name = mother_name
	surgical_operative_note.save()

@frappe.whitelist()
def delete_surgical_operative_note(doc, method):
	surgical_operative_note = frappe.get_doc('Surgical Operative Note', {'baby_id': doc.baby_id})
	surgical_operative_note.delete()
	