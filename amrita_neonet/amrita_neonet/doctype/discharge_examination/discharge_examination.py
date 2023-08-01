# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dischargeexamination(Document):
	pass


@frappe.whitelist()
def create_discharge_examination(baby_id,mother_name):
	discharge_examination = frappe.new_doc('Discharge Examination')
	discharge_examination.baby_id = baby_id
	discharge_examination.mother_name = mother_name
	discharge_examination.save()

@frappe.whitelist()
def delete_discharge_examination(doc, method):
	discharge_examination = frappe.get_doc('Discharge Examination', {'baby_id': doc.baby_id})
	discharge_examination.delete()