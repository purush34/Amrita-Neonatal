# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Openingpage(Document):
    def before_insert(self):
        # admission
        admission = frappe.new_doc('Admission')
        admission.baby_id = self.baby_id
        admission.mother_name = self.mother_name
        admission.save()

        # baby_selfuments
        # baby_selfuments = frappe.new_doc('Baby Documents')
        # baby_selfuments.baby_id = self.baby_id
        # baby_selfuments.mother_name = self.mother_name
        # baby_selfuments.save()
        """
        # blood_culture
        blood_culture = frappe.new_doc('Blood culture')
        blood_culture.baby_id = self.baby_id
        blood_culture.mother_name = self.mother_name
        blood_culture.save()

        # catheterisation
        catheterisation = frappe.new_doc('Catheterisation')
        catheterisation.baby_id = self.baby_id
        catheterisation.mother_name = self.mother_name
        catheterisation.save()

        # chest_drain
        chest_drain = frappe.new_doc('Chest Drain')
        chest_drain.baby_id = self.baby_id
        chest_drain.mother_name = self.mother_name
        chest_drain.save()

        # cns
        cns = frappe.new_doc('Cns')
        cns.baby_id = self.baby_id
        cns.mother_name = self.mother_name
        cns.save()

        # cooling_criteria
        cooling_criteria = frappe.new_doc('Cooling Criteria')
        cooling_criteria.baby_id = self.baby_id
        cooling_criteria.mother_name = self.mother_name
        cooling_criteria.save()

        # cooloing_criteria
        cooloing_criteria = frappe.new_doc('Cooloing Criteria')
        cooloing_criteria.baby_id = self.baby_id
        cooloing_criteria.mother_name = self.mother_name
        cooloing_criteria.save()

        # crib_score
        crib_score = frappe.new_doc('Crib Score')
        crib_score.baby_id = self.baby_id
        crib_score.mother_name = self.mother_name
        crib_score.save()

        # ct
        ct = frappe.new_doc('Ct')
        ct.baby_id = self.baby_id
        ct.mother_name = self.mother_name
        ct.save()

        # cvs
        cvs = frappe.new_doc('Cvs')
        cvs.baby_id = self.baby_id
        cvs.mother_name = self.mother_name
        cvs.save()

        # death_summery
        death_summery = frappe.new_doc('Death Summery')
        death_summery.baby_id = self.baby_id
        death_summery.mother_name = self.mother_name
        death_summery.save()

        # discharge_checklist
        discharge_checklist = frappe.new_doc('Discharge Checklist')
        discharge_checklist.baby_id = self.baby_id
        discharge_checklist.mother_name = self.mother_name
        discharge_checklist.save()

        # discharge_examination
        discharge_examination = frappe.new_doc('Discharge Examination')
        discharge_examination.baby_id = self.baby_id
        discharge_examination.mother_name = self.mother_name
        discharge_examination.save()

        # discharge_letter
        discharge_letter = frappe.new_doc('Discharge Letter')
        discharge_letter.baby_id = self.baby_id
        discharge_letter.mother_name = self.mother_name
        discharge_letter.save()

        # echocardiography
        echocardiography = frappe.new_doc('Echocardiography')
        echocardiography.baby_id = self.baby_id
        echocardiography.mother_name = self.mother_name
        echocardiography.save()

        # electroencephalography
        electroencephalography = frappe.new_doc('Electroencephalography')
        electroencephalography.baby_id = self.baby_id
        electroencephalography.mother_name = self.mother_name
        electroencephalography.save()

        # enselfrine_and_metabolic
        enselfrine_and_metabolic = frappe.new_doc('Enselfrine And Metabolic')
        enselfrine_and_metabolic.baby_id = self.baby_id
        enselfrine_and_metabolic.mother_name = self.mother_name
        enselfrine_and_metabolic.save()

        # ent_and_swallow
        ent_and_swallow = frappe.new_doc('Ent And Swallow')
        ent_and_swallow.baby_id = self.baby_id
        ent_and_swallow.mother_name = self.mother_name
        ent_and_swallow.save()

        # genetic
        genetic = frappe.new_doc('Genetic')
        genetic.baby_id = self.baby_id
        genetic.mother_name = self.mother_name
        genetic.save()

        # genetic_tests
        genetic_tests = frappe.new_doc('Genetic Tests')
        genetic_tests.baby_id = self.baby_id
        genetic_tests.mother_name = self.mother_name
        genetic_tests.save()

        # gi
        gi = frappe.new_doc('Gi')
        gi.baby_id = self.baby_id
        gi.mother_name = self.mother_name
        gi.save()

        # haematology
        haematology = frappe.new_doc('Haematology') 
        haematology.baby_id = self.baby_id
        haematology.mother_name = self.mother_name
        haematology.save()

        # intubation
        intubation = frappe.new_doc('Intubation')
        intubation.baby_id = self.baby_id
        intubation.mother_name = self.mother_name
        intubation.save()

        # lumbar_puncture
        lumbar_puncture = frappe.new_doc('Lumbar Puncture')
        lumbar_puncture.baby_id = self.baby_id
        lumbar_puncture.mother_name = self.mother_name
        lumbar_puncture.save()

        # maternal_and_antenatal_details
        maternal_and_antenatal_details = frappe.new_doc('Maternal And Antenatal Details')
        maternal_and_antenatal_details.baby_id = self.baby_id
        maternal_and_antenatal_details.mother_name = self.mother_name
        maternal_and_antenatal_details.save()

        # mri

        mri = frappe.new_doc('Mri')
        mri.baby_id = self.baby_id
        mri.mother_name = self.mother_name
        mri.save()

        # naso__pharyngeal_tube
        naso__pharyngeal_tube = frappe.new_doc('Naso  Pharyngeal Tube')
        naso__pharyngeal_tube.baby_id = self.baby_id
        naso__pharyngeal_tube.mother_name = self.mother_name
        naso__pharyngeal_tube.save()

        # neogen
        neogen = frappe.new_doc('Neogen')
        neogen.baby_id = self.baby_id
        neogen.mother_name = self.mother_name
        neogen.save()

        # neonet_navigator
        neonet_navigator = frappe.new_doc('Neonet Navigator')
        neonet_navigator.baby_id = self.baby_id
        neonet_navigator.mother_name = self.mother_name
        neonet_navigator.save()

        # neurosonogram
        neurosonogram = frappe.new_doc('Neurosonogram')
        neurosonogram.baby_id = self.baby_id
        neurosonogram.mother_name = self.mother_name
        neurosonogram.save()

        # ng_tube_insertion
        ng_tube_insertion = frappe.new_doc('Ng Tube Insertion')
        ng_tube_insertion.baby_id = self.baby_id
        ng_tube_insertion.mother_name = self.mother_name
        ng_tube_insertion.save()

        # opening_page
        opening_page = frappe.new_doc('Opening Page')
        opening_page.baby_id = self.baby_id
        opening_page.mother_name = self.mother_name
        opening_page.save()

        # ophthalmology
        ophthalmology = frappe.new_doc('Ophthalmology')
        ophthalmology.baby_id = self.baby_id
        ophthalmology.mother_name = self.mother_name
        ophthalmology.save()

        # # page1
        # page1 = frappe.new_doc('Page1')
        # page1.baby_id = self.baby_id
        # page1.mother_name = self.mother_name
        # page1.save()

        # # page2
        # page2 = frappe.new_doc('Page2')
        # page2.baby_id = self.baby_id
        # page2.mother_name = self.mother_name
        # page2.save()

        # # page3
        # page3 = frappe.new_doc('Page3')
        # page3.baby_id = self.baby_id
        # page3.mother_name = self.mother_name
        # page3.save()

        # pcr
        pcr = frappe.new_doc('Pcr')
        pcr.baby_id = self.baby_id
        pcr.mother_name = self.mother_name
        pcr.save()

        # pericardial_tap
        pericardial_tap = frappe.new_doc('Pericardial Tap')
        pericardial_tap.baby_id = self.baby_id
        pericardial_tap.mother_name = self.mother_name
        pericardial_tap.save()

        # peripheral_arterial_line
        peripheral_arterial_line = frappe.new_doc('Peripheral Arterial Line')
        peripheral_arterial_line.baby_id = self.baby_id
        peripheral_arterial_line.mother_name = self.mother_name
        peripheral_arterial_line.save()

        # peritoneal_drain
        peritoneal_drain = frappe.new_doc('Peritoneal Drain')
        peritoneal_drain.baby_id = self.baby_id
        peritoneal_drain.mother_name = self.mother_name
        peritoneal_drain.save()

        # peritoneal_tap
        peritoneal_tap = frappe.new_doc('Peritoneal Tap')
        peritoneal_tap.baby_id = self.baby_id
        peritoneal_tap.mother_name = self.mother_name
        peritoneal_tap.save()

        # picc_line
        picc_line = frappe.new_doc('Picc Line')
        picc_line.baby_id = self.baby_id
        picc_line.mother_name = self.mother_name
        picc_line.save()

        # pleural_tap
        pleural_tap = frappe.new_doc('Pleural Tap')
        pleural_tap.baby_id = self.baby_id
        pleural_tap.mother_name = self.mother_name
        pleural_tap.save()

        # renal
        renal = frappe.new_doc('Renal')
        renal.baby_id = self.baby_id
        renal.mother_name = self.mother_name
        renal.save()

        # respiratory
        respiratory = frappe.new_doc('Respiratory')
        respiratory.baby_id = self.baby_id
        respiratory.mother_name = self.mother_name
        respiratory.save()

        # respiratory_secreations
        respiratory_secreations = frappe.new_doc('Respiratory Secreations')
        respiratory_secreations.baby_id = self.baby_id
        respiratory_secreations.mother_name = self.mother_name
        respiratory_secreations.save()

        # respiratory_secreations
        respiratory_secreations = frappe.new_doc('Respiratory Secreations')
        respiratory_secreations.baby_id = self.baby_id
        respiratory_secreations.mother_name = self.mother_name
        respiratory_secreations.save()

        # retinopathy_of_prematurity
        retinopathy_of_prematurity = frappe.new_doc('Retinopathy Of Prematurity')
        retinopathy_of_prematurity.baby_id = self.baby_id
        retinopathy_of_prematurity.mother_name = self.mother_name
        retinopathy_of_prematurity.save()

        # sepsis
        sepsis = frappe.new_doc('Sepsis')
        sepsis.baby_id = self.baby_id
        sepsis.mother_name = self.mother_name
        sepsis.save()

        # snappe_ii
        snappe_ii = frappe.new_doc('Snappe Ii')
        snappe_ii.baby_id = self.baby_id
        snappe_ii.mother_name = self.mother_name
        snappe_ii.save()

        # subclavian_femoral_line
        subclavian_femoral_line = frappe.new_doc('Subclavian Femoral Line')
        subclavian_femoral_line.baby_id = self.baby_id
        subclavian_femoral_line.mother_name = self.mother_name
        subclavian_femoral_line.save()

        # summary
        summary = frappe.new_doc('Summary')
        summary.baby_id = self.baby_id
        summary.mother_name = self.mother_name
        summary.save()

        # surgical_operative_note
        surgical_operative_note = frappe.new_doc('Surgical Operative Note')
        surgical_operative_note.baby_id = self.baby_id
        surgical_operative_note.mother_name = self.mother_name
        surgical_operative_note.save()

        # swabs
        swabs = frappe.new_doc('Swabs')
        swabs.baby_id = self.baby_id
        swabs.mother_name = self.mother_name
        swabs.save()

        # # test_1
        # test_1 = frappe.new_doc('Test 1')
        # test_1.baby_id = self.baby_id
        # test_1.mother_name = self.mother_name
        # test_1.save()

        # # testbabies
        # testbabies = frappe.new_doc('Testbabies')
        # testbabies.baby_id = self.baby_id
        # testbabies.mother_name = self.mother_name
        # testbabies.save()

        # umbiilical_lines
        umbiilical_lines = frappe.new_doc('Umbiilical Lines')
        umbiilical_lines.baby_id = self.baby_id
        umbiilical_lines.mother_name = self.mother_name
        umbiilical_lines.save()

        # urine_peritoneal_pleural_fluid
        urine_peritoneal_pleural_fluid = frappe.new_doc('Urine Peritoneal Pleural Fluid')
        urine_peritoneal_pleural_fluid.baby_id = self.baby_id
        urine_peritoneal_pleural_fluid.mother_name = self.mother_name
        urine_peritoneal_pleural_fluid.save()

        # uss_kub_abdomen
        uss_kub_abdomen = frappe.new_doc('Uss Kub Abdomen')
        uss_kub_abdomen.baby_id = self.baby_id
        uss_kub_abdomen.mother_name = self.mother_name
        uss_kub_abdomen.save()

        """





""" 
admission
antibiotics
baby_selfuments
blood_culture
catheterisation
chest_drain
cns
cooling_criteria
cooloing_criteria
crib_score
ct
cvs
death_summery
discharge_checklist
discharge_examination
discharge_letter
echocardiography
electroencephalography
enselfrine_and_metabolic
ent_and_swallow
genetic
genetic_tests
gi
haematology
intubation
lumbar_puncture
maternal_and_antenatal_details
mri
naso__pharyngeal_tube
neogen
neonet_navigator
neurosonogram
ng_tube_insertion
opening_page
opthalmology
page1
page2
page3
pcr
pericardial_tap
peripheral_arterial_line
peritoneal_drain
peritoneal_tap
picc_line
pleural_tap
renal
respiratory
respiratory_secreations
retinopathy_of_prematurity
sepsis
snappe_ii
subclavian_femoral_line
summary
surgical_operative_note
swabs
test_1
testbabies
umbiilical_lines
urine_peritoneal_pleural_fluid
uss_kub_abdomen
"""

# @frappe.whitelist()
# def before_insert(self, method):
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.admission.admission.create_admission', args=(self.baby_id, self.mother_name), method='POST')  
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.antibiotics.antibiotics.create_antibiotics', args=(self.baby_id, self.mother_name), method='POST')  
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.baby_selfuments.baby_selfuments.create_baby_selfuments', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.blood_culture.blood_culture.create_blood_culture', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.catheterisation.catheterisation.create_catheterisation', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.chest_drain.chest_drain.create_chest_drain', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.cns.cns.create_cns', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.cooling_criteria.cooling_criteria.create_cooling_criteria', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.crib_score.crib_score.create_crib_score', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.ct.ct.create_ct', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.cvs.cvs.create_cvs', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.death_summery.death_summery.create_death_summery', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.discharge_checklist.discharge_checklist.create_discharge_checklist', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.discharge_examination.discharge_examination.create_discharge_examination', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.discharge_letter.discharge_letter.create_discharge_letter', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.echocardiography.echocardiography.create_echocardiography', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.electroencephalography.electroencephalography.create_electroencephalography', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.enselfrine_and_metabolic.enselfrine_and_metabolic.create_enselfrine_and_metabolic', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.ent_and_swallow.ent_and_swallow.create_ent_and_swallow', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.genetic.genetic.create_genetic', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.genetic_tests.genetic_tests.create_genetic_tests', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.gi.gi.create_gi', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.haematology.haematology.create_haematology', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.incuabtion.incuabtion.create_incuabtion', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.lumbar_puncture.lumbar_puncture.create_lumbar_puncture', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.mri.mri.create_mri', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.maternal_and_antenatal_details.maternal_and_antenatal_details.create_maternal_and_antenatal_details', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.naso__pharyngeal_tube.naso__pharyngeal_tube.create_naso__pharyngeal_tube', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.neogen.neogen.create_neogen', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.neurosonogram.neurosonogram.create_neurosonogram', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.ng_tube_insertion.ng_tube_insertion.create_ng_tube_insertion', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.opthalmology.opthalmology.create_opthalmology', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.pericardial_tap.pericardial_tap.create_pericardial_tap', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.peripheral_arterial_line.peripheral_arterial_line.create_peripheral_arterial_line', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.peritoneal_drain.peritoneal_drain.create_peritoneal_drain', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.picc_line.picc_line.create_picc_line', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.pleural_tap.pleural_tap.create_pleural_tap', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.peritoneal_tap.peritoneal_tap.create_peritoneal_tap', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.renal.renal.create_renal', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.respiratory.respiratory.create_respiratory', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.respiratory_secreations.respiratory_secreations.create_respiratory_secreations', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.retinopathy_of_prematurity.retinopathy_of_prematurity.create_retinopathy_of_prematurity', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.sepsis.sepsis.create_sepsis', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.snappe_ii.snappe_ii.create_snappe_ii', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.subclavian_femoral_line.subclavian_femoral_line.create_subclavian_femoral_line', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.summary.summary.create_summary', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.surgical_operative_note.surgical_operative_note.create_surgical_operative_note', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.umbiilical_lines.umbiilical_lines.create_umbiilical_lines', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.urine_peritoneal_pleural_fluid.urine_peritoneal_pleural_fluid.create_urine_peritoneal_pleural_fluid', args=(self.baby_id, self.mother_name), method='POST')
#     frappe.enqueue('amrita_neonet.amrita_neonet.selftype.uss_kub_abdomen.uss_kub_abdomen.create_uss_kub_abdomen', args=(self.baby_id, self.mother_name), method='POST')


# @frappe.whitelist()
# def before_insert(doc, method):
#     print("before insert from below")
#     print(doc.baby_id)
#     print(doc.mother_name)
#     frappe.enqueue('amrita_neonet.amrita_neonet.doctype.admission.admission.create_admission', args=(doc.baby_id, doc.mother_name), method='POST')






# # Path: apps/amrita_neonet/amrita_neonet/amrita_neonet/selftype/opening_page/opening_page.py
