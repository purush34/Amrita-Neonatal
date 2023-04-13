// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('NICU Stay Outcomes', {
	// refresh: function(frm) {

	// }
	onload: function(frm) {
		// frm.set_value("respiratory_discharge_summery", "print<br>hello");
	},
	refresh_data: function(frm) {
		/* 
		Respiratory
		CVS
		Gastroinstestine
		CNS
		Endocrine and Metabolic 
		Sepsis
		Ophthalmology
		ENT & Swallow
		Haematology
		Renal
		Genetic 
		*/
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getRespiratoryDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("respiratory_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getCVSDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("cvs_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getGastroinstestineDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("gastroinstestine_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getCNSDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("cns_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getEndocrineAndMetabolicDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("endocrine_and_metabolic_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getSepsisDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("sepsis_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getOphthalmologyDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("ophthalmology_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getENTAndSwallowDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("ent_and_swallow_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getHaematologyDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("haematology_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getRenalDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("renal_summery", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getGeneticDailySummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("genetic_summery", r.message);
				}
			}
		})
	},
});
