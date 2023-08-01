# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dischargechecklist(Document):
	pass


@frappe.whitelist()
def create_dischargechecklist(baby_id,mother_name):
	dischargechecklist = frappe.new_doc('Dischargechecklist')
	dischargechecklist.baby_id = baby_id
	dischargechecklist.mother_name = mother_name
	dischargechecklist.save()

@frappe.whitelist()
def delete_dischargechecklist(doc, method):
	dischargechecklist = frappe.get_doc('Dischargechecklist', {'baby_id': doc.baby_id})
	dischargechecklist.delete()
	