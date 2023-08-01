# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Genetic(Document):
	pass


@frappe.whitelist()
def create_genetic(baby_id,mother_name):
	genetic = frappe.new_doc('Genetic')
	genetic.baby_id = baby_id
	genetic.mother_name = mother_name
	genetic.save()

@frappe.whitelist()
def delete_genetic(doc, method):
	genetic = frappe.get_doc('Genetic', {'baby_id': doc.baby_id})
	genetic.delete()
	