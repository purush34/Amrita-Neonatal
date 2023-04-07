# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Openingpage(Document):
    all_dict_doctypes = {
        'Admission': 'admission',
        # 'Antibiotics': 'antibiotics',
        'Baby Documents': 'baby_documents',
        'Blood culture': 'blood_culture',
        'Catheterisation': 'catheterisation',
        'Chest drain': 'chest_drain',
        'CNS': 'cns',
        'Cooling Criteria': 'cooling_criteria',
        'CRIB score': 'crib_score',
        'CT': 'ct',
        'CVS': 'cvs',
        'Death summery': 'death_summery',
        'Discharge checklist': 'discharge_checklist',
        'Discharge examination': 'discharge_examination',
        'Discharge letter': 'discharge_letter',
        'Echocardiography': 'echocardiography',
        'Electroencephalography': 'electroencephalography',
        # 'Enselfrine And Metabolic': 'enselfrine_and_metabolic',
        'ENT and Swallow': 'ent_and_swallow',
        'Genetic': 'genetic',
        'Genetic Tests': 'genetic_tests',
        'GI': 'gi',
        'Haematology': 'haematology',
        'Intubation': 'intubation',
        'Lumbar puncture': 'lumbar_puncture',
        'Maternal And Antenatal Details': 'maternal_and_antenatal_details',
        'MRI': 'mri',
        'Naso- Pharyngeal tube': 'naso__pharyngeal_tube',
        'Neogen': 'neogen',
        # 'Neonet Navigator': 'neonet_navigator',
        'Neurosonogram': 'neurosonogram',
        'NG tube insertion': 'ng_tube_insertion',
        # 'Opening Page': 'opening_page',
        'Opthalmology': 'opthalmology',
        'PCR': 'pcr',
        'Pericardial tap': 'pericardial_tap',
        'Peripheral Arterial line': 'peripheral_arterial_line',
        'Peritoneal drain': 'peritoneal_drain',
        'Peritoneal tap': 'peritoneal_tap',
        'PICC line': 'picc_line',
        'Pleural tap': 'pleural_tap',
        'Renal': 'renal',
        'Respiratory': 'respiratory',
        'Retinopathy of Prematurity':'retinopathy_of_prematurity',
        'Respiratory secreations': 'respiratory_secreations',
        'Sepsis': 'sepsis',
        'Surgical Operative Note': 'surgical_operative_note',
        'Subclavian_femoral line': 'subclavian_femoral_line',
        'Swabs': 'swabs',
        'Umbiilical lines': 'umbiilical_lines',
        'Urine_Peritoneal_Pleural fluid': 'urine_peritoneal_pleural_fluid',
        'USS KUB_Abdomen': 'uss_kub_abdomen',
    }
    def before_insert(self):
        """Called before doc is saved."""
        for i in self.all_dict_doctypes.keys():
            temp = frappe.new_doc(i)
            print(i)
            temp.baby_id = self.baby_id
            temp.mother_name = self.mother_name
            temp.save()

    def on_trash(self):
        """Called when doc is trashed."""
        for i in self.all_dict_doctypes.keys():
            temp = frappe.get_doc(i, {'baby_id': self.baby_id})
            temp.delete()
        # neogen = frappe.get_doc('Neogen', {'baby_id': self.baby_id})
        # neogen.delete()

        









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
umbiilical_lines
urine_peritoneal_pleural_fluid
uss_kub_abdomen
"""

