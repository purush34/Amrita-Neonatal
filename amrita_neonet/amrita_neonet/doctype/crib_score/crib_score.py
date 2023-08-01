# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CRIBscore(Document):
	pass


@frappe.whitelist()
def create_crib_score(baby_id,mother_name):
	crib_score = frappe.new_doc('CRIBscore')
	crib_score.baby_id = baby_id
	crib_score.mother_name = mother_name
	crib_score.save()

@frappe.whitelist()
def delete_crib_score(doc, method):
	crib_score = frappe.get_doc('CRIBscore', {'baby_id': doc.baby_id})
	crib_score.delete()
	
