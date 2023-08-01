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

frappe.ui.form.on("child_sepsis",{
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
    }
});

frappe.ui.form.on("Sepsis Antibiotics",{
		start_date(frm, cdt, cdn) {
			calc_day_diff(frm, cdt, cdn);
		},
		end_date(frm, cdt, cdn) {
			calc_day_diff(frm, cdt, cdn);
		}
})
frappe.ui.form.on("Sepsis Antifungals",{
		start_date(frm, cdt, cdn) {
			calc_day_diff(frm, cdt, cdn);
		},
		end_date(frm, cdt, cdn) {
			calc_day_diff(frm, cdt, cdn);
		}
})

function calc_day_diff(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	if (child.continuing){
		var diff = frappe.datetime.get_day_diff( frappe.datetime.get_today(),child.start_date)
		child.number_of_days = diff + " (continuing)";
		frm.refresh_fields();
	}
	else{
		var diff = frappe.datetime.get_day_diff(child.end_date, child.start_date)
		child.number_of_days = diff
		frm.refresh_fields();
	}
}