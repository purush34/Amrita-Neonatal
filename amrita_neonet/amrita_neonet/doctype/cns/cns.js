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
	cooling_details: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "Cooling Criteria", frm.doc.name)
	},
});
frappe.ui.form.on('child_cns', {
	// refresh: function(frm) {

	// }
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