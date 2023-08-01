# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NasoPharyngealtube(Document):
	pass


@frappe.whitelist()
def create_naso__pharyngeal_tube(baby_id,mother_name):
	naso__pharyngeal_tube = frappe.new_doc('Naso Pharyngeal tube')
	naso__pharyngeal_tube.baby_id = baby_id
	naso__pharyngeal_tube.mother_name = mother_name
	naso__pharyngeal_tube.save()

@frappe.whitelist()
def delete_naso__pharyngeal_tube(doc, method):
	naso__pharyngeal_tube = frappe.get_doc('Naso Pharyngeal tube', {'baby_id': doc.baby_id})
	naso__pharyngeal_tube.delete()
	