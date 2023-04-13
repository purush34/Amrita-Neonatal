// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Haematology', {
	// refresh: function(frm) {

	// }
	go_back_to_ent_swallow(frm){
		frm.save();
		frappe.set_route("Form", "ENT and Swallow", frm.doc.name);
	},
	save_and_goto_renal(frm){
		frm.save();
		frappe.set_route("Form", "Renal", frm.doc.name);
	}
});
