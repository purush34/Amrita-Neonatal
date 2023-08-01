# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe,json
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
    htmlText += nextLine 
    s = 0
    center_lines = ""
    start_date = ""
    end_date = ""
    dd = 0
    for child in gastroinstestine.get_all_children():
        if child.central_line_present == "Yes" and s == 0:
            start_date = child.date
            s = 1
        elif child.central_line_present == "No" and s == 1:
            end_date = frappe.utils.add_days(child.date, -1)
            center_lines += str(start_date) + " to " + str(end_date)+" (" + str(dd) + " days)" + nextLine
            s = 0
        if child.free_text_box_for_discharge_letter:
            htmlText += str(child.date) + nextLine + \
                child.free_text_box_for_discharge_letter + nextLine + nextLine
        dd = str(child.no_of_days_of_central_line_in_situ)
    if s == 1:
        center_lines += str(start_date) + " to continuing" + nextLine
    htmlText += nextLine
    htmlText += "Central Lines: " + nextLine + center_lines + nextLine
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
            if child.discharge == "Yes":
                if child.discharge_diag == "Cyanotic Congenital Heart Disease":
                    htmlText += "Cyanotic Congenital Heart Disease " + child.cchd_dis + nextLine
                elif child.discharge_diag == "Acyanotci Heart Disease":
                    htmlText += "Acyanotci Heart Disease " + child.ahd_dis + nextLine
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
                htmlText += "Other " + child.text1 + nextLine

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


"""
name,owner,creation,modified,modified_by,docstatus,idx,mother_mrd,mother_name,antenantal_follow_up,1st_visit_to_aims,conception,icsi_iui,donors,number_of_babies,twins,triplets,others,lmp,edd_by_dates,blood_group,vdrl,hepatitis_b,hepatitis_c,any_antibodies,torch,hiv,mmr_vaccination,tt,covid_immunisations,one_dose,two_dose,booster,date_of_first_dose,year_of_2nd_dose,year_of_booster,scans,an_dos,an_ga,an_dopplers,d_n,d_a,an_findings,gs_dos,gs_ga,gs_doplers,gs_n,gs_a,gs_findings,efw_growth,by_scan,by_dates,pih,explain_pih,gdm,diet,oha,insulin,hypothyroidism,reason,select_type,antibodies,medication,hyperthyroidism,last_text,doctype,number_of_additional_scans,pre_term_labour,rupture_of_membranes,prolonged_rupture_of_membranes,date_and_time,duration_of_prom,steroids,steroids_no,if_steriods,first_dose,first_date,second_dose,second_date,no_of_courses_of_steroids,number_of_courses,gestation_age_at_which_given,use_of_magnesium_sulphate,no_magnesium_sulphate,meconium_staining_of_liquor,meconium_yes,prom,maternal_pyrexia,uti,uti_text,hvs_positive,hvs_text,prolonged_stay,foul_smelling_liquor,leaking_per_vagina,date_time_leaking,peripartum_name,peripartum_date,last_dose_given,onset_of_labour,medication_used,mode_of_delivery,if_vaginal,if_instrumentation,if_forceps,if_electivelscs,if_maternal_health,if_emlscs,if_maternal,if_fetal,if_fetal_distress,if_suboptimal,if_dopplers_concerns,if_umbilical_artery,if_umbilical_vein,anaesthesia,cried_soon_after_birth,need_for_resuscitation,stimulation,bag_and_mask,noc,intubation,age_in_min,size,fixed_at,c_comp,started_at_age_in_min,no_of_cycles,adrenaline_doses,et_1,iv,sb_1,hr_1,c_1,t_1,r_1,total_1,sb_5,hr_5,c_5,t_5,r_5,total_5,sb_10,hr_10,c_10,t_10,r_10,total_10,sb_15,hr_15,c_15,t_15,r_15,total_15,sb_20,hr_20,c_20,t_20,r_20,total_20,passive_cooling,age_in_minutes,cord_blood_gas,resuscitation
"""

@frappe.whitelist()
def getAntenatalHistory(baby_id):
    """
    Antenatal History
    """
    opening_page = frappe.get_doc("Opening page", {'baby_id':baby_id})
    mother_mrd = opening_page.mother_mrd
    antenatal_history = frappe.get_doc('Antenatal-1', {'mother_mrd': mother_mrd})
    antenatal_history2 = frappe.get_doc(
        'Antenatal-2', {'mother_mrd': mother_mrd})
    dict1 = antenatal_history.as_dict()
    dict2 = antenatal_history2.as_dict()
    final_dict = {**dict1, **dict2}
    for i,j in final_dict.items():
        final_dict[i] = str(j)
    final_json = json.dumps(final_dict, default=str)
    htmlText = ''
    table = '<table>'
    tableEnd = '</table>'
    row = '<tr>'
    rowEnd = '</tr>'
    col = '<td>'
    colEnd = '</td>'
    linebreak = '<br>'

    htmlText += "Antenatal 1 Follow up :" + final_dict["antenantal_follow_up"] + linebreak
    htmlText += "First Visit to AIMS :" + str(final_dict["1st_visit_to_aims"]) + linebreak
    if final_dict["conception"]=="IVF":
        htmlText += "Conception :" + final_dict["conception"] + "<br>" + final_dict["icsi_iui"] + " " + final_dict["donors"] + linebreak
    else:
        htmlText += "Conception :" + final_dict["conception"] + linebreak
    htmlText += "Number of Babies :" + final_dict["number_of_babies"] + linebreak
    htmlText += "LMP :" + str(final_dict["lmp"]) + linebreak
    htmlText += "EDD by Dates :" + str(final_dict["edd_by_dates"]) + linebreak

    htmlText += "Blood Group :" + final_dict["blood_group"] + linebreak
    htmlText += "VDRL :" + str(final_dict["vdrl"]) + linebreak
    htmlText += "Hepatitis B :" + str(final_dict["hepatitis_b"]) + linebreak
    htmlText += "Hepatitis C :" + str(final_dict["hepatitis_c"]) + linebreak
    if final_dict["any_antibodies"]:htmlText += "Any Antibodies :" + final_dict["any_antibodies"] + linebreak
    if final_dict["torch"] :htmlText += "TORCH :" + final_dict["torch"] + linebreak
    if final_dict["hiv"]: htmlText += "HIV :" + final_dict["hiv"] + linebreak
    if final_dict["mmr_vaccination"]:htmlText += "MMR Vaccination :" + final_dict["mmr_vaccination"] + linebreak
    if final_dict["tt"]:htmlText += "TT :" + final_dict["tt"] + linebreak
    if final_dict["covid_immunisations"]=="Yes":
        htmlText += "Covid Immunisations :" + final_dict["covid_immunisations"] +linebreak
        if final_dict["one_dose"]=="Yes":
            htmlText +=  final_dict["one_dose"] + ":" + str(final_dict["date_of_first_dose"])+linebreak
        if final_dict["two_dose"]=="Yes":
            htmlText +=  final_dict["two_dose"] + ":" + str(final_dict["year_of_2nd_dose"])+linebreak
        if final_dict["booster"]=="Yes":
            htmlText +=  final_dict["booster"] + ":" + str(final_dict["year_of_booster"])+linebreak
    else:
        htmlText += "Covid Immunisations :" + final_dict["covid_immunisations"] +linebreak
    
    htmlText += "Scans :" + final_dict["scans"] + linebreak
    if final_dict['scans']=="Yes":
        # htmlText += "Dating Scan :" + str(final_dict["d_dos"]) + linebreak
        # htmlText += "GA :" + final_dict["d_ga"] + linebreak
        # htmlText += "Findings :" + final_dict["d_findings"] + linebreak
        htmlText += "Anaomaly Scan :" + str(final_dict["an_dos"]) + linebreak
        htmlText += "GA :" + final_dict["an_ga"] + linebreak
        if final_dict["an_findings"]:htmlText += "Findings :" + final_dict["an_findings"] + linebreak
        htmlText += "Growth Scan :" + str(final_dict["gs_dos"]) + linebreak
        htmlText += "GA :" + final_dict["gs_ga"] + linebreak
        if final_dict["gs_doplers"]=="Normal":
            htmlText += "Dopplers :" + final_dict["gs_doplers"] + linebreak
            htmlText += "Dopplers type:" + final_dict["gs_n"] + linebreak
        else:
            htmlText += "Dopplers :" + final_dict["gs_doplers"] + linebreak
            htmlText += "Dopplers type:" + final_dict["gs_a"] + linebreak
        htmlText += "Findings :" + final_dict["gs_findings"] + linebreak
        htmlText += "EFW :" + final_dict["efw_growth"] + linebreak
        # for i in antenatal_history.get_all_children():

        #     if i.doctype=="Additional Scans":
        #         htmlText += "Additional Scans :" + str(i.dos) + linebreak
        #         htmlText += "GA :" + i.ga + linebreak
        #         htmlText += "Findings :" + i.findings + linebreak
    elif final_dict['scans']=="No":
        htmlText += "Findings :" + final_dict["an_findings"] + linebreak    
    htmlText += "EDD : By Scan:" + str(final_dict["by_scan"]) + linebreak
    htmlText += "EDD : By Dates:" + str(final_dict["by_dates"]) + linebreak

    htmlText += "History Of:" + linebreak
    if final_dict["pih"]=="Yes":
        htmlText += "PIH :" + final_dict["pih"] + linebreak
        htmlText += "Details of PIH :" + final_dict["explain_pih"] + linebreak
    else:
        htmlText += "PIH :" + final_dict["pih"] + linebreak
    if final_dict["gdm"]=="Yes":
        ##doubt : how to show checkbox data
        htmlText += "GDM :" + final_dict["gdm"] + linebreak
        if final_dict["diet"]==True:            
            htmlText += "Diet :" + final_dict["diet"] + linebreak
        if final_dict["oha"]==True:
            htmlText += "OHA :" + final_dict["oha"] + linebreak
        if final_dict["insulin"]==True:
            htmlText += "Insulin :" + final_dict["insulin"] + linebreak
    else:
        htmlText += "GDM :" + final_dict["gdm"] + linebreak
    if final_dict["hypothyroidism"]=="Yes":
        htmlText += "Hypothyroidism :" + final_dict["hypothyroidism"] + linebreak
        if final_dict["select_type"]=="Pre- pregnancy":
            htmlText += "Pre- pregnancy :" + final_dict["medication"] + linebreak
        elif final_dict["select_type"]=="Gestation":
            htmlText += "Gestation :" + final_dict["medication"] + linebreak
        elif final_dict["select_type"]=="Post- Thyroidectomy":
            htmlText += "Post- Thyroidectomy :" + linebreak
            htmlText += "Reason :" + final_dict["reason"] + linebreak
            htmlText += "Anti-bodies :" + final_dict["antibodies"] + linebreak
            htmlText += "Medication :" + final_dict["medication"] + linebreak
    else:
        htmlText += "Hypothyroidism :" + final_dict["hypothyroidism"] + linebreak
    htmlText += "Hyperthyroidism :" + final_dict["hyperthyroidism"] + linebreak
    htmlText += final_dict["last_text"] + linebreak

    htmlText += "Antenatal 2 Follow up :" + final_dict["doctype"] + linebreak
    htmlText +="Pre Term Labour :" + final_dict["pre_term_labour"] + linebreak
    htmlText +="Rupture of Membranes :" + final_dict["rupture_of_membranes"] + linebreak
    if final_dict["prolonged_rupture_of_membranes"]=="Yes":
        htmlText += "Prolonged Rupture of Membranes :" + final_dict["prolonged_rupture_of_membranes"] + linebreak
        htmlText += "Date and Time :" + str(final_dict["date_and_time"]) + linebreak
        htmlText += "Duration of PROM :" + final_dict["duration_of_prom"] + linebreak
        htmlText += "Duration in days :" + final_dict["duration_in_days"] + linebreak
    else:
        htmlText += "Prolonged Rupture of Membranes :" + final_dict["prolonged_rupture_of_membranes"] + linebreak
    if final_dict["steroids"]=="Yes":
        htmlText += "Steroids :" + final_dict["steroids"] + linebreak
        htmlText += "Type : " + final_dict["if_steriods"] + linebreak
        if final_dict["first_dose"]:
            htmlText += "First Dose :" + str(final_dict["first_date"]) + linebreak
        if final_dict["second_dose"]:
            htmlText += "Second Dose :" + str(final_dict["second_date"]) + linebreak
        if final_dict["no_of_courses_of_steroids"]=="Multiple":
            htmlText += "Number of Corses :" + final_dict["no_of_courses_of_steroids"] + linebreak
            htmlText += "Number of Courses :" + final_dict["number_of_courses"] + linebreak
            htmlText += "Gestation Age at which given :" + final_dict["gestation_age_at_which_given"] + linebreak
        elif final_dict["no_of_courses_of_steroids"]=="Single":
            htmlText += "Number of Corses :" + final_dict["no_of_courses_of_steroids"] + linebreak
    else:
        htmlText += "Steroids :" + final_dict["steroids"] + linebreak
        htmlText += "Type : " + final_dict["if_steriods"] + linebreak


    htmlText += "Use of Magnesium Sulphate :" + final_dict["use_of_magnesium_sulphate"] + linebreak
    if final_dict["use_of_magnesium_sulphate"]=="No":
        htmlText += "Reason :" + final_dict["no_magnesium_sulphate"] + linebreak
    if final_dict["meconium_staining_of_liquor"]=="Yes":
        htmlText += "Meconium Staining of Liquor :" + final_dict["meconium_staining_of_liquor"] + linebreak
        htmlText += "Meconium :" + final_dict["meconium_yes"] + linebreak
    else:
        htmlText += "Meconium Staining of Liquor :" + final_dict["meconium_staining_of_liquor"] + linebreak
    
    htmlText += "PROM :" + final_dict["prom"] + linebreak
    htmlText += "Maternal Pyrexia :" + final_dict["maternal_pyrexia"] + linebreak
    htmlText += "Prolonged Stay :" + final_dict["prolonged_stay"] + linebreak
    htmlText += "Foul Smelling Liquor :" + final_dict["foul_smelling_liquor"] + linebreak
    htmlText += linebreak
    htmlText += "UTI :" + final_dict["uti"] + linebreak
    if final_dict["uti"]:
        htmlText += "UTI :" + final_dict["uti_text"] + linebreak
    htmlText += "HVS :" + final_dict["hvs_positive"] + linebreak
    if final_dict["hvs_positive"]:
        htmlText += "HVS :" + final_dict["hvs_text"] + linebreak
    htmlText += "Leaking per vagina :" + final_dict["leaking_per_vagina"] + linebreak
    if final_dict["leaking_per_vagina"]:
        htmlText += "Date and Time of leaking " + final_dict["date_time_leaking"]

    htmlText += linebreak
    htmlText += "Peripartum name: " + final_dict["peripartum_name"]+ linebreak
    htmlText += "Peripartum date: " + final_dict["peripartum_date"] + linebreak
    htmlText += "Last Dose given: "+ final_dict["last_dose_given"] + linebreak
    htmlText += "Onset of labour: " + final_dict["onset_of_labour"] + linebreak
    """
    onset_of_labour,medication_used,mode_of_delivery,if_vaginal,if_instrumentation,if_forceps,if_electivelscs,if_maternal_health,if_emlscs,if_maternal,if_fetal,if_fetal_distress,if_suboptimal,if_dopplers_concerns,if_umbilical_artery,if_umbilical_vein,anaesthesia,cried_soon_after_birth,need_for_resuscitation,stimulation,bag_and_mask,noc,intubation,age_in_min,size,fixed_at,c_comp,started_at_age_in_min,no_of_cycles,adrenaline_doses,et_1,iv,sb_1,hr_1,c_1,t_1,r_1,total_1,sb_5,hr_5,c_5,t_5,r_5,total_5,sb_10,hr_10,c_10,t_10,r_10,total_10,sb_15,hr_15,c_15,t_15,r_15,total_15,sb_20,hr_20,c_20,t_20,r_20,total_20,passive_cooling,age_in_minutes,cord_blood_gas,resuscitation
    """
    if final_dict["mode_of_delivery"] == "Vaginal":
        htmlText += "Mode of Delivery :" + final_dict["mode_of_delivery"] + linebreak
        htmlText += "If Vaginal :" + final_dict["if_vaginal"] + linebreak
        if final_dict["if_vaginal"] == "Instrumentation":
            htmlText += "If Instrumentation :" + final_dict["if_instrumentation"] + linebreak
            if final_dict["if_instrumentation"] == "Forceps":
                htmlText += "If Forceps :" + final_dict["if_forceps"] + linebreak
        else:
            htmlText += "Vaginal :" + final_dict["if_vaginal"] + linebreak
        
    elif final_dict["mode_of_delivery"] == "Elective LSCS":
        htmlText += "Mode of Delivery :" + final_dict["mode_of_delivery"] + linebreak
        htmlText += "If Elective LSCS :" + final_dict["if_electivelscs"] + linebreak
        if final_dict["if_electivelscs"] == "Previous Section" or final_dict["if_electivelscs"] == "Patient Request":
            htmlText += "If Maternal :" + final_dict["if_maternal"] + linebreak
        elif final_dict["if_electivelscs"]=="Maternal Health":
            htmlText += "If Maternal Health :" + final_dict["if_maternal_health"] + linebreak
        elif final_dict["if_electivelscs"]=="Fetal":
            htmlText += "If Fetal Distress :" + final_dict["text_fetal"] + linebreak
        
    elif final_dict["mode_of_delivery"] == "Em LSCS":
        htmlText += "Mode of Delivery :" + final_dict["mode_of_delivery"] + linebreak
        if final_dict["if_emlscs"] == "Maternal":
            htmlText += "If Maternal :" + final_dict["if_maternal"] + linebreak
        elif final_dict["if_emlscs"] == "Fetal":
            htmlText += "Fetal  :" + final_dict["if_fetal"] + linebreak
            if final_dict["if_fetal"]=="Fetal Distress":
                htmlText += "If Fetal Distress :" + final_dict["if_fetal_distress"] + linebreak
            elif final_dict["if_fetal"]=="Sub-optimal CTG":
                htmlText += "If Sub-optimal CTG :" + final_dict["if_suboptimal"] + linebreak
            elif final_dict["if_fetal"]=="Dopplers Concerns":
                htmlText += "If Dopplers Concerns :" + final_dict["if_dopplers_concerns"] + linebreak
        else:
            htmlText += "If Maternal :" + final_dict["if_emlscs"] + linebreak
            htmlText += "Both :" + final_dict["text_f_m"] + linebreak
    htmlText += "Anaesthesia :" + final_dict["anaesthesia"] + linebreak

    htmlText += "Cried soon after birth :" + final_dict["cried_soon_after_birth"] + linebreak
    htmlText += "Need for Resuscitation :" + final_dict["need_for_resuscitation"] + linebreak
    if final_dict["need_for_resuscitation"]=="Yes":
        htmlText += "Stimulation :" + final_dict["stimulation"] + linebreak
        htmlText += "Bag and Mask :" + final_dict["bag_and_mask"] + linebreak
        if final_dict["bag_and_mask"]=="Yes":
            htmlText += "NOC :" + final_dict["noc"] + linebreak
        htmlText += "Intubation :" + final_dict["intubation"] + linebreak
        if final_dict["intubation"]=="Yes":
            htmlText += "Age in min :" + final_dict["age_in_min"] + " " + "Size :" + final_dict["size"] + " " + "Fixed at :" + final_dict["fixed_at"] + linebreak
        
        htmlText += "C-Comp :" + final_dict["c_comp"] + linebreak
        if final_dict["c_comp"]=="Yes":
            htmlText += "Started at age in min :" + final_dict["started_at_age_in_min"] + " " + "No of cycles :" + final_dict["no_of_cycles"] + linebreak
            htmlText += "Adrenaline Doses :" + final_dict["adrenaline_doses"] + linebreak
            if final_dict["adrenaline_doses"]=="Yes":
                htmlText += "ET 1 :" + final_dict["et_1"] + " " + "IV :" + final_dict["iv"] + linebreak
    
    colHead = '<td>'
    colHeadEnd = '</td>'

    htmlText += table

    htmlText += row
    htmlText += colHead + "Title" + colHeadEnd
    htmlText += colHead + "Age in 1 min" + colHeadEnd
    htmlText += colHead + "Age in 5 min" + colHeadEnd
    htmlText += colHead + "Age in 10 min" + colHeadEnd
    htmlText += colHead + "Age in 15 min" + colHeadEnd
    htmlText += colHead + "Age in 20 min" + colHeadEnd
    htmlText += rowEnd

    htmlText += row
    
    htmlText += col + "Spontaneous breathing" + colEnd
    htmlText += col + final_dict["sb_1"] + colEnd
    htmlText += col + final_dict["sb_5"] + colEnd
    htmlText += col + final_dict["sb_10"] + colEnd
    htmlText += col + final_dict["sb_15"] + colEnd
    htmlText += col + final_dict["sb_20"] + colEnd
    htmlText += rowEnd

    htmlText += row
    htmlText += col + "Heart Rate" + colEnd
    htmlText += col + final_dict["hr_1"] + colEnd
    htmlText += col + final_dict["hr_5"] + colEnd
    htmlText += col + final_dict["hr_10"] + colEnd
    htmlText += col + final_dict["hr_15"] + colEnd
    htmlText += col + final_dict["hr_20"] + colEnd
    htmlText += rowEnd

    htmlText += row
    htmlText += col + "Colour" + colEnd
    htmlText += col + final_dict["c_1"] + colEnd
    htmlText += col + final_dict["c_5"] + colEnd
    htmlText += col + final_dict["c_10"] + colEnd
    htmlText += col + final_dict["c_15"] + colEnd
    htmlText += col + final_dict["c_20"] + colEnd
    htmlText += rowEnd

    htmlText += row
    htmlText += col + "Tone" + colEnd
    htmlText += col + final_dict["t_1"] + colEnd
    htmlText += col + final_dict["t_5"] + colEnd
    htmlText += col + final_dict["t_10"] + colEnd
    htmlText += col + final_dict["t_15"] + colEnd
    htmlText += col + final_dict["t_20"] + colEnd
    htmlText += rowEnd

    htmlText += row
    htmlText += col + "Respiratory Effort" + colEnd
    htmlText += col + final_dict["r_1"] + colEnd
    htmlText += col + final_dict["r_5"] + colEnd
    htmlText += col + final_dict["r_10"] + colEnd
    htmlText += col + final_dict["r_15"] + colEnd
    htmlText += col + final_dict["r_20"] + colEnd
    htmlText += rowEnd

    htmlText += row
    htmlText += col + "Total" + colEnd
    htmlText += col + final_dict["total_1"] + colEnd
    htmlText += col + final_dict["total_5"] + colEnd
    htmlText += col + final_dict["total_10"] + colEnd
    htmlText += col + final_dict["total_15"] + colEnd
    htmlText += col + final_dict["total_20"] + colEnd
    htmlText += rowEnd

    htmlText += tableEnd
    

    htmlText += linebreak

    



    

        
        

    htmlText += linebreak
    htmlText += linebreak

    htmlText += "Passive Cooling :" + final_dict["passive_cooling"] + linebreak
    if final_dict["passive_cooling"]=="Yes":
        htmlText += "Age in minutes :" + final_dict["age_in_minutes"] + linebreak
    """
    "arterial",
    "ph_column",
    "ph",
    "pco2_column",
    "pco2",
    "hco3_column",
    "hco3",
    "be_column",
    "be",
    "lactate_column",
    "lactate",
    "section_break_ibq8d",
    "venous",
    "ph_v",
    "ph_d",
    "pco2_v",
    "pco2_vd",
    "hco3_v",
    "hco3_vd",
    "be_v",
    "be_vd",
    "lactate_v",
    "lactate_vd",
    "section_break_iwuvv",
    "delayed_cord_clamping",
    "section_break_cmr7k",
    "resuscitation"
    """
    htmlText += linebreak
    if final_dict["arterial"]:
        htmlText += "Arterial :" + linebreak
        htmlText += "Ph :" +  final_dict["ph"] + linebreak
        htmlText += "PCO2 :" +  final_dict["pco2"] + linebreak
        htmlText += "HCO3 :" +  final_dict["hco3"] + linebreak
        htmlText += "BE :" +  final_dict["be"] + linebreak
        htmlText += "Lactate :" +  final_dict["lactate"] + linebreak
    htmlText += linebreak
    if final_dict["venous"]:
        htmlText += "Venous :" + linebreak
        htmlText += "Ph :" +  final_dict["ph_d"] + linebreak
        htmlText += "PCO2 :" +  final_dict["pco2_vd"] + linebreak
        htmlText += "HCO3 :" +  final_dict["hco3_vd"] + linebreak
        htmlText += "BE :" +  final_dict["be_vd"] + linebreak
        htmlText += "Lactate :" +  final_dict["lactate_vd"] + linebreak
    htmlText += linebreak

    htmlText += "Delayed Cord Clamping :" + final_dict["delayed_cord_clamping"] + linebreak
    htmlText += "Resuscitation :" + final_dict["resuscitation"] + linebreak




    
    return htmlText


@frappe.whitelist()
def getAdmissionDetails(baby_id):
    """
    Admission Details
    """
    admission_details = frappe.get_doc('Admission', {'baby_id': baby_id})
    final_json = admission_details.as_json()
    
    return final_json


@frappe.whitelist()
def getMotherMRD(baby_id):
    """
    Opening page
    """
    op = frappe.get_doc('Opening page', {'baby_id': baby_id})
    return op.mother_mrd