# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

# import frappe
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
		day_to_reach_full_feeds = 0
		day_to_reach_full_feeds_orally = 0
		average_kcalories_per_day_during_stay = 0
		average_gir_content_per_day_during_stay = 0
		average_protein_content_per_day_during_stay = 0
		average_lipid_content_per_day_during_stay = 0
		maximum_bilirubin = 0
		total_no_of_days_of_phototherapy = 0

		for row in self.get_all_children():
			if row.tpn == 'Yes':
				total_no_of_tpn_days += 1
			if row.full_enteral_feeds == 'Yes':
				day_to_reach_full_feeds += 1
			if row.full_oral_feeds == 'Yes':
				day_to_reach_full_feeds_orally += 1
			average_kcalories_per_day_during_stay += row.total_kcal
			average_gir_content_per_day_during_stay += row.gir_kcal
			average_protein_content_per_day_during_stay += row.protein_kcal
			average_lipid_content_per_day_during_stay += row.lipid_kcal
			if row.jaundice == 'Yes':
				maximum_bilirubin += 1
			if row.phototherapy == 'Yes':
				total_no_of_days_of_phototherapy += 1

		self.total_no_of_tpn_days = total_no_of_tpn_days
		self.day_to_reach_full_feeds = day_to_reach_full_feeds
		self.day_to_reach_full_feeds_orally = day_to_reach_full_feeds_orally
		self.average_kcalories_per_day_during_stay = average_kcalories_per_day_during_stay
		self.average_gir_content_per_day_during_stay = average_gir_content_per_day_during_stay
		self.average_protein_content_per_day_during_stay = average_protein_content_per_day_during_stay
		self.average_lipid_content_per_day_during_stay = average_lipid_content_per_day_during_stay
		self.maximum_bilirubin = maximum_bilirubin
		self.total_no_of_days_of_phototherapy = total_no_of_days_of_phototherapy
		
