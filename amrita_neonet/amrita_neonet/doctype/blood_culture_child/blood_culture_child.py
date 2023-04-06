# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Bloodculture_child(Document):
	pass


@frappe.whitelist()
def create_blood_culture_child(baby_id,mother_name):
	blood_culture_child = frappe.new_doc('Blood Culture Child')
	blood_culture_child.baby_id = baby_id
	blood_culture_child.mother_name = mother_name
	blood_culture_child.save()

@frappe.whitelist()
def delete_blood_culture_child(doc, method):
	blood_culture_child = frappe.get_doc('Blood Culture Child', {'baby_id': doc.baby_id})
	blood_culture_child.delete()
	