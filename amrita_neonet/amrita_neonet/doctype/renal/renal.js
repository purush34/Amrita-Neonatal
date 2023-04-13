// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Renal', {
	// refresh: function(frm) {

	// }
	go_back_to_haematology(frm){
		frm.save();
		frappe.set_route("Form", "Haematology", frm.doc.name);
	},
	save_and_goto_genetic(frm){
		frm.save();
		frappe.set_route("Form", "Genetic", frm.doc.name);
	}
});
