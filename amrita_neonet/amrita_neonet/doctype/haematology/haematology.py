# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Haematology(Document):
	""" 
	no_of_days_exchange_transfusion_past_24_hours",
	"no_of_days_prbc_past_24_hours",
	"no_of_days_platelets_past_24_hours",
	"no_of_days_ffp_past_24_hours",
	"column_break_bgeeo",
	"no_of_days_cryoprecipitate_past_24_hours",
	"no_of_days_ivig_past_24_hours"
	"""
	def before_save(self):
		no_of_days_exchange_transfusion_past_24_hours = 0
		no_of_days_prbc_past_24_hours = 0
		no_of_days_platelets_past_24_hours = 0
		no_of_days_ffp_past_24_hours = 0
		no_of_days_cryoprecipitate_past_24_hours = 0
		no_of_days_ivig_past_24_hours = 0

		for child in self.get_all_children():
			if child.transfusion == "Yes":
				no_of_days_exchange_transfusion_past_24_hours += 1
			if child.prbc == "Yes":
				no_of_days_prbc_past_24_hours += 1
			if child.platelets == "Yes":
				no_of_days_platelets_past_24_hours += 1
			if child.ffp == "Yes":
				no_of_days_ffp_past_24_hours += 1
			if child.cryoprecipitate == "Yes":
				no_of_days_cryoprecipitate_past_24_hours += 1
			if child.ivig == "Yes":
				no_of_days_ivig_past_24_hours += 1

		self.no_of_days_exchange_transfusion_past_24_hours = no_of_days_exchange_transfusion_past_24_hours
		self.no_of_days_prbc_past_24_hours = no_of_days_prbc_past_24_hours
		self.no_of_days_platelets_past_24_hours = no_of_days_platelets_past_24_hours
		self.no_of_days_ffp_past_24_hours = no_of_days_ffp_past_24_hours
		self.no_of_days_cryoprecipitate_past_24_hours = no_of_days_cryoprecipitate_past_24_hours
		self.no_of_days_ivig_past_24_hours = no_of_days_ivig_past_24_hours
		

@frappe.whitelist()
def create_haematology(baby_id,mother_name):
	haematology = frappe.new_doc('Haematology')
	haematology.baby_id = baby_id
	haematology.mother_name = mother_name
	haematology.save()

@frappe.whitelist()
def delete_haematology(doc, method):
	haematology = frappe.get_doc('Haematology', {'baby_id': doc.baby_id})
	haematology.delete()
