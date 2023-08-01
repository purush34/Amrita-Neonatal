// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maternal details', {
	// refresh: function(frm) {

	// }
	"ddob":function(frm){
		var today = frappe.datetime.get_today();
		var ag = frappe.datetime.get_diff(today, frm.doc.ddob);
		// console.log(ag);
		// calculate age in years
		ag = ag/365;
		frm.set_value("age", ag);
		frm.refresh_field("age");
	},
	"p_dob":function(frm){
		var today = frappe.datetime.get_today();
		var ag = frappe.datetime.get_diff(today, frm.doc.p_dob);
		// calculate age in years
		ag = ag/365;
		ag = Math.floor(ag);
		frm.set_value("p_age", ag);
		frm.refresh_field("p_age");
	},
	"go_to_antenatal_1": function(frm){
		frm.save();
		frappe.set_route("Form", "Antenatal-1", frm.doc.name);
	}
});
 