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
frappe.ui.form.on('child_genetic', {
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