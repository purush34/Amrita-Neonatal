// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Antenatal-1', {
	// refresh: function(frm) {

	// }
	"go_to_antenatal_2" : function(frm){
		frm.save();
		frappe.set_route("Form", "Antenatal-2", frm.doc.name);
	},
	"lmp" : function(frm){
		var days = 280;
		frm.set_value("edd_by_dates", frappe.datetime.add_days(frm.doc.lmp, days));
	},
});
