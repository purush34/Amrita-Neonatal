# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Peritonealtap(Document):
	pass

@frappe.whitelist()
def create_peritoneal_tap(baby_id,mother_name):
	peritoneal_tap = frappe.new_doc('Peritoneal Tap')
	peritoneal_tap.baby_id = baby_id
	peritoneal_tap.mother_name = mother_name
	peritoneal_tap.save()

@frappe.whitelist()
def delete_peritoneal_tap(doc, method):
	peritoneal_tap = frappe.get_doc('Peritoneal Tap', {'baby_id': doc.baby_id})
	peritoneal_tap.delete()
	