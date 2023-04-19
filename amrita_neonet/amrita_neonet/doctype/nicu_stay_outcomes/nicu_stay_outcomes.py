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
	
	htmlText = ""
	nextLine = "<br>"

	neurosonogram = frappe.get_doc('Neurosonogram', {'baby_id': baby_id})
	for child in neurosonogram.get_all_children():
		htmlText += str(child.date_done) + " Neurosonogram " + child.report + nextLine 
	# htmlText += nextLine

	ct = frappe.get_doc('CT', {'baby_id': baby_id})
	for child in ct.get_all_children():
		htmlText += str(child.date_done) + " CT " + child.report + nextLine
	# htmlText += nextLine

	mri = frappe.get_doc('MRI', {'baby_id': baby_id})
	for child in mri.get_all_children():
		htmlText += str(child.date_done) + " MRI " + child.report + nextLine
	# htmlText += nextLine

	electroencephalography = frappe.get_doc('Electroencephalography', {'baby_id': baby_id})
	for child in electroencephalography.get_all_children():
		htmlText += str(child.date_done) + " Electroencephalography " + child.report + nextLine
	# htmlText += nextLine

	uss_kub_abdomen = frappe.get_doc('USS KUB_Abdomen', {'baby_id': baby_id})
	for child in uss_kub_abdomen.get_all_children():
		htmlText += str(child.date_done) + " USS KUB_Abdomen " + child.report + nextLine
	# htmlText += nextLine

	blood_culture = frappe.get_doc('Blood culture', {'baby_id': baby_id})
	for child in blood_culture.get_all_children():
		htmlText += str(child.date_done) + " Blood culture " + child.report + nextLine
	# htmlText += nextLine

	urine_peritoneal_pleural_fluid = frappe.get_doc('Urine_Peritoneal_Pleural fluid', {'baby_id': baby_id})
	for child in urine_peritoneal_pleural_fluid.get_all_children():
		htmlText += str(child.date_done) + " Urine_Peritoneal_Pleural fluid " + child.report + nextLine
	# htmlText += nextLine

	echocardiography = frappe.get_doc('Echocardiography', {'baby_id': baby_id})
	for child in echocardiography.get_all_children():
		htmlText += str(child.date_done) + " Echocardiography " + child.report + nextLine
	# htmlText += nextLine

	lumbar_puncture = frappe.get_doc('Lumbar puncture', {'baby_id': baby_id})
	for child in lumbar_puncture.get_all_children():
		htmlText += str(child.date_done) + " Lumbar puncture " + child.report + nextLine
	# htmlText += nextLine

	neogen = frappe.get_doc('Neogen', {'baby_id': baby_id})
	for child in neogen.get_all_children():
		htmlText += str(child.date_done) + " Neogen " + child.report + nextLine
	# htmlText += nextLine

	genetic_tests = frappe.get_doc('Genetic Tests', {'baby_id': baby_id})
	for child in genetic_tests.get_all_children():
		htmlText += str(child.date_done) + " Genetic Tests " + child.report + nextLine
	# htmlText += nextLine

	pcr = frappe.get_doc('PCR', {'baby_id': baby_id})
	for child in pcr.get_all_children():
		htmlText += str(child.date_done) + " PCR " + child.report + nextLine
	# htmlText += nextLine

	swabs = frappe.get_doc('Swabs', {'baby_id': baby_id})
	for child in swabs.get_all_children():
		htmlText += str(child.date_done) + " Swabs " + child.report + nextLine
	# htmlText += nextLine

	respiratory_secreations = frappe.get_doc('Respiratory secreations', {'baby_id': baby_id})
	for child in respiratory_secreations.get_all_children():
		htmlText += str(child.date_done) + " Respiratory secreations " + child.report + nextLine
	# htmlText += nextLine

	retinopathy_of_prematurity = frappe.get_doc('Retinopathy of Prematurity', {'baby_id': baby_id})
	for child in retinopathy_of_prematurity.get_all_children():
		htmlText += str(child.date_done) + " Retinopathy of Prematurity " + child.report + nextLine
	# htmlText += nextLine
	# print(htmlText)
	if htmlText:
		return htmlText
	return "No Data"


@frappe.whitelist()
def getAllProcedures(baby_id):
	"""
	Umbilical lines
	PICC line
	Subclavian/ femoral line
	Pericardial tap
	Pleural tap
	Peritoneal tap
	Chest drain
	Peritoneal drain
	Surgical Operative Note
	Intubation
	Naso- Pharyngeal tube
	"""
	umbilical_lines = frappe.get_doc('Umbilical lines', {'baby_id': baby_id})
	picc_line = frappe.get_doc('PICC line', {'baby_id': baby_id})
	subclavian_femoral_line = frappe.get_doc('Subclavian/ femoral line', {'baby_id': baby_id})
	pericardial_tap = frappe.get_doc('Pericardial tap', {'baby_id': baby_id})
	pleural_tap = frappe.get_doc('Pleural tap', {'baby_id': baby_id})
	peritoneal_tap = frappe.get_doc('Peritoneal tap', {'baby_id': baby_id})
	chest_drain = frappe.get_doc('Chest drain', {'baby_id': baby_id})
	peritoneal_drain = frappe.get_doc('Peritoneal drain', {'baby_id': baby_id})
	surgical_operative_note = frappe.get_doc('Surgical Operative Note', {'baby_id': baby_id})
	intubation = frappe.get_doc('Intubation', {'baby_id': baby_id})
	naso_pharyngeal_tube = frappe.get_doc('Naso- Pharyngeal tube', {'baby_id': baby_id})

	htmlText = ""
	nextLine = "<br>"

	for child in umbilical_lines.get_all_children():
		if child.uac and child.uvc:
			htmlText += str(child.date_done) + " Umbilical lines " +  " UAC and UVC " + nextLine
		elif child.uac:
			htmlText += str(child.date_done) + " Umbilical lines " +  " UAC " + nextLine
		elif child.uvc:
			htmlText += str(child.date_done) + " Umbilical lines " +  " UVC " + nextLine
	
	for child in picc_line.get_all_children():
		htmlText += str(child.date_done) + " PICC line " + child.type + nextLine

	for child in subclavian_femoral_line.get_all_children():
		htmlText += str(child.date_done) + " Subclavian femoral line " + child.type + nextLine
	
	for child in pericardial_tap.get_all_children():
		htmlText += str(child.date_done) + " Pericardial tap " + child.nature_of_effusion + " " + child.done_by + nextLine
	
	for child in pleural_tap.get_all_children():
		htmlText += str(child.date_done) + " Pleural tap " + child.nature_of_effusion + " " + child.done_by + nextLine
	
	for child in peritoneal_tap.get_all_children():
		htmlText += str(child.date_done) + " Peritoneal tap " + child.nature_of_effusion + " " + child.done_by + nextLine
	
	for child in chest_drain.get_all_children():
		htmlText += str(child.date_done) + " Chest drain " + child.type + nextLine

	for child in peritoneal_drain.get_all_children():
		htmlText += str(child.date_done) + " Peritoneal drain " + child.nature_of_effusion + " " + child.done_by + nextLine

	for child in surgical_operative_note.get_all_children():
		htmlText += str(child.date_done) + " Surgical Operative Note " + child.operative_notes + nextLine
	
	for child in intubation.get_all_children():
		htmlText += str(child.date_done) + " Intubation " + child.type + nextLine

	for child in naso_pharyngeal_tube.get_all_children():
		htmlText += str(child.date_done) + " Naso Pharyngeal tube " + child.done_by + nextLine
	
	for child in naso_pharyngeal_tube.get_all_children():
		htmlText += str(child.date_done) + " Naso Pharyngeal tube " + child.done_by + nextLine
	
	if htmlText:
		return htmlText
	return "No Data"