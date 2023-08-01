# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CVS(Document):
	""" 
	"inotropic_support_dopamime_days",
	"inotropic_support_dobutamine_days",
	"inotropic_support_adrenaline_days",
	"inotropic_support_noradrenaline_days",
	"column_break_vpzck",
	"inotropic_support_hydroocortisone_days",
	"no_of_days_need_for_prostin",
	"no_of_hs_pda_medical_courses_paracetmol",
	"no_of_hs_pda_medical_courses_ibuprofin", 
    """
	

	def before_save(self):
		inotropic_support_dopamime_days = 0
		inotropic_support_dobutamine_days = 0
		inotropic_support_adrenaline_days = 0
		inotropic_support_noradrenaline_days = 0
		inotropic_support_hydroocortisone_days = 0
		no_of_days_need_for_prostin = 0
		no_of_hs_pda_medical_courses_paracetmol = 0
		no_of_hs_pda_medical_courses_ibuprofin = 0
		no_hs_pda_surgical = 0
		for child in self.get_all_children():
			if child.inotropic_support == 'Yes':
				if child.dopamine:
					inotropic_support_dopamime_days += 1
				if child.dobutamine:
					inotropic_support_dobutamine_days += 1
				if child.adrenaline:
					inotropic_support_adrenaline_days += 1
				if child.noradrenaline:
					inotropic_support_noradrenaline_days += 1
				if child.hydroocortisone:
					inotropic_support_hydroocortisone_days += 1
			if child.need_for_prostin == 'Yes':
				no_of_days_need_for_prostin += 1
			if child.hs_pda == 'Yes':
				if child.hs_type == 'Medical':
					if child.medicine == 'Paracetmol':
						no_of_hs_pda_medical_courses_paracetmol += 1
					elif child.medicine == 'Ibuprofin':
						no_of_hs_pda_medical_courses_ibuprofin += 1
				else:
					no_hs_pda_surgical += 1
		
		self.inotropic_support_dopamime_days = inotropic_support_dopamime_days
		self.inotropic_support_dobutamine_days = inotropic_support_dobutamine_days
		self.inotropic_support_adrenaline_days = inotropic_support_adrenaline_days
		self.inotropic_support_noradrenaline_days = inotropic_support_noradrenaline_days
		self.inotropic_support_hydroocortisone_days = inotropic_support_hydroocortisone_days
		self.no_of_days_need_for_prostin = no_of_days_need_for_prostin
		self.no_of_hs_pda_medical_courses_paracetmol = no_of_hs_pda_medical_courses_paracetmol
		self.no_of_hs_pda_medical_courses_ibuprofin = no_of_hs_pda_medical_courses_ibuprofin
		self.no_hs_pda_surgical = no_hs_pda_surgical




@frappe.whitelist()
def create_cvs(baby_id,mother_name):
	cvs = frappe.new_doc('CVS')
	cvs.baby_id = baby_id
	cvs.mother_name = mother_name
	cvs.save()

@frappe.whitelist()
def delete_cvs(doc, method):
	cvs = frappe.get_doc('CVS', {'baby_id': doc.baby_id})
	cvs.delete()
	