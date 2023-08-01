// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

// import time


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
		var startTime = new Date().getTime();
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getMotherMRD",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					// console.log(r.message);
					frm.set_value("mother_id", r.message);
				}
			}
		})
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
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getAllInvestigations",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("list_of_investigations", r.message);
				}
			}
		})
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getAllProcedures",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("procedures_done_during_the_stay", r.message);
				}
			}
		})

		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getAllDiagnosis",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("diagnosis_throughout_the_stay", r.message);
				}
			}
		})

		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.admission.admission.getSummery",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				// console.log("Hello", r.message)
				if(r.message) {
					var msg = JSON.parse(r.message);
					// console.log(msg);
					frm.set_value("date_of_admission", msg.doa);
					frm.set_value("gestational_age_at_admission", msg.gaa_v);
					frm.set_value("admission_weight", msg.admission_weight);
					frm.set_value("admission_length", msg.admission_length);
					frm.set_value("admission_ofc", msg.admission_ofc);
					frm.set_value("date_and_time_of_birth", msg.dob);
					
					// frm.refresh_fields();
				}
			}

		});
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getAntenatalHistory",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				// console.log("Hello", r.message)
				if(r.message) {
					// console.log(r.message);
					// var data = JSON.parse(r.message);
					// console.log(data);
					// frm.set_value("antenatal", Object.keys(data));
					frm.set_value("antenatal", (r.message));
				}
			}
		});
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.nicu_stay_outcomes.nicu_stay_outcomes.getAdmissionDetails",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				// console.log("Hello", r.message)
				if(r.message) {
					// var data = JSON.parse(r.message);
					// frm.set_value("admission_details", Object.keys(data));
					frm.set_value("admission_details", (r.message));
				}
			}
		});

		var endTime = new Date().getTime();
		console.log("Fetching data from NICU Stay Outcomes for baby: " + frm.doc.baby_id + " completed" + " in " + (endTime - startTime) + " ms");
	
	},
	"time_and_date_of_discharge": function(frm) {
		var startTime = new Date(frm.doc.date_of_admission)
		var endTime = new Date(frm.doc.time_and_date_of_discharge)
		var diff = endTime.getTime() - startTime.getTime();
		var ldays = diff / (1000 * 3600 * 24);
		ldays = Math.round(ldays);
		var ag = frm.doc.gestational_age_at_admission;
		ag = ag.split(" ");
		var gw = parseInt(ag[0]);
		var gd = parseInt(ag[2]);
		var gd = gw * 7 + gd;
		var days = ldays + gd; 
		// convert days to weeks
		var weeks = days / 7;
		weeks = Math.round(weeks);
		var day = days % 7;
		frm.set_value("length_of_hospital_stay", ldays);
		frm.set_value("gestational_age_at_discharge", weeks + " " + "weeks" + " " + day + " " + "days");
	},
	"time_and_date_of_death": function(frm) {
		var startTime = new Date(frm.doc.date_of_admission)
		var endTime = new Date(frm.doc.time_and_date_of_death)
		var diff = endTime.getTime() - startTime.getTime();
		var days = diff / (1000 * 3600 * 24);
		days = Math.round(days);
		frm.set_value("length_of_hospital_stay", days);
	}
});
