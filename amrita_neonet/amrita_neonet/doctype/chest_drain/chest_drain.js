// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Chest drain', {
	// refresh: function(frm) {

	// }
	
});

frappe.ui.form.on('Chest drain_child', {
	"add_reports_add": function(frm, cdt, cdn) {
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
