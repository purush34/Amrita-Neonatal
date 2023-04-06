# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Cooloingcriteria(Document):
	pass

@frappe.whitelist()
def create_cooloingcriteria(baby_id,mother_name):
	cooloingcriteria = frappe.new_doc('Cooloingcriteria')
	cooloingcriteria.baby_id = baby_id
	cooloingcriteria.mother_name = mother_name
	cooloingcriteria.save()

@frappe.whitelist()
def delete_cooloingcriteria(doc, method):
	cooloingcriteria = frappe.get_doc('Cooloingcriteria', {'baby_id': doc.baby_id})
	cooloingcriteria.delete()