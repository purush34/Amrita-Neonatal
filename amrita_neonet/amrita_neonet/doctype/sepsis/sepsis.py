# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sepsis(Document):
	def before_save(self):
		"""
		"no_of_episodes_of_culture_postive_sepsis",
		"no_of_episodes_of_culture_negative_sepsis",
		"total_duration_of_iv_antibiotics_in_days",
		"column_break_x9iwe",
		"total_duration_of_reserve_antibiotics",
		"total_duration_of_antifungals",
		"no_of_central_lines_days"
		"""
		day = 0
		no_of_episodes_of_culture_postive_sepsis = 0
		no_of_episodes_of_culture_negative_sepsis = 0
		sepsis_child = self.get("daily_observations")
		for i in sepsis_child:
			if i.central_line_present == 'Yes':
				day += 1
			else:
				day = 0
			if i.blood_culture_in_past_24_hours == 'Yes':
				if i.last_blood_culture_report_within_past_72_hours == 'Positive':
					no_of_episodes_of_culture_postive_sepsis += 1
				elif i.last_blood_culture_report_within_past_72_hours == 'Negative':
					no_of_episodes_of_culture_negative_sepsis += 1

			i.no_of_days_of_central_line_in_situ = str(day)
		# days_antibiotics = 0
		# for i in self.get("antibiotics_used"):
		# 	days_antibiotics += i.number_of_days
		
		# days_antifungals = 0
		# for i in self.get("antifungals_used"):
		# 	days_antifungals += i.number_of_days
		self.no_of_episodes_of_culture_postive_sepsis = str(no_of_episodes_of_culture_postive_sepsis)
		self.no_of_episodes_of_culture_negative_sepsis = str(no_of_episodes_of_culture_negative_sepsis)
		# self.total_duration_of_iv_antibiotics_in_days = str(days_antibiotics)
		# self.total_duration_of_antifungals = str(days_antifungals)
		


@frappe.whitelist()
def create_sepsis(baby_id,mother_name):
	sepsis = frappe.new_doc('Sepsis')
	sepsis.baby_id = baby_id
	sepsis.mother_name = mother_name
	sepsis.save()

@frappe.whitelist()
def delete_sepsis(doc, method):
	sepsis = frappe.get_doc('Sepsis', {'baby_id': doc.baby_id})
	sepsis.delete()
	