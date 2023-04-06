# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Test1(Document):
	pass

@frappe.whitelist()
def create_test_1(baby_id,mother_name):
	test_1 = frappe.new_doc('Test 1')
	test_1.baby_id = baby_id
	test_1.mother_name = mother_name
	test_1.save()

@frappe.whitelist()
def delete_test_1(doc, method):
	test_1 = frappe.get_doc('Test 1', {'baby_id': doc.baby_id})
	test_1.delete()
	