# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Gastrointestinal(Document):
	
	def before_save(self):
		"""
		total_no_of_tpn_days",
		"day_to_reach_full_feeds",
		"day_to_reach_full_feeds_orally",
		"average_kcalories_per_day_during_stay",
		"column_break_1ijyw",
		"average_gir_content_per_day_during_stay",
		"average_protein_content_per_day_during_stay",
		"average_lipid_content_per_day_during_stay",
		"maximum_bilirubin",
		"total_no_of_days_of_phototherapy",
		"""
		total_no_of_tpn_days = 0
		day_to_reach_full_feeds = -1
		day_to_reach_full_feeds_orally = -1
		average_kcalories_per_day_during_stay = 0
		average_gir_content_per_day_during_stay = 0
		average_protein_content_per_day_during_stay = 0
		average_lipid_content_per_day_during_stay = 0
		maximum_bilirubin = 0
		total_no_of_days_of_phototherapy = 0
		day = 0
		tot_protein = 0
		full_feeds = 1
		full_feeds_orally = 1
		y = self.get_all_children()
		for row in y:
			if row.tpn == 'Yes':
				total_no_of_tpn_days += 1
			if row.full_enteral_feeds == 'Yes' and full_feeds:
				day_to_reach_full_feeds = row.day_of_life
				full_feeds = 0
			if row.full_oral_feeds == 'Yes' and full_feeds_orally:
				day_to_reach_full_feeds_orally = row.day1
				full_feeds_orally = 0
			average_kcalories_per_day_during_stay += row.total_kcal
			average_gir_content_per_day_during_stay += row.gir_mg
			if row.working_weight:
				average_protein_content_per_day_during_stay += (row.protein_kcal + row.total_protein_content)/row.working_weight
			average_lipid_content_per_day_during_stay += row.lipid_grams
			if row.jaundice == 'Yes':
				maximum_bilirubin += 1
			if row.phototherapy == 'Yes':
				total_no_of_days_of_phototherapy += 1
			if row.central_line_present == 'Yes':
				day += 1
			else:
				day = 0
			row.no_of_days_of_central_line_in_situ = str(day)
		lengthOfStay = len(y)
		self.total_no_of_tpn_days = total_no_of_tpn_days
		self.day_to_reach_full_feeds = day_to_reach_full_feeds
		self.day_to_reach_full_feeds_orally = day_to_reach_full_feeds_orally
		if  lengthOfStay:
			self.average_kcalories_per_day_during_stay = average_kcalories_per_day_during_stay / lengthOfStay
			self.average_gir_content_per_day_during_stay = average_gir_content_per_day_during_stay / lengthOfStay
			self.average_protein_content_per_day_during_stay = average_protein_content_per_day_during_stay / lengthOfStay
			self.average_lipid_content_per_day_during_stay = average_lipid_content_per_day_during_stay / lengthOfStay
		self.maximum_bilirubin = maximum_bilirubin
		self.total_no_of_days_of_phototherapy = total_no_of_days_of_phototherapy
		



@frappe.whitelist()
def getDayOfLife(baby_id,date):
	baby = frappe.get_doc("Opening page",  {'baby_id': baby_id})
	days = frappe.utils.date_diff(date, baby.dob)
	return days