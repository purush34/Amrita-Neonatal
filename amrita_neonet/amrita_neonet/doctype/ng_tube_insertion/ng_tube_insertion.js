// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('NG tube insertion', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('NG tube insertion_child', {
	"add_reports_add": function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        if (frm.doc.add_reports.length > 1){
			var date = frm.doc.add_reports[frm.doc.add_reports.length - 2].date_inserted;
			row.date_inserted = frappe.datetime.add_days(date,1);
			frm.refresh_field("add_reports");
		}
		else{
			row.date_inserted = frappe.datetime.get_today();
			frm.refresh_field("add_reports");
		}
    },
});