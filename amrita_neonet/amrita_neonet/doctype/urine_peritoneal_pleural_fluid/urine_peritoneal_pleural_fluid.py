# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Urine_Peritoneal_Pleuralfluid(Document):
	pass

@frappe.whitelist()
def create_urine_peritoneal_pleural_fluid(baby_id,mother_name):
	urine_peritoneal_pleural_fluid = frappe.new_doc('Urine Peritoneal Pleural Fluid')
	urine_peritoneal_pleural_fluid.baby_id = baby_id
	urine_peritoneal_pleural_fluid.mother_name = mother_name
	urine_peritoneal_pleural_fluid.save()

@frappe.whitelist()
def delete_urine_peritoneal_pleural_fluid(doc, method):
	urine_peritoneal_pleural_fluid = frappe.get_doc('Urine Peritoneal Pleural Fluid', {'baby_id': doc.baby_id})
	urine_peritoneal_pleural_fluid.delete()
	