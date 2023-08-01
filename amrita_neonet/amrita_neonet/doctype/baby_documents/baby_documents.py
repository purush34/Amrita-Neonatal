# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BabyDocuments(Document):
	pass


@frappe.whitelist()
def create_baby_documents(baby_id,mother_name):
	baby_documents = frappe.new_doc('Baby Documents')
	baby_documents.baby_id = baby_id
	baby_documents.mother_name = mother_name
	baby_documents.save()

@frappe.whitelist()
def delete_baby_documents(doc, method):
	baby_documents = frappe.get_doc('Baby Documents', {'baby_id': doc.baby_id})
	baby_documents.delete()