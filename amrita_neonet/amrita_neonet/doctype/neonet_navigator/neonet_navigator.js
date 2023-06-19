// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt
/* 
"opening_form",
  "admission",
  "maternal",
  "crib_ii_score",
  "snappe_ii",
  "navigator",
  "discharge",
  "discharge_examination",
  "discharge_checklist",
  "death_summary",
  "column_break_vxatl",
  "daily_summery",
  "respiratory",
  "cvs",
  "gi",
  "cns",
  "endocrine_and_metabollic",
  "sepsis",
  "opthalmology",
  "ent_and_swallow",
  "haematology",
  "renal",
  "genetic",
  "section_break_gmvir",
  "investigations",
  "nurosonogram",
  "ct",
  "mri",
  "electroencephalography",
  "uss_kub_abdomen",
  "blood_culture",
  "urineperitonealpleural_fluid",
  "echocardiography",
  "lumbar_puncture",
  "neogen",
  "genetic_investigation",
  "pcr",
  "swabs",
  "respiratory_secretions",
  "retinopathy_of_prematurity",
  "column_break_sry3q",
  "important_procedures",
  "umbilical_lines",
  "picc_lines",
  "subclavian_femoral_line",
  "peripheral_arterial_line",
  "pericardial_tab",
  "pleural_tab",
  "peritoneal_tab",
  "chest_drain",
  "peritoneal_drain",
  "surgical_operative_note",
  "catheterisation",
  "intubation",
  "ng_tube_insertion",
  "naso_pharyngeal_tube"
*/
/* 
GI - done
Endocrine - done
Nurosonogram - done
Lumbar puncture - done
Genetic in investigation - done
Respiratory secretions - done
Umbilical lines  - done
Peritoneal tab - done
Surgical operative note - done
Discharge-All
*/
frappe.ui.form.on('Neonet_Navigator', {
	// refresh: function(frm) {

	// }
	baby_id: function (frm) {
		// console.log(frm.doc.baby_id);
		frappe.call({
			method: "amrita_neonet.amrita_neonet.doctype.neonet_navigator.neonet_navigator.getMotherMrd",
			args: {
				"baby_id": frm.doc.baby_id,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("mother_mrd", r.message);
				}
			}
		})
	},
	opening_form: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Opening page", frm.doc.baby_id)
	},
	admission: function (frm) {
		// console.log("frm.doc.baby_id", frm.doc.baby_id);
		if(verifyID(frm)) return;
		frappe.set_route("Form", "Admission", frm.doc.baby_id)
	},
	maternal: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Maternal And Antenatal Details", frm.doc.baby_id)
	},
	respiratory: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Respiratory", frm.doc.baby_id)
	},
	cvs: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "CVS", frm.doc.baby_id)
	},
	gi: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Gastrointestinal", frm.doc.baby_id)
	},
	cns: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "CNS", frm.doc.baby_id)
	},
	endocrine_and_metabollic: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Endocrine and metabolic", frm.doc.baby_id)
	},
	sepsis: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Sepsis", frm.doc.baby_id)
	},
	opthalmology: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Opthalmology", frm.doc.baby_id)
	},
	ent_and_swallow: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "ENT and Swallow", frm.doc.baby_id)
	},
	haematology: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "haematology", frm.doc.baby_id)
	},
	renal: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "renal", frm.doc.baby_id)
	},
	genetic: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "genetic", frm.doc.baby_id)
	},
	crib_ii_score: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "CRIB score", frm.doc.baby_id)
	},
	snappe_ii: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Snappe II", frm.doc.baby_id)
	},
	investigations: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Investigations", frm.doc.baby_id)
	},
	nurosonogram: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Neurosonogram", frm.doc.baby_id)
	},
	ct: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "CT", frm.doc.baby_id)
	},
	mri: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "MRI", frm.doc.baby_id)
	},
	electroencephalography: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Electroencephalography", frm.doc.baby_id)
	},
	uss_kub_abdomen: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "USS KUB_Abdomen", frm.doc.baby_id)
	},
	blood_culture: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Blood Culture", frm.doc.baby_id)
	},
	urineperitonealpleural_fluid: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Urine_Peritoneal_Pleural fluid", frm.doc.baby_id)
	},
	echocardiography: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Echocardiography", frm.doc.baby_id)
	},
	limber_puncture: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Limber Puncture", frm.doc.baby_id)
	},
	neogen: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Neogen", frm.doc.baby_id)
	},
	genetic_investigation: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Genetic Tests", frm.doc.baby_id)
	},
	pcr: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "PCR", frm.doc.baby_id)
	},
	swabs: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Swabs", frm.doc.baby_id)
	},
	respiratory_secretions: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Respiratory secreations", frm.doc.baby_id)
	},
	retinopathy_of_prematurity: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Retinopathy of Prematurity", frm.doc.baby_id)
	},
	important_procedures: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Important Procedures", frm.doc.baby_id)
	},
	umbilical_lines: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Umbiilical lines", frm.doc.baby_id)
	},
	picc_lines: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "PICC Line", frm.doc.baby_id)
	},
	subclavian_femoral_line: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Subclavian_femoral line", frm.doc.baby_id)
	},
	peripheral_arterial_line: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Peripheral Arterial Line", frm.doc.baby_id)
	},
	pericardial_tab: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Pericardial tap", frm.doc.baby_id)
	},
	pleural_tab: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Pleural tap", frm.doc.baby_id)
	},
	peritoneal_tab: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Peritoneal tap", frm.doc.baby_id)
	},
	chest_drain: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Chest Drain", frm.doc.baby_id)
	},
	peritoneal_drain: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Peritoneal Drain", frm.doc.baby_id)
	},
	surgical_operative_note: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Surgical Operative Notes", frm.doc.baby_id)
	},
	catheterisation: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Catheterisation", frm.doc.baby_id)
	},
	intubation: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Intubation", frm.doc.baby_id)
	},
	ng_tube_insertion: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "NG Tube Insertion", frm.doc.baby_id)
	},
	naso_pharyngeal_tube: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Naso- Pharyngeal Tube", frm.doc.baby_id)
	},
	lumbar_puncture: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Lumbar puncture", frm.doc.baby_id)
	},
	cooling_documentation: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Cooling Documentation", frm.doc.baby_id)
	},
	cooling_criteria: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Cooling Criteria", frm.doc.baby_id)
	},
	nicu_outcomes: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "NICU Stay Outcomes", frm.doc.baby_id)
	},
	maternal: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Maternal details", frm.doc.baby_id)
	},
	antenatal_1: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Antenatal-1", frm.doc.baby_id)
	},
	antenatal_2: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Antenatal-2", frm.doc.baby_id)
	},
	discharge_examination: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Discharge Examination", frm.doc.baby_id)
	},
	discharge_checklist : function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Discharge Checklist", frm.doc.baby_id)
	},
	dermatology: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Dermotology", frm.doc.baby_id)
	},
	musculoskeletal: function (frm) {
		// console.log(frm.doc.baby_id);
        if(verifyID(frm)) return;
		frappe.set_route("Form", "Musculoskeletal", frm.doc.baby_id)
	},

	
});
function verifyID(frm) {
	if (frm.doc.baby_id.trim() == "") {
		frappe.msgprint("Please Enter Baby ID")
		return true;
	}
	frappe.open_in_new_tab = true;
	return false;
}