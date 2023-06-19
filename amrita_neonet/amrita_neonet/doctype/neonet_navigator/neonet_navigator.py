# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Neonet_Navigator(Document):
	def before_save(self):
		self.baby_id = ''
	
@frappe.whitelist()
def getMotherMrd(baby_id):
	opening_page = frappe.get_doc("Opening page", baby_id)
	return opening_page.mother_mrd or 'Not Found'
