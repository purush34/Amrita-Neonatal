// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Admission', {
	// refresh: function(frm) {

	// }
	onload:function(frm){
		if (! frm.doc.baby_id) {
			return
		}
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.admission.admission.getWeight",
			args: {
				"babyid": frm.doc.baby_id
			},
			callback: function(r) {
				if(r.message) {
					var msg = JSON.parse(r.message);
					console.log(msg.admission_weight);
					frm.set_value("admission_weight", msg.admission_weight);
				}
			}
		})
	},
	"goto_maternal": function(frm){
		frm.save();
		frappe.set_route("Form", "Maternal details", frm.doc.name);
	}
});
 