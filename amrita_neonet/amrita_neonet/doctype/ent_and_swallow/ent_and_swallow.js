// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('ENT and Swallow', {
	// refresh: function(frm) {

	// }
	go_back_to_opthalmology(frm){	
		frm.save();
		frappe.set_route("Form", "Opthalmology", frm.doc.name);
	},
	save_and_goto_haematology(frm){
		frm.save();
		frappe.set_route("Form", "Haematology", frm.doc.name);
	},
});
