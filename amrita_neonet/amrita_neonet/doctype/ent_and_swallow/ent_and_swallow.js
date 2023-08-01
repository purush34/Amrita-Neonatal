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
frappe.ui.form.on('ent_child', {
	"daily_observations_add": function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        if (frm.doc.daily_observations.length > 1){
			var date = frm.doc.daily_observations[frm.doc.daily_observations.length - 2].date;
			row.date = frappe.datetime.add_days(date,1);
			frm.refresh_field("daily_observations");
		}
		else{
			row.date = frappe.datetime.get_today();
			frm.refresh_field("daily_observations");
		}
    },
});