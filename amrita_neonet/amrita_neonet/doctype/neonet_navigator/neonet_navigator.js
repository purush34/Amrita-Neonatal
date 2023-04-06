// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Neonet_Navigator', {
	// refresh: function(frm) {

	// }
	opening_form: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "testbabies", frm.doc.baby_id)
	},
	admission: function (frm) {
		console.log("frm.doc.baby_id", frm.doc.baby_id);
		frappe.set_route("Form", "Admission", frm.doc.baby_id)
	},
	maternal: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "Maternal And Antenatal Details", frm.doc.baby_id)
	},
	respiratory: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "Respiratory", frm.doc.baby_id)
	},
	cvs: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "cvs", frm.doc.baby_id)
	},
	gi: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "GI", frm.doc.baby_id)
	},
	cns: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "cns", frm.doc.baby_id)
	},
	endocrine_and_metabollic: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "Endocrine and metabolic", frm.doc.baby_id)
	},
	sepsis: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "sepsis", frm.doc.baby_id)
	},
	opthalmology: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "opthalmology", frm.doc.baby_id)
	},
	ent_and_swallow: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "ENT and Swallow", frm.doc.baby_id)
	},
	haematology: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "haematology", frm.doc.baby_id)
	},
	renal: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "renal", frm.doc.baby_id)
	},
	genetic: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "genetic", frm.doc.baby_id)
	},
	crib_ii_score: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "CRIB score", frm.doc.baby_id)
	},
	snappe_ii: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.set_route("Form", "Snappe II", frm.doc.baby_id)
	},
	
	
});
