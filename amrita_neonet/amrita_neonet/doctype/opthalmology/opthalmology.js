// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Opthalmology', {
	// refresh: function(frm) {

	// }
	go_back_to_sepsis(frm){
		frm.save();
		frappe.set_route("Form", "Sepsis", frm.doc.name);
	},
	save_and_goto_ent_swallow(frm){
		frm.save();
		frappe.set_route("Form", "ENT and Swallow", frm.doc.name);
	}
});
