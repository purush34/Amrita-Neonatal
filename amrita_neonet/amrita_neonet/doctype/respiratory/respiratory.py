# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Respiratory(Document):
	
	""" 
	Type 1 RDS
	Type II RDS
	ARDS
	VAP
	Congenital Pneumonia
	CPAM
	Congenital Diaphragmatic Hernia
	Eventeration
	Pulmonary Hypoplasia
	Delayed Perinatal Transition
	Transient Tachypnoea of Newborn
	Tracheo-Oesophageal Atresia
	Pneumothorax
	Pleural Effusion
	Chylothorax
	Sequestration
	Other 
	"""
	types = {
		'Type 1 RDS': 0,
		'Type II RDS': 0,
		'ARDS': 0,
		'VAP': 0,
		'Congenital Pneumonia': 0,
		'CPAM': 0,
		'Congenital Diaphragmatic Hernia': 0,
		'Eventeration': 0,
		'Pulmonary Hypoplasia': 0,
		'Delayed Perinatal Transition': 0,
		'Transient Tachypnoea of Newborn': 0,
		'Tracheo-Oesophageal Atresia': 0,
		'Pneumothorax': 0,
		'Pleural Effusion': 0,
		'Chylothorax': 0,
		'Sequestration': 0,
		'Other': 0
	}
	def before_save(self):
		days_of_simv = 0
		days_of_hfov = 0
		days_of_nasal_cannula = 0
		days_of_hhhfnc = 0
		days_of_bcpap = 0
		days_of_cpap = 0
		days_of_o2 = 0
		duration_of_nitric = 0
		types = {
			'Type 1 RDS': 0,
			'Type II RDS': 0,
			'ARDS': 0,
			'VAP': 0,
			'Congenital Pneumonia': 0,
			'CPAM': 0,
			'Congenital Diaphragmatic Hernia': 0,
			'Eventeration': 0,
			'Pulmonary Hypoplasia': 0,
			'Delayed Perinatal Transition': 0,
			'Transient Tachypnoea of Newborn': 0,
			'Tracheo-Oesophageal Atresia': 0,
			'Pneumothorax': 0,
			'Pleural Effusion': 0,
			'Chylothorax': 0,
			'Sequestration': 0,
			'Other': 0
		}
		for i in self.get_all_children():
			if i.ventilated == 'Yes':
				if i.simv_hfov == 'SIMV':
					days_of_simv += 1
				else:
					days_of_hfov += 1
			if i.nasal_cannula:
				days_of_nasal_cannula += 1
			if i.hhhfnc:
				days_of_hhhfnc += 1
			if i.bcpap:
				days_of_bcpap += 1
			if i.vent_cpap:
				days_of_cpap += 1
			if i.new_diag_dis == 'Yes':
				types[i.diag_dis.strip()] = 1
			if i.nitric_use_in_past_24_hours:
				duration_of_nitric += float(i.duration)
			if i.o2_24 == "Yes":
				days_of_o2 += 1
		
		self.simv_days = days_of_simv
		self.hfov_days = days_of_hfov
		self.nasal_days = days_of_nasal_cannula
		self.hhhfnc_days = days_of_hhhfnc
		self.bcpap_days = days_of_bcpap
		self.vent_days = days_of_cpap
		self.type_1_rds = types['Type 1 RDS']
		self.type_ii_rds = types['Type II RDS']
		self.ards = types['ARDS']
		self.vap = types['VAP']
		self.congenital_pneumonia = types['Congenital Pneumonia']
		self.cpam = types['CPAM']
		self.congenital_diaphragmatic_hernia = types['Congenital Diaphragmatic Hernia']
		self.eventeration = types['Eventeration']
		self.pulmonary_hypoplasia = types['Pulmonary Hypoplasia']
		self.delayed_perinatal_transition = types['Delayed Perinatal Transition']
		self.transient_tachypnoea_of_newborn = types['Transient Tachypnoea of Newborn']
		self.tracheo_oesophageal_atresia = types['Tracheo-Oesophageal Atresia']
		self.pneumothorax = types['Pneumothorax']
		self.pleural_effusion = types['Pleural Effusion']
		self.chylothorax = types['Chylothorax']
		self.sequestration = types['Sequestration']
		self.other = types['Other']
		self.n_hour = duration_of_nitric
		self.o2_days = days_of_o2

@frappe.whitelist()
def create_respiratory(baby_id,mother_name):
	respiratory = frappe.new_doc('Respiratory')
	respiratory.baby_id = baby_id
	respiratory.mother_name = mother_name
	respiratory.save()

@frappe.whitelist()
def delete_respiratory(doc, method):
	respiratory = frappe.get_doc('Respiratory', {'baby_id': doc.baby_id})
	respiratory.delete()
	