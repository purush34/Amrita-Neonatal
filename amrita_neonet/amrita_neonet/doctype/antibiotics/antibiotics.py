# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Antibiotics(Document):
	pass


@frappe.whitelist()	
def create_antibiotics(baby_id,mother_name):
	antibiotics = frappe.new_doc('Antibiotics')
	antibiotics.baby_id = baby_id
	antibiotics.mother_name = mother_name
	antibiotics.save()


@frappe.whitelist()
def delete_admission(doc, method):
	antibiotics = frappe.get_doc('Antibiotics', {'baby_id': doc.baby_id})
	antibiotics.delete()