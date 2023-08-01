# Copyright (c) 2023, ICTS and contributors
# For license information, please see license.txt

import frappe,json
from frappe.model.document import Document

class Neonet_Navigator(Document):
	def before_save(self):
		self.baby_id = ''
		self.reminders = ''
		self.mother_mrd = ''
	
@frappe.whitelist()
def getMotherMrd(baby_id):
	dashboard = {}
	try:
		opening_page = frappe.get_doc("Opening page", baby_id)
		mother_mrd = opening_page.mother_mrd
		if mother_mrd == None:
			dashboard["mother_mrd"] =  "MOTHER MRD NOT FOUND"
		maternalDetails = frappe.get_doc("Maternal details", {'mother_mrd':mother_mrd})
		dashboard["mother_mrd"] = maternalDetails.get_title()
		dashboard["dob"] = str(opening_page.dob)
		dashboard["doa"] = str(opening_page.doa)
		dashboard["gabw"] = opening_page.gab_w
		dashboard["gabd"] = opening_page.gab_d
		jsondata = json.dumps(dashboard)
		return jsondata
	except:
		return "	"
	

""" 

<div class="d-flex flex-wrap">
<div class="alert alert-success flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">
      <p style="margin-bottom: 5px;">Date: June 25, 2023</p>
      <p style="margin-bottom: 0;">Task: Complete project report</p>
    </div>
    <div class="alert alert-danger flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">
      <p style="margin-bottom: 5px;">Date: June 25, 2023</p>
      <p style="margin-bottom: 0;">Task: Complete project report</p>
    </div>
    <div class="alert alert-warning flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">
      <p style="margin-bottom: 5px;">Date: June 25, 2023</p>
      <p style="margin-bottom: 0;">Task: Complete project report</p>
    </div>
</div>
 """

def makeHtmlStr(taskName,date):
	now = frappe.utils.nowdate()
	dayDiff = frappe.utils.date_diff(date,now)
	html = ''
	if dayDiff < 1:
		html += '<div class="alert alert-danger flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">'
		html += '<p style="margin-bottom: 5px;">Date: ' + date.strftime("%d %B, %Y") + ('</p>' if dayDiff == 0 else ' [Past]</p>')
		html += '<p style="margin-bottom: 0;">Task: ' + taskName + '</p>'
		html += '</div>'
	elif dayDiff < 5:
		html += '<div class="alert alert-success flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">'
		html += '<p style="margin-bottom: 5px;">Date: ' + \
			date.strftime("%d %B, %Y") + '</p>'
		html += '<p style="margin-bottom: 0;">Task: ' + taskName + '</p>'
		html += '</div>'
	else:
		html += '<div class="alert alert-warning flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">'
		html += '<p style="margin-bottom: 5px;">Date: ' + \
			date.strftime("%d %B, %Y") + '</p>'
		html += '<p style="margin-bottom: 0;">Task: ' + taskName + '</p>'
		html += '</div>'
	return html



@frappe.whitelist()
def getReminders(baby_id):
	try:
		reminders = frappe.get_doc('Reminders', baby_id)
		x = reminders.get_all_children()
		html = ''
		html += '<div class="d-flex flex-wrap">'
		arr = []
		for i in x:
			if i.status == 'Pending':
				arr.append((i.task,i.remind_on))
		arr.sort(key=lambda x: x[1])
		if len(arr)==0:
			html += '<div class="alert alert-success flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">'
			html += '<p style="margin-bottom: 5px;">No Reminders</p>'
			html += '</div>'
			html += '</div>'
			return html
		for i in arr:
			html += makeHtmlStr(i[0],i[1])
		html += '</div>'

		return html
	except:
		return '<div class="alert alert-success flex-grow-1" role="alert" style="max-width: 300px; margin-right: 10px;">' + \
			'<p style="margin-bottom: 5px;">No Reminders(Form dosent exist)</p>' + \
			'</div>' + \
			'</div>'
