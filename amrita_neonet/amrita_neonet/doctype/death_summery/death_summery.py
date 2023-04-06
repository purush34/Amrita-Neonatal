# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Deathsummery(Document):
	pass

@frappe.whitelist()
def create_death_summery(baby_id,mother_name):
	death_summery = frappe.new_doc('Death Summery')
	death_summery.baby_id = baby_id
	death_summery.mother_name = mother_name
	death_summery.save()

@frappe.whitelist()
def delete_death_summery(doc, method):
	death_summery = frappe.get_doc('Death Summery', {'baby_id': doc.baby_id})
	death_summery.delete()