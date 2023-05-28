// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

function setGAA(frm,doa,dob) {
	var gad = frappe.datetime.get_day_diff(doa,dob);
	frm.set_value("day_of_life", gad);
	// console.log(doa + " Hello");
	var g_days = parseInt(frm.doc.gab_w) * 7 + parseInt(frm.doc.gab_d);
	// console.log(g_days + " Hello");
	gad = gad + g_days
	frm.set_value("gaa_v", Math.floor(gad / 7) + " Weeks " + (gad % 7) + " Days");
}
frappe.ui.form.on('Opening page', {
	// refresh: function(frm) {

	// }
	
	"onload":function(frm){
		if (frm.doc.doa == null) {
			frm.set_value("doa", frappe.datetime.get_today())
		}
			
		if (frm.doc.dob == null) {
			frm.set_value("dob", frappe.datetime.get_today())
		}
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
		console.log(frm.doc.doa + " Hello doa");
		setGAA(frm, frm.doc.doa, frm.doc.dob);
	},
	"dob":function(frm){
		setGAA(frm);
	},
	"go_to_admission": function(frm){
		frm.save();
		frappe.set_route("Form", "Admission", frm.doc.name);
	}

 
});
