# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import json

class Admission(Document):
	pass


@frappe.whitelist()
def create_admission(baby_id,mother_name):
    print("create_admission")
    admission = frappe.new_doc('Admission')
    admission.baby_id = baby_id
    admission.mother_name = mother_name
    admission.save()

@frappe.whitelist()
def delete_admission(doc, method):
    admission = frappe.get_doc('Admission', {'baby_id': doc.baby_id})
    admission.delete()


@frappe.whitelist()
def getWeight(babyid):
    """
    
    """
    page = frappe.get_doc('Opening page',{'baby_id':babyid})
    auto = { 
        "admission_weight": page.admission_weight
    }
    return json.dumps(auto)

@frappe.whitelist()
def getSummery(baby_id):
     """
     admission_weight
     admission_ofc
     admission_length
     gaa_v
     doa
     """
     page = frappe.get_doc('Admission',{'baby_id':baby_id})
     opage = frappe.get_doc('Opening page',{'baby_id':baby_id})
     res = {
            "admission_weight": page.admission_weight,
            "admission_ofc": page.admission_ofc,
            "admission_length": page.admission_length,
            "gaa_v" : opage.gaa_v,
            "doa" : str(opage.doa),
            "dob": str(opage.dob)
     }
     return json.dumps(res)
