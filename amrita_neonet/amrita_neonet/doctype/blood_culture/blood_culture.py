# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Bloodculture(Document):
	pass


@frappe.whitelist()
def create_blood_culture(baby_id,mother_name):
	blood_culture = frappe.new_doc('Blood Culture')
	blood_culture.baby_id = baby_id
	blood_culture.mother_name = mother_name
	blood_culture.save()

@frappe.whitelist()
def delete_blood_culture(doc, method):
	blood_culture = frappe.get_doc('Blood Culture', {'baby_id': doc.baby_id})
	blood_culture.delete()
	