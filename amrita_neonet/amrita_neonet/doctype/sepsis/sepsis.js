// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sepsis', {
	// refresh: function(frm) {

	// }
	go_back_to_endocrine_and_metabolic(frm){
		frm.save();
		frappe.set_route("Form", "Endocrine and Metabolic", frm.doc.name);
	},
	save_and_goto_ophthalmology(frm){
		frm.save();
		frappe.set_route("Form", "Opthalmology", frm.doc.name);
	},
});
