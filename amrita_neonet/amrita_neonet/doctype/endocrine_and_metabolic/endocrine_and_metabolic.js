// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Endocrine and metabolic', {
	// refresh: function(frm) {

	// }
	go_back_to_cns(frm){
		frm.save();
		frappe.set_route("Form", "CNS", frm.doc.name);
	},
	save_and_goto_sepsis(frm){
		frm.save();
		frappe.set_route("Form", "Sepsis", frm.doc.name);
	}
});
