// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

function setGAA(frm) {
	var gad = frappe.datetime.get_day_diff(frm.doc.dob, frm.doc.doa);
	var g_days = parseInt(frm.doc.gab_w) * 7 + parseInt(frm.doc.gab_d);
	gad = gad + g_days
	frm.set_value("gaa_v", Math.floor(gad / 7) + " Weeks " + (gad % 7) + " Days");
}
frappe.ui.form.on('Opening page', {
	// refresh: function(frm) {

	// }
	"onload":function(frm){
		frm.set_value("doa", frappe.datetime.get_today())
		frm.set_value("dob", frappe.datetime.get_today())
	},
	"gab_w":function(frm){
		// console.log(frm.doc.gab_w)
		frm.set_value("gab_v", frm.doc.gab_w+" Weeks "+frm.doc.gab_d+" Days");
		setGAA(frm);
	},
	"gab_d":function(frm){
		// console.log(frm.doc.gab_d)
		frm.set_value("gab_v", frm.doc.gab_w+" Weeks "+frm.doc.gab_d+" Days");
		setGAA(frm);
	},
	"doa":function(frm){
		setGAA(frm);
	},
	"dob":function(frm){
		setGAA(frm);
	}


});
