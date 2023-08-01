// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Blood culture', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Blood culture_child', {
	"add_reports_add": function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        if (frm.doc.add_reports.length > 1){
			var date = frm.doc.add_reports[frm.doc.add_reports.length - 2].date_done;
			row.date_done = frappe.datetime.add_days(date,1);
			frm.refresh_field("add_reports");
		}
		else{
			row.date_done = frappe.datetime.get_today();
			frm.refresh_field("add_reports");
		}
    },
});