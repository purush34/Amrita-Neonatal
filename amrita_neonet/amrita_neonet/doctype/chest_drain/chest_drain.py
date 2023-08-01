# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Chestdrain(Document):
	pass


@frappe.whitelist()
def create_chestdrain(baby_id,mother_name):
	chestdrain = frappe.new_doc('Chestdrain')
	chestdrain.baby_id = baby_id
	chestdrain.mother_name = mother_name
	chestdrain.save()

@frappe.whitelist()
def delete_chestdrain(doc, method):
	chestdrain = frappe.get_doc('Chestdrain', {'baby_id': doc.baby_id})
	chestdrain.delete()
	