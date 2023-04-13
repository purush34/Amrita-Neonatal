# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NICUStayOutcomes(Document):
	pass



""" 
Respiratory
CVS
Gastroinstestine
CNS
Endocrine and Metabolic 
Sepsis
Ophthalmology
ENT & Swallow
Haematology
Renal
Genetic 
"""

@frappe.whitelist()
def getRespiratoryDailySummery(baby_id):
	respiratory = frappe.get_doc('Respiratory', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in respiratory.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getCVSDailySummery(baby_id):
	cvs = frappe.get_doc('CVS', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in cvs.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getGastroinstestineDailySummery(baby_id):
	gastroinstestine = frappe.get_doc('Gastrointestinal', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in gastroinstestine.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getCNSDailySummery(baby_id):
	cns = frappe.get_doc('CNS', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in cns.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getEndocrineAndMetabolicDailySummery(baby_id):
	endocrine_and_metabolic = frappe.get_doc('Endocrine and metabolic', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in endocrine_and_metabolic.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getSepsisDailySummery(baby_id):
	sepsis = frappe.get_doc('Sepsis', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in sepsis.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getOphthalmologyDailySummery(baby_id):
	ophthalmology = frappe.get_doc('Opthalmology', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in ophthalmology.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getENTAndSwallowDailySummery(baby_id):
	ent_and_swallow = frappe.get_doc('ENT and Swallow', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in ent_and_swallow.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getHaematologyDailySummery(baby_id):
	haematology = frappe.get_doc('Haematology', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in haematology.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getRenalDailySummery(baby_id):
	renal = frappe.get_doc('Renal', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in renal.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getGeneticDailySummery(baby_id):
	genetic = frappe.get_doc('Genetic', {'baby_id': baby_id})
	htmlText = ""
	nextLine = "<br>"
	for child in genetic.get_all_children():
		if child.free_text_box_for_discharge_letter:
			htmlText += str(child.date) + nextLine + child.free_text_box_for_discharge_letter + nextLine + nextLine
	if htmlText:
		return htmlText
	return "No Data"

@frappe.whitelist()
def getAllDiagnosisSummery(baby_id):
	""" 
	Respiratory
	CVS
	Gastroinstestine
	CNS
	Endocrine and Metabolic 
	Sepsis
	Ophthalmology
	ENT & Swallow
	Haematology
	Renal
	Genetic 
	"""
	respiratory = frappe.get_doc('Respiratory', {'baby_id': baby_id})
	cvs = frappe.get_doc('CVS', {'baby_id': baby_id})
	gastroinstestine = frappe.get_doc('Gastroinstestine', {'baby_id': baby_id})
	cns = frappe.get_doc('CNS', {'baby_id': baby_id})
	endocrine_and_metabolic = frappe.get_doc('Endocrine and metabolic', {'baby_id': baby_id})
	sepsis = frappe.get_doc('Sepsis', {'baby_id': baby_id})
	ophthalmology = frappe.get_doc('Opthalmology', {'baby_id': baby_id})
	ent_and_swallow = frappe.get_doc('ENT and Swallow', {'baby_id': baby_id})
	haematology = frappe.get_doc('Haematology', {'baby_id': baby_id})
	renal = frappe.get_doc('Renal', {'baby_id': baby_id})
	genetic = frappe.get_doc('Genetic', {'baby_id': baby_id})
	
	htmlText = ""
	nextLine = "<br>"
	for child in respiratory.get_all_children():
		pass
	for child in cvs.get_all_children():
		pass
	for child in gastroinstestine.get_all_children():
		pass
	for child in cns.get_all_children():
		pass
	for child in endocrine_and_metabolic.get_all_children():
		pass
	for child in sepsis.get_all_children():
		pass
	for child in ophthalmology.get_all_children():
		pass
	for child in ent_and_swallow.get_all_children():
		pass
	for child in haematology.get_all_children():
		pass
	for child in renal.get_all_children():
		pass
	for child in genetic.get_all_children():
		pass
	if htmlText:
		return htmlText
	return "No Data"


@frappe.whitelist()
def getAllInvestigations(baby_id):
	"""
	Neurosonogram
	CT
	MRI
	Electroencephalography
	USS KUB/Abdomen
	Blood culture
	Urine/Peritoneal/ Pleural fluid
	Echocardiography
	Lumbar puncture
	Neogen
	Genetic
	PCR
	Swabs
	Respiratory secreations
	Retinopathy of Prematurity
	"""
	