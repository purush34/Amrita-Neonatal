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
    """
    "simv_days",
    "hfov_days",
    "nasal_days",
    "hhhfnc_days",
    "column_break_h5e9s",
    "bcpap_days",
    "vent_days",
    "o2_days",
    "n_hour",
    """
    htmlText += "SIMV Days: " + str(respiratory.simv_days) + nextLine
    htmlText += "HFOV Days: " + str(respiratory.hfov_days) + nextLine
    htmlText += "Nasal Cannula Days: " + str(respiratory.nasal_days) + nextLine
    htmlText += "HHHFNC Days: " + str(respiratory.hhhfnc_days) + nextLine
    htmlText += "BCPAP Days: " + str(respiratory.bcpap_days) + nextLine
    htmlText += "CPAP Days: " + str(respiratory.vent_days) + nextLine
    htmlText += "O2 Days: " + str(respiratory.o2_days) + nextLine
    htmlText += "Nitric Oxide Hours: " + str(respiratory.n_hour) + nextLine
    htmlText += nextLine + nextLine

    for child in respiratory.get_all_children():
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Respiratory daily summary")
    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getCVSDailySummery(baby_id):
    cvs = frappe.get_doc('CVS', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    """
    "inotropic_support_dopamime_days",
    "inotropic_support_dobutamine_days",
    "inotropic_support_adrenaline_days",
    "inotropic_support_noradrenaline_days",
    "inotropic_support_hydroocortisone_days",
    "column_break_vpzck",
    "no_of_days_need_for_prostin",
    "no_of_hs_pda_medical_courses_paracetmol",
    "no_of_hs_pda_medical_courses_ibuprofin",
    "no_hs_pda_surgical",
    """
    htmlText += "Dopamine Days: " + str(cvs.inotropic_support_dopamime_days) + nextLine
    htmlText += "Dobutamine Days: " + str(cvs.inotropic_support_dobutamine_days) + nextLine
    htmlText += "Adrenaline Days: " + str(cvs.inotropic_support_adrenaline_days) + nextLine
    htmlText += "Noradrenaline Days: " + str(cvs.inotropic_support_noradrenaline_days) + nextLine
    htmlText += "Hydrocortisone Days: " + str(cvs.inotropic_support_hydroocortisone_days) + nextLine
    htmlText += "Prostin Days: " + str(cvs.no_of_days_need_for_prostin) + nextLine
    htmlText += "Paracetmol Days: " + str(cvs.no_of_hs_pda_medical_courses_paracetmol) + nextLine
    htmlText += "Ibuprofin Days: " + str(cvs.no_of_hs_pda_medical_courses_ibuprofin) + nextLine
    htmlText += "Surgical Days: " + str(cvs.no_hs_pda_surgical) + nextLine
    htmlText += nextLine + nextLine


    for child in cvs.get_all_children():
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent CVS daily summary")
    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getGastroinstestineDailySummery(baby_id):
    gastroinstestine = frappe.get_doc('Gastrointestinal', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    """
    "total_no_of_tpn_days",
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
    htmlText += "Total TPN Days: " + str(gastroinstestine.total_no_of_tpn_days) + nextLine
    htmlText += "Full Feeds Days: " + str(gastroinstestine.day_to_reach_full_feeds) + nextLine
    htmlText += "Full Feeds Orally Days: " + str(gastroinstestine.day_to_reach_full_feeds_orally) + nextLine
    htmlText += "Average Kcalories: " + str(gastroinstestine.average_kcalories_per_day_during_stay) + nextLine
    htmlText += "Average GIR: " + str(gastroinstestine.average_gir_content_per_day_during_stay) + nextLine
    htmlText += "Average Protein: " + str(gastroinstestine.average_protein_content_per_day_during_stay) + nextLine
    htmlText += "Average Lipid: " + str(gastroinstestine.average_lipid_content_per_day_during_stay) + nextLine
    htmlText += "Maximum Bilirubin: " + str(gastroinstestine.maximum_bilirubin) + nextLine
    htmlText += "Phototherapy Days: " + str(gastroinstestine.total_no_of_days_of_phototherapy) + nextLine
    htmlText += nextLine + nextLine
    for child in gastroinstestine.get_all_children():
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Gastroinstestine daily summary")
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
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent CNS daily summary")
    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getEndocrineAndMetabolicDailySummery(baby_id):
    endocrine_and_metabolic = frappe.get_doc(
        'Endocrine and metabolic', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    for child in endocrine_and_metabolic.get_all_children():
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Endocrine and metabolic daily summary")
    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getSepsisDailySummery(baby_id):
    sepsis = frappe.get_doc('Sepsis', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    """
    "no_of_episodes_of_culture_postive_sepsis",
    "no_of_episodes_of_culture_negative_sepsis",
    "total_duration_of_iv_antibiotics_in_days",
    "column_break_x9iwe",
    "total_duration_of_reserve_antibiotics",
    "total_duration_of_antifungals",
    "no_of_central_lines_days"
    """
    htmlText += "No of episodes of culture positive sepsis: " + str(sepsis.no_of_episodes_of_culture_postive_sepsis) + nextLine
    htmlText += "No of episodes of culture negative sepsis: " + str(sepsis.no_of_episodes_of_culture_negative_sepsis) + nextLine
    htmlText += "Total duration of iv antibiotics: " + str(sepsis.total_duration_of_iv_antibiotics_in_days) + nextLine
    htmlText += "Total duration of reserve antibiotics: " + str(sepsis.total_duration_of_reserve_antibiotics) + nextLine
    htmlText += "Total duration of antifungals: " + str(sepsis.total_duration_of_antifungals) + nextLine
    htmlText += "No of central lines days: " + str(sepsis.no_of_central_lines_days) + nextLine

    sepsis_child = sepsis.get("daily_observations")
    antibiotics = sepsis.get("antibiotics_used")
    antifungals = sepsis.get("antifungals_used")
    htmlText += nextLine + nextLine
    center_lines = ""
    start_date = ""
    end_date = ""
    s = 0
    dd = 0
    for child in sepsis_child:
        if child.central_line_present=="Yes" and s == 0:
            start_date = child.date
            s = 1
        elif child.central_line_present=="No" and s == 1:
            end_date = frappe.utils.add_days(child.date, -1)
            center_lines += str(start_date) + " to " + str(end_date)+" (" + dd+ " days)" + nextLine
            s = 0
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
        dd = str(child.no_of_days_of_central_line_in_situ)
    if s == 1:
        center_lines += str(start_date) + " to continuing" + nextLine
    htmlText += nextLine 
    htmlText += "Central Lines: " + nextLine + center_lines + nextLine
    
    for child in antibiotics:
        htmlText += "Antibiotic Used: " + str(child.antibiotic_used) + ", "
        htmlText += "Type: " + str(child.type) + ", "
        htmlText += "Start Date: " + str(child.start_date) + ", "
        if not child.continuing:
            htmlText += "End Date: " + str(child.end_date) + ", "
        htmlText += "Number of Days: " + str(child.number_of_days) 
        htmlText += nextLine 
    htmlText += nextLine

    for child in antifungals:
        htmlText += "Antifungal Used: " + str(child.antibiotic_used) + ", "
        htmlText += "Type: " + str(child.type) + ", "
        htmlText += "Start Date: " + str(child.start_date) + ", "
        if not child.continuing:
            htmlText += "End Date: " + str(child.end_date) + ", "
        htmlText += "Number of Days: " + str(child.number_of_days) 
        htmlText += nextLine
    print("Sent Sepsis daily summary")
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
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Opthalmology daily summary")
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
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent ENT and Swallow daily summary")
    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getHaematologyDailySummery(baby_id):
    haematology = frappe.get_doc('Haematology', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    """
    "no_of_days_exchange_transfusion_past_24_hours",
    "no_of_days_prbc_past_24_hours",
    "no_of_days_platelets_past_24_hours",
    "no_of_days_ffp_past_24_hours",
    "column_break_bgeeo",
    "no_of_days_cryoprecipitate_past_24_hours",
    "no_of_days_ivig_past_24_hours",
    """
    htmlText += "No of days exchange transfusion past 24 hours: " + str(haematology.no_of_days_exchange_transfusion_past_24_hours) + nextLine
    htmlText += "No of days prbc past 24 hours: " + str(haematology.no_of_days_prbc_past_24_hours) + nextLine
    htmlText += "No of days platelets past 24 hours: " + str(haematology.no_of_days_platelets_past_24_hours) + nextLine
    htmlText += "No of days ffp past 24 hours: " + str(haematology.no_of_days_ffp_past_24_hours) + nextLine
    htmlText += "No of days cryoprecipitate past 24 hours: " + str(haematology.no_of_days_cryoprecipitate_past_24_hours) + nextLine
    htmlText += "No of days ivig past 24 hours: " + str(haematology.no_of_days_ivig_past_24_hours) + nextLine
    htmlText += nextLine + nextLine
    for child in haematology.get_all_children():
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Haematology daily summary")
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
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Renal daily summary")
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
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
    print("Sent Genetic daily summary")
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
    endocrine_and_metabolic = frappe.get_doc(
        'Endocrine and metabolic', {'baby_id': baby_id})
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
        htmlText += str(child.date_done) + " Neurosonogram " + \
            child.report + nextLine
    # htmlText += nextLine

    ct = frappe.get_doc('CT', {'baby_id': baby_id})
    for child in ct.get_all_children():
        htmlText += str(child.date_done) + " CT " + child.report + nextLine
    # htmlText += nextLine

    mri = frappe.get_doc('MRI', {'baby_id': baby_id})
    for child in mri.get_all_children():
        htmlText += str(child.date_done) + " MRI " + child.report + nextLine
    # htmlText += nextLine

    electroencephalography = frappe.get_doc(
        'Electroencephalography', {'baby_id': baby_id})
    for child in electroencephalography.get_all_children():
        htmlText += str(child.date_done) + \
            " Electroencephalography " + child.report + nextLine
    # htmlText += nextLine

    uss_kub_abdomen = frappe.get_doc('USS KUB_Abdomen', {'baby_id': baby_id})
    for child in uss_kub_abdomen.get_all_children():
        htmlText += str(child.date_done) + \
            " USS KUB_Abdomen " + child.report + nextLine
    # htmlText += nextLine

    blood_culture = frappe.get_doc('Blood culture', {'baby_id': baby_id})
    for child in blood_culture.get_all_children():
        htmlText += str(child.date_done) + " Blood culture " + \
            child.report + nextLine
    # htmlText += nextLine

    urine_peritoneal_pleural_fluid = frappe.get_doc(
        'Urine_Peritoneal_Pleural fluid', {'baby_id': baby_id})
    for child in urine_peritoneal_pleural_fluid.get_all_children():
        htmlText += str(child.date_done) + \
            " Urine_Peritoneal_Pleural fluid " + child.report + nextLine
    # htmlText += nextLine

    echocardiography = frappe.get_doc('Echocardiography', {'baby_id': baby_id})
    for child in echocardiography.get_all_children():
        htmlText += str(child.date_done) + \
            " Echocardiography " + child.report + nextLine
    # htmlText += nextLine

    lumbar_puncture = frappe.get_doc('Lumbar puncture', {'baby_id': baby_id})
    for child in lumbar_puncture.get_all_children():
        htmlText += str(child.date_done) + \
            " Lumbar puncture " + child.report + nextLine
    # htmlText += nextLine

    neogen = frappe.get_doc('Neogen', {'baby_id': baby_id})
    for child in neogen.get_all_children():
        htmlText += str(child.date_done) + " Neogen " + child.report + nextLine
    # htmlText += nextLine

    genetic_tests = frappe.get_doc('Genetic Tests', {'baby_id': baby_id})
    for child in genetic_tests.get_all_children():
        htmlText += str(child.date_done) + " Genetic Tests " + \
            child.report + nextLine
    # htmlText += nextLine

    pcr = frappe.get_doc('PCR', {'baby_id': baby_id})
    for child in pcr.get_all_children():
        htmlText += str(child.date_done) + " PCR " + child.report + nextLine
    # htmlText += nextLine

    swabs = frappe.get_doc('Swabs', {'baby_id': baby_id})
    for child in swabs.get_all_children():
        htmlText += str(child.date_done) + " Swabs " + child.report + nextLine
    # htmlText += nextLine

    respiratory_secreations = frappe.get_doc(
        'Respiratory secreations', {'baby_id': baby_id})
    for child in respiratory_secreations.get_all_children():
        htmlText += str(child.date_done) + \
            " Respiratory secreations " + child.report + nextLine
    # htmlText += nextLine

    retinopathy_of_prematurity = frappe.get_doc(
        'Retinopathy of Prematurity', {'baby_id': baby_id})
    for child in retinopathy_of_prematurity.get_all_children():
        htmlText += str(child.date_done) + \
            " Retinopathy of Prematurity " + child.report + nextLine
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
    umbilical_lines = frappe.get_doc('Umbiilical lines', {'baby_id': baby_id})
    picc_line = frappe.get_doc('PICC line', {'baby_id': baby_id})
    subclavian_femoral_line = frappe.get_doc(
        'Subclavian_femoral line', {'baby_id': baby_id})
    pericardial_tap = frappe.get_doc('Pericardial tap', {'baby_id': baby_id})
    pleural_tap = frappe.get_doc('Pleural tap', {'baby_id': baby_id})
    peritoneal_tap = frappe.get_doc('Peritoneal tap', {'baby_id': baby_id})
    chest_drain = frappe.get_doc('Chest drain', {'baby_id': baby_id})
    peritoneal_drain = frappe.get_doc('Peritoneal drain', {'baby_id': baby_id})
    surgical_operative_note = frappe.get_doc(
        'Surgical Operative Note', {'baby_id': baby_id})
    intubation = frappe.get_doc('Intubation', {'baby_id': baby_id})
    naso_pharyngeal_tube = frappe.get_doc(
        'Naso- Pharyngeal tube', {'baby_id': baby_id})

    htmlText = ""
    nextLine = "<br>"

    for child in umbilical_lines.get_all_children():
        if child.uac and child.uvc:
            htmlText += str(child.date_done) + \
                " Umbiilical lines " + " UAC and UVC " + nextLine
        elif child.uac:
            htmlText += str(child.date_done) + \
                " Umbiilical lines " + " UAC " + nextLine
        elif child.uvc:
            htmlText += str(child.date_done) + \
                " Umbiilical lines " + " UVC " + nextLine

    for child in picc_line.get_all_children():
        htmlText += str(child.date_done) + " PICC line " + \
            child.type + nextLine

    for child in subclavian_femoral_line.get_all_children():
        htmlText += str(child.date_done) + \
            " Subclavian femoral line " + child.type + nextLine

    for child in pericardial_tap.get_all_children():
        htmlText += str(child.date_done) + " Pericardial tap " + \
            child.nature_of_effusion + " " + child.done_by + nextLine

    for child in pleural_tap.get_all_children():
        htmlText += str(child.date_done) + " Pleural tap " + \
            child.nature_of_effusion + " " + child.done_by + nextLine

    for child in peritoneal_tap.get_all_children():
        htmlText += str(child.date_done) + " Peritoneal tap " + \
            child.nature_of_effusion + " " + child.done_by + nextLine

    for child in chest_drain.get_all_children():
        htmlText += str(child.date_done) + " Chest drain " + \
            child.side + child.size_of_drain + nextLine

    for child in peritoneal_drain.get_all_children():
        htmlText += str(child.date_done) + " Peritoneal drain " + \
            child.nature_of_effusion + " " + child.done_by + nextLine

    for child in surgical_operative_note.get_all_children():
        htmlText += str(child.date_done) + " Surgical Operative Note " + \
            child.operative_notes +  nextLine

    for child in intubation.get_all_children():
        htmlText += str(child.date_done) + " Intubation " + \
            child.size + " " + child.done_by + nextLine

    for child in naso_pharyngeal_tube.get_all_children():
        htmlText += str(child.date_done) + \
            " Naso Pharyngeal tube " + child.done_by + nextLine

    for child in naso_pharyngeal_tube.get_all_children():
        htmlText += str(child.date_done) + \
            " Naso Pharyngeal tube " + child.done_by + nextLine

    if htmlText:
        return htmlText
    return "No Data"


@frappe.whitelist()
def getAllDiagnosis(baby_id):
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
    # Respiratory
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
    respiratory = frappe.get_doc('Respiratory', {'baby_id': baby_id})
    htmlText = ""
    nextLine = "<br>"
    for child in respiratory.get_all_children():
        if child.new_diag_dis == "Yes":
            htmlText += str(child.date) + " Respiratory " + nextLine
            if child.diag_dis == "Type 1 RDS":
                htmlText += "Type 1 RDS" + nextLine
            elif child.diag_dis == "Type II RDS":
                htmlText += "Type II RDS" + nextLine
            elif child.diag_dis == "ARDS":
                htmlText += "ARDS" + nextLine
            elif child.diag_dis == "VAP":
                htmlText += "VAP " + child.diag_dis_text + nextLine
            elif child.diag_dis == "Congenital Pneumonia":
                htmlText += "Congenital Pneumonia" + nextLine
            elif child.diag_dis == "CPAM":
                htmlText += "CPAM " + child.diag_dis_text + nextLine
            elif child.diag_dis == "Congenital Diaphragmatic Hernia":
                htmlText += "Congenital Diaphragmatic Hernia " + child.cdh_dis + nextLine
            elif child.diag_dis == "Eventeration":
                htmlText += "Eventeration " + child.evnt_pnemo_pe_chylo_dis + nextLine
            elif child.diag_dis == "Pulmonary Hypoplasia":
                htmlText += "Pulmonary Hypoplasia " + nextLine
            elif child.diag_dis == "Delayed Perinatal Transition":
                htmlText += "Delayed Perinatal Transition " + nextLine
            elif child.diag_dis == "Transient Tachypnoea of Newborn":
                htmlText += "Transient Tachypnoea of Newborn " + nextLine
            elif child.diag_dis == "Tracheo-Oesophageal Atresia":
                htmlText += "Tracheo-Oesophageal Atresia " + child.toa_dis + nextLine
            elif child.diag_dis == "Pneumothorax":
                htmlText += "Pneumothorax " + child.evnt_pnemo_pe_chylo_dis + nextLine
            elif child.diag_dis == "Pleural Effusion":
                htmlText += "Pleural Effusion " + child.evnt_pnemo_pe_chylo_dis + nextLine
            elif child.diag_dis == "Chylothorax":
                htmlText += "Chylothorax " + child.evnt_pnemo_pe_chylo_dis + nextLine
            elif child.diag_dis == "Sequestration":
                htmlText += "Sequestration " + nextLine
            elif child.diag_dis == "Other":
                htmlText += "Other " + child.diag_dis_text + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # CVS
    """
	Cyanotic Congenital Heart Disease
	Acyanotci Heart Disease
	Hypotension
	Persistent Pulmonary Hpertension of Newborn
	Heart failure
	Hypertension
	Aberrant right sub-clavian artery
	Vascular ring
	Premature Atrial Contraction
	Premature Ventricular Contraction
	Tachy arrythmias
	Brady Arrythmias
	Other
	"""
    cvs = frappe.get_doc('CVS', {'baby_id': baby_id})
    for child in cvs.get_all_children():
        if child.discharge == "Yes":
            htmlText += str(child.date) + " CVS " + nextLine
            if child.discharge_diag == "Cyanotic Congenital Heart Disease":
                htmlText += "Cyanotic Congenital Heart Disease " + child.cchd_dis + nextLine
            elif child.discharge_diag == "Acyanotci Heart Disease":
                htmlText += "Acyanotci Heart Disease " + child.achd_dis + nextLine
            elif child.discharge_diag == "Hypotension":
                htmlText += "Hypotension " + nextLine
            elif child.discharge_diag == "Persistent Pulmonary Hpertension of Newborn":
                htmlText += "Persistent Pulmonary Hpertension of Newborn " + nextLine
            elif child.discharge_diag == "Heart failure":
                htmlText += "Heart failure " + nextLine
            elif child.discharge_diag == "Hypertension":
                htmlText += "Hypertension " + nextLine
            elif child.discharge_diag == "Aberrant right sub-clavian artery":
                htmlText += "Aberrant right sub-clavian artery " + nextLine
            elif child.discharge_diag == "Vascular ring":
                htmlText += "Vascular ring " + nextLine
            elif child.discharge_diag == "Premature Atrial Contraction":
                htmlText += "Premature Atrial Contraction " + nextLine
            elif child.discharge_diag == "Premature Ventricular Contraction":
                htmlText += "Premature Ventricular Contraction " + nextLine
            elif child.discharge_diag == "Tachy arrythmias":
                htmlText += "Tachy arrythmias " + child.tachy_brady_dis + nextLine
            elif child.discharge_diag == "Brady Arrythmias":
                htmlText += "Brady Arrythmias " + child.tachy_brady_dis + nextLine
            elif child.discharge_diag == "Other":
                htmlText += "Other " + child.tachy_brady_dis + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # Gastrointestinal
    """
	Feed Intolerance
	NEC- BELLS Staging
	Atresia
	Duplication cyst
	Perforation
	Biliary Atresia
	Meconium Ileus
	Malrotation
	Volvulus
	Anorectal malformation
	Disorders of sex Development
	Inguinal Hernia
	Hydrocoel
	Choledocal cyst
	Other
	"""
    gastrointestinal = frappe.get_doc('Gastrointestinal', {'baby_id': baby_id})

    for child in gastrointestinal.get_all_children():
        if child.new1 == "Yes":
            htmlText += str(child.date) + " Gastrointestinal " + nextLine
            if child.discharge == "Feed Intolerance":
                htmlText += "Feed Intolerance " + nextLine
            elif child.discharge == "NEC- BELLS Staging":
                htmlText += "NEC- BELLS Staging " + child.nec_bells_staging1 + nextLine
            elif child.discharge == "Atresia":
                htmlText += "Atresia " + child.atresia1 + nextLine
            elif child.discharge == "Duplication cyst":
                htmlText += "Duplication cyst " + child.text1 + nextLine
            elif child.discharge == "Perforation":
                htmlText += "Perforation " + child.text1 + nextLine
            elif child.discharge == "Biliary Atresia":
                htmlText += "Biliary Atresia " + nextLine
            elif child.discharge == "Meconium Ileus":
                htmlText += "Meconium Ileus " + nextLine
            elif child.discharge == "Malrotation":
                htmlText += "Malrotation " + nextLine
            elif child.discharge == "Volvulus":
                htmlText += "Volvulus " + nextLine
            elif child.discharge == "Anorectal malformation":
                htmlText += "Anorectal malformation " + nextLine
            elif child.discharge == "Disorders of sex Development":
                htmlText += "Disorders of sex Development" + nextLine
            elif child.discharge == "Inguinal Hernia":
                htmlText += "Inguinal Hernia " + nextLine
            elif child.discharge == "Hydrocoel":
                htmlText += "Hydrocoel " + nextLine
            elif child.discharge == "Choledocal cyst":
                htmlText += "Choledocal cyst " + nextLine
            elif child.discharge == "Other":
                htmlText += "Other " + child.other1 + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # CNS
    """
	Intraventricular Haemorrhage
	Post Haemorrhagic Ventricular Dilatation
	Hydrocephalous
	Periventricular Leucomalacia
	Absent Corpus Callosum
	Partial Agenisis of Corpus Callosum
	Arnold- Chiari Malformation
	Meningocoel
	Meningomyelocoel
	Hypoxic Ischaemic Encephalopathy
    History of Therapeutic cooling
	Seizures
	Other
	"""

    renal = frappe.get_doc('Renal', {'baby_id': baby_id})

    for child in renal.get_all_children():
        if child.diagnosis_discharge == "Yes":
            htmlText += str(child.date) + " Renal " + nextLine
            if child.if_diagdischarge == "Intraventricular Haemorrhage":
                htmlText += "Intraventricular Haemorrhage " + \
                    child.grade_dis + " " + child.ihd + nextLine
            elif child.if_diagdischarge == "Post Haemorrhagic Ventricular Dilatation":
                htmlText += "Post Haemorrhagic Ventricular Dilatation " + nextLine
            elif child.if_diagdischarge == "Hydrocephalous":
                htmlText += "Hydrocephalous " + child.hydro_dis + nextLine
            elif child.if_diagdischarge == "Periventricular Leucomalacia":
                htmlText += "Periventricular Leucomalacia " + nextLine
            elif child.if_diagdischarge == "Absent Corpus Callosum":
                htmlText += "Absent Corpus Callosum " + nextLine
            elif child.if_diagdischarge == "Partial Agenisis of Corpus Callosum":
                htmlText += "Partial Agenisis of Corpus Callosum " + nextLine
            elif child.if_diagdischarge == "Arnold- Chiari Malformation":
                htmlText += "Arnold- Chiari Malformation " + nextLine
            elif child.if_diagdischarge == "Meningocoel":
                htmlText += "Meningocoel " + nextLine
            elif child.if_diagdischarge == "Meningomyelocoel":
                htmlText += "Meningomyelocoel " + nextLine
            elif child.if_diagdischarge == "Hypoxic Ischaemic Encephalopathy":
                htmlText += "Hypoxic Ischaemic Encephalopathy " + \
                    "Grade " + child.grade_hie_dis + nextLine
            elif child.if_diagdischarge == "History of Therapeutic cooling":
                htmlText += "History of Therapeutic cooling " + nextLine
            elif child.if_diagdischarge == "Seizures":
                htmlText += "Seizures " + child.seiz_dis + nextLine
            elif child.if_diagdischarge == "Other":
                htmlText += "Other " + child.other_dis + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # Endocrine

    """
	Transient hypothyroidism
	Congenital hypothyroidism
	Congenital Hyperthyroidism
	Disorders of Protein metabolism
	Disorders of Fat metabolism
	Disorders of Carbohydrate metabolism
	Congenital Adrenal Hyperplasia
	Growth Harmone deficiency
	Transient Hyperinsulism
	Disorders of Sexual differentiation
	Hypoparathyroidism
	Hyperparathyroidism
	Adrenal Insufficiency
	Neonatal Diabetes Mellitus
	Diabetes Insipidus
	Cerebral Salt Wasting Syndrome
	Other
	"""

    endocrine = frappe.get_doc('Endocrine and metabolic', {'baby_id': baby_id})

    for child in endocrine.get_all_children():
        if child.new_diagnosis_for_discharge == "Yes":
            htmlText += str(child.date) + " Endocrine " + nextLine
            if child.discharge_diagnosis == "Transient hypothyroidism":
                htmlText += "Transient hypothyroidism " + nextLine
            elif child.discharge_diagnosis == "Congenital hypothyroidism":
                htmlText += "Congenital hypothyroidism " + nextLine
            elif child.discharge_diagnosis == "Congenital Hyperthyroidism":
                htmlText += "Congenital Hyperthyroidism " + nextLine
            elif child.discharge_diagnosis == "Disorders of Protein metabolism":
                htmlText += "Disorders of Protein metabolism " + \
                    child.diagnosis_for_discharge_text + nextLine
            elif child.discharge_diagnosis == "Disorders of Fat metabolism":
                htmlText += "Disorders of Fat metabolism " + \
                    child.diagnosis_for_discharge_text + nextLine
            elif child.discharge_diagnosis == "Disorders of Carbohydrate metabolism":
                htmlText += "Disorders of Carbohydrate metabolism " + \
                    child.diagnosis_for_discharge_text + nextLine
            elif child.discharge_diagnosis == "Congenital Adrenal Hyperplasia":
                htmlText += "Congenital Adrenal Hyperplasia " + nextLine
            elif child.discharge_diagnosis == "Growth Harmone deficiency":
                htmlText += "Growth Harmone deficiency " + nextLine
            elif child.discharge_diagnosis == "Other":
                htmlText += "Other " + child.diagnosis_for_discharge_text + nextLine
            else:
                htmlText += child.diagnosis_for_discharge_text + nextLine
    htmlText += nextLine
    htmlText += nextLine

    # Sepsis
    """
    Suspected sepsis
        Culture Postive sepsis
        Culture Negative sepsis
        Ventilator associated pneumonia
        Meningitis
        Candida Sepsis
        Other
    """

    sepsis = frappe.get_doc('Sepsis', {'baby_id': baby_id})

    for child in sepsis.get("daily_observations"):
        if child.if_diag_dis == "Yes":
            htmlText += str(child.date) + " Sepsis " + nextLine
            if child.diagnosis == "Suspected sepsis":
                htmlText += "Suspected sepsis " + nextLine
            elif child.diagnosis == "Culture Postive sepsis":
                htmlText += "Culture Postive sepsis " + "Blood Culture " + \
                    child.blood_dis + "Urine Culture " + child.urine_dis + nextLine
            elif child.diagnosis == "Culture Negative sepsis":
                htmlText += "Culture Negative sepsis " + nextLine
            elif child.diagnosis == "Ventilator associated pneumonia":
                htmlText += "Ventilator associated pneumonia " + child.bacteria_dis + nextLine
            elif child.diagnosis == "Meningitis":
                htmlText += "Meningitis " + child.bacteria_dis + nextLine
            elif child.diagnosis == "Candida Sepsis":
                htmlText += "Candida Sepsis " + "Blood Culture " + child.blood_dis + \
                    "Urine Culture " + child.urine_dis + \
                    "Meningitis " + child.meningitis_dis + nextLine
            elif child.diagnosis == "Other":
                htmlText += "Other " + child.other_dis + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # Ophthalmology

    opthal = frappe.get_doc('Opthalmology', {'baby_id': baby_id})

    for child in opthal.get_all_children():
        if child.new_diagnosis_for_discharge == "Yes":
            htmlText += str(child.date) + " Opthalmology " + nextLine
            htmlText += child.discharge_diagnosis + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # ENT

    ent = frappe.get_doc('ENT and Swallow', {'baby_id': baby_id})

    for child in ent.get_all_children():
        if child.diagnosis_discharge == "Yes":
            htmlText += str(child.date) + " ENT and Swallow " + nextLine
            if child.if_diagdischarge == "Chonal Atresia":
                htmlText += "Chonal Atresia " + child.chonal_atresia_dis + \
                    " " + child.text_diagdischarge + nextLine
            else:
                htmlText += child.if_diagdischarge + " " + child.text_diagdischarge + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # Haematology

    haematology = frappe.get_doc('Haematology', {'baby_id': baby_id})
    """
    Anemia of prematurity
    Thrombocytopaenia
    Coagulopathy
    Post Surgical Anemia
    Heriditary Spherocytosis
    Haemolytic
    """
    for child in haematology.get_all_children():
        if child.diag_discharge == "Yes":
            htmlText += str(child.date) + " Haematology " + nextLine
            if child.if_diag_discharge == "Anemia of prematurity":
                htmlText += "Anemia of prematurity " + nextLine
            elif child.if_diag_discharge == "Thrombocytopaenia":
                htmlText += "Thrombocytopaenia " + child.thrombocytopaenia_dis + nextLine
            elif child.if_diag_discharge == "Coagulopathy":
                htmlText += "Coagulopathy " + child.coagulopathy_dis + nextLine
            elif child.if_diag_discharge == "Post Surgical Anemia":
                htmlText += "Post Surgical Anemia " + nextLine
            elif child.if_diag_discharge == "Heriditary Spherocytosis":
                htmlText += "Heriditary Spherocytosis " + nextLine
            elif child.if_diag_discharge == "Haemolytic":
                htmlText += "Haemolytic " + child.haemolytic_dis + nextLine

    htmlText += nextLine
    htmlText += nextLine

    # Renal

    renal = frappe.get_doc('Renal', {'baby_id': baby_id})
    """
    Renal Pelvic dilatation
    Multicystic Dysplastic Kidney
    Fungal Ball
    Pelvi-Ureter Junction obstruction
    Posterior Uretheral Valve
    Acute Kidney Injury
    Acute Renal Failure
    Chronic Renal Failure
    Other
    """
    for child in renal.get_all_children():
        if child.diagnosis_discharge == "Yes":
            htmlText += str(child.date) + " Renal " + nextLine
            if child.if_diagdischarge == "Renal Pelvic dilatation":
                htmlText += "Renal Pelvic dilatation " + child.chonal_atresia_dis + \
                    " " + child.text_diagdischarge + nextLine
            elif child.if_diagdischarge == "Multicystic Dysplastic Kidney":
                htmlText += "Multicystic Dysplastic Kidney " + \
                    child.chonal_atresia_dis + " " + child.text_diagdischarge + nextLine
            elif child.if_diagdischarge == "Fungal Ball":
                htmlText += "Fungal Ball " + child.chonal_atresia_dis + \
                    " " + child.text_diagdischarge + nextLine
            elif child.if_diagdischarge == "Pelvi-Ureter Junction obstruction":
                htmlText += "Pelvi-Ureter Junction obstruction " + \
                    child.chonal_atresia_dis + " " + child.text_diagdischarge + nextLine
            else:
                htmlText += child.if_diagdischarge + " " + child.text_diagdischarge + nextLine

    htmlText += nextLine
    htmlText += nextLine

    return htmlText
