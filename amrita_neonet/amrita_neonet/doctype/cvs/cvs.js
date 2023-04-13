// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('CVS', {
	// refresh: function(frm) {

	// }
	go_back_to_respiratory(frm){
		frm.save();
		frappe.set_route("Form", "Respiratory", frm.doc.name);
	},
	save_and_goto_gi(frm){
		frm.save();
		frappe.set_route("Form", "Gastrointestinal", frm.doc.name);
	}
});
