# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MaternalAndAntenatalDetails(Document):
	pass

@frappe.whitelist()
def create_maternal_and_antenatal_details(baby_id,mother_name):
	maternal_and_antenatal_details = frappe.new_doc('Maternal And Antenatal Details')
	maternal_and_antenatal_details.baby_id = baby_id
	maternal_and_antenatal_details.mother_name = mother_name
	maternal_and_antenatal_details.save()

@frappe.whitelist()
def delete_maternal_and_antenatal_details(doc, method):
	maternal_and_antenatal_details = frappe.get_doc('Maternal And Antenatal Details', {'baby_id': doc.baby_id})
	maternal_and_antenatal_details.delete()
	