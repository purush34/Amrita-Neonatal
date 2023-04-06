# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GeneticTests(Document):
	pass


@frappe.whitelist()
def create_genetic_tests(baby_id,mother_name):
	genetic_tests = frappe.new_doc('Genetic Tests')
	genetic_tests.baby_id = baby_id
	genetic_tests.mother_name = mother_name
	genetic_tests.save()

@frappe.whitelist()
def delete_genetic_tests(doc, method):
	genetic_tests = frappe.get_doc('Genetic Tests', {'baby_id': doc.baby_id})
	genetic_tests.delete()