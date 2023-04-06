# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CoolingCriteria(Document):
	pass


@frappe.whitelist()
def create_cooling_criteria(baby_id,mother_name):
	cooling_criteria = frappe.new_doc('Cooling Criteria')
	cooling_criteria.baby_id = baby_id
	cooling_criteria.mother_name = mother_name
	cooling_criteria.save()

@frappe.whitelist()
def delete_cooling_criteria(doc, method):
	cooling_criteria = frappe.get_doc('Cooling Criteria', {'baby_id': doc.baby_id})
	cooling_criteria.delete()