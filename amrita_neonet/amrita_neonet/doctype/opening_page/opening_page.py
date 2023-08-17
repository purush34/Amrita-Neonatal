# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
import time
from frappe.model.document import Document

class Openingpage(Document):
    all_dict_doctypes = {
        'Admission': 'admission',
        # 'Antibiotics': 'antibiotics',
        'Baby Documents': 'baby_documents',
        'Birth and resuscitation' : 'birth_and _resuscitation',
        'Blood culture': 'blood_culture',
        'Catheterisation': 'catheterisation',
        'Chest drain': 'chest_drain',
        'CNS': 'cns',
        'Cooling Criteria': 'cooling_criteria',
        'Cooling Documentation': 'cooling_documentation',
        'CRIB score': 'crib_score',
        "Snappe II" : "snappe-ii",
        'CT': 'ct',
        'CVS': 'cvs',
        # 'Death summary': 'death_summery',
        'Discharge checklist': 'discharge_checklist',
        'Discharge examination': 'discharge_examination',
        # 'Discharge letter': 'discharge_letter',
        'Echocardiography': 'echocardiography',
        'Endocrine and metabolic': 'endocrine_and_metabolic',
        'Electroencephalography': 'electroencephalography',
        # 'Enselfrine And Metabolic': 'enselfrine_and_metabolic',
        'ENT and Swallow': 'ent_and_swallow',
        'Genetic': 'genetic',
        'Genetic Tests': 'genetic_tests',
        'Gastrointestinal': 'gastrointestinal',
        'Haematology': 'haematology',
        'Intubation': 'intubation',
        'Lumbar puncture': 'lumbar_puncture',
        # 'Maternal And Antenatal Details': 'maternal_and_antenatal_details',  # come back
        'MRI': 'mri',
        'Naso- Pharyngeal tube': 'naso__pharyngeal_tube',
        'Neogen': 'neogen',
        # 'Neonet Navigator': 'neonet_navigator',
        "NICU Stay Outcomes": "nicu_stay_outcomes",
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
        'Dermatology': 'dermatology',
        'Musculoskeletal': 'musculoskeletal',
        'Reminders': 'reminders',
    }
    motherDocs = {
        'Maternal details': 'maternal_details',
        'Antenatal-1': 'antenatal-1',
        'Antenatal-2': 'antenatal-2',
    }
    def before_insert(self):
        """Called before doc is saved."""
        for i in self.all_dict_doctypes.keys():
            try :
                temp = frappe.new_doc(i)
                temp.baby_id = self.baby_id
                temp.mother_name = self.mother_name
                temp.save()
                # print(i, "created")
            except Exception as r:
                print(f"{i} not created {r}")
        if not frappe.db.exists('Maternal details', {'mother_mrd': self.mother_mrd}):
            for i in self.motherDocs.keys():
                try :
                    temp = frappe.new_doc(i)
                    temp.mother_name = self.mother_name
                    temp.mother_mrd = self.mother_mrd
                    temp.save()
                    # print(i, "created")
                except Exception as r:
                    print(f"{i} not created {r}")

        # ad = frappe.new_doc('Admission')
        # ad.baby_id = self.baby_id
        # ad.mother_name = self.mother_name
        # ad.save()

    def on_trash(self):
        """Called when doc is trashed."""
        for i in self.all_dict_doctypes.keys():
            try :
                temp = frappe.get_doc(i, {'baby_id': self.baby_id})
                frappe.delete_doc(i, temp.name)
            except:
                print(f"{i} not deleted ")
        for i in self.motherDocs.keys():
            try :
                temp = frappe.get_doc(i, {'mother_mrd': self.mother_mrd})
                frappe.delete_doc(i, temp.name)
            except:
                print(f"{i} not deleted ")

        # neogen = frappe.get_doc('Neogen', {'baby_id': self.baby_id})
        # neogen.delete()
        # open = frappe.get_doc('Opening Page', {'baby_id': self.baby_id})
        # open.delete()

        # admi = frappe.get_doc('Admission', {'baby_id': self.baby_id})
        # frappe.delete_doc('Admission', admi.name)

        









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

