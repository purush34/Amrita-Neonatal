// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('testBabies', {
	// refresh: function(frm) {

	// }
});

// frappe.ui.form.on("testBabies", {
// 	before_save: function (frm) {
// 		// Call the create_admission function
// 		frappe.call({
// 			method: "amrita_neonet.amrita_neonet.doctype.page1.page1.create_page1",
// 			args: {
// 				baby_id: frm.doc.baby_id,
// 				mother_name: frm.doc.mother_name
// 			},
// 			callback: function (r) {
// 				if (r.message) {
// 					// Success message
// 					frappe.msgprint('Baby created successfully');
// 				} else {
// 					// Error message
// 					frappe.msgprint('Failed to create baby');
// 					// console.log(r.exc)
// 				}
// 			}
// 		});
// 	}
// });

// Path: apps/amrita_neonet/amrita_neonet/amrita_neonet/doctype/testbabies/testbabies.py