// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Genetic', {
	// refresh: function(frm) {

	// }
	go_back_to_renal(frm){
		frm.save();
		frappe.set_route("Form", "Renal", frm.doc.name);
	},
	save_and_goto_navigator(frm){
		frm.save();
		frappe.set_route("Form", "Neonet_Navigator");
	}
});
