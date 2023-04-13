// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('CNS', {
	// refresh: function(frm) {

	// }
	go_back_to_gi(frm){
		frm.save();
		frappe.set_route("Form", "gastrointestinal", frm.doc.name);
	},
	save_and_goto_endocrine_and_metabolic(frm){
		frm.save();
		frappe.set_route("Form", "Endocrine and Metabolic", frm.doc.name);
	},
});
