// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test-1', {
	// refresh: function(frm) {

	// }
	page1: function (frm) {
		console.log(frm.doc.mid);
		frappe.set_route("Form", "testbabies", frm.doc.mid)
	}
});
