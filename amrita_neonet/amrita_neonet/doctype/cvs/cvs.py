# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CVS(Document):
	pass


@frappe.whitelist()
def create_cvs(baby_id,mother_name):
	cvs = frappe.new_doc('CVS')
	cvs.baby_id = baby_id
	cvs.mother_name = mother_name
	cvs.save()

@frappe.whitelist()
def delete_cvs(doc, method):
	cvs = frappe.get_doc('CVS', {'baby_id': doc.baby_id})
	cvs.delete()
	