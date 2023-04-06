# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

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