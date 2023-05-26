// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gastrointestinal', {
	// refresh: function(frm) {

	// }
	go_back_to_cvs(frm){
		frm.save();
		frappe.set_route("Form", "CVS", frm.doc.name);
	},
	save_and_goto_cns(frm){
		frm.save();
		frappe.set_route("Form", "CNS", frm.doc.name);
	},
});
function total_calories(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	var calories = parseFloat(d.ebm_pre_term_calories) + parseFloat(d.ebm_term_calories) + parseFloat(d.no_of_fortifier_sachets_calories) + parseFloat(d.pre_term_formula_calories) + parseFloat(d.term_formula_calories) + parseFloat(d.neocate_calories) + parseFloat(d.sagar_calories) + parseFloat(d.mct_oil_calories) + parseFloat(d.beneprotien_calories);
	d.total_calories = (calories);

	var per_kilo = parseFloat(d.ebm_pre_term_per_kilo) + parseFloat(d.ebm_term_per_kilo) + parseFloat(d.no_of_fortifier_sachets_per_kilo) + parseFloat(d.pre_term_formula_per_kilo) + parseFloat(d.term_formula_per_kilo) + parseFloat(d.neocate_per_kilo) + parseFloat(d.sagar_per_kilo) + parseFloat(d.mct_oil_per_kilo) + parseFloat(d.beneprotien_per_kilo);
	d.total_per_kilo = (per_kilo);

	var protein = parseFloat(d.ebm_pre_term_protein) + parseFloat(d.ebm_term_protein_content) + parseFloat(d.no_of_fortifier_sachets_protein_content) + parseFloat(d.pre_term_formula_protein) + parseFloat(d.term_formula_protein_content) + parseFloat(d.neocate_protein_content) + parseFloat(d.sagar_protein_content) + parseFloat(d.beneprotien_protein_content);
	
	d.total_protein_content = (protein);
	d.feeds_and_supplement_kcals = per_kilo;
}
function avg_total_calories(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	var kcal = parseFloat(d.gir_kcal) + parseFloat(d.protein_kcal) + parseFloat(d.lipid_kcal) + parseFloat(d.feeds_and_supplement_kcals);
	d.total_kcal = (kcal);
}
frappe.ui.form.on('GI', {
	// refresh: function(frm) {

	// }
	/*
	"ebm_pre_term_ml",
	"ebm_term_mlday",
	"no_of_fortifier_sachets_mlday",
	"pre_term_formula_ml",
	"term_formula_mlday",
	"neocate_mlday",
	"sagar_mlday",
	"mct_oil_dropsday",
	"beneprotien_gmkgday"
	*/
	/*
	"ebm_pre_term_calories",
	"ebm_term_calories",
	"no_of_fortifier_sachets_calories",
	"pre_term_formula_calories",
	"term_formula_calories",
	"neocate_calories",
	"sagar_calories",
	"mct_oil_calories",
	"beneprotien_calories",
	"total_calories",
	*/
	/*
	"ebm_pre_term_per_kilo",
	"ebm_term_per_kilo",
	"no_of_fortifier_sachets_per_kilo",
	"pre_term_formula_per_kilo",
	"term_formula_per_kilo",
	"neocate_per_kilo",
	"sagar_per_kilo",
	"mct_oil_per_kilo",
	"beneprotien_per_kilo",
	"total_per_kilo",
	*/
	/*
	"ebm_pre_term_protein",
  "ebm_term_protein_content",
  "no_of_fortifier_sachets_protein_content",
  "pre_term_formula_protein",
  "term_formula_protein_content",
  "neocate_protein_content",
  "sagar_protein_content",
  "mct_oil_protein_content",
  "beneprotien_protein_content",
  "total_protein_content",
	*/
	ebm_pre_term_ml(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.67;
		var calories = d.ebm_pre_term_ml * k_cal;
		d.ebm_pre_term_calories = calories;
		var working_weight = d.working_weight;
		d.ebm_pre_term_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.016;
		d.ebm_pre_term_protein = d.ebm_pre_term_ml * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	ebm_term_mlday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.67;
		var calories = (d.ebm_term_mlday * k_cal);
		d.ebm_term_calories = calories;
		var working_weight = d.working_weight;
		d.ebm_term_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.011;
		d.ebm_term_protein_content = d.ebm_term_mlday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	no_of_fortifier_sachets_mlday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 3.5;
		var calories = d.no_of_fortifier_sachets_mlday * k_cal;
		d.no_of_fortifier_sachets_calories = calories;
		var working_weight = d.working_weight;
		d.no_of_fortifier_sachets_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.3;
		d.no_of_fortifier_sachets_protein_content = d.no_of_fortifier_sachets_mlday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	pre_term_formula_ml(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.792;
		var calories = d.pre_term_formula_ml * k_cal;
		d.pre_term_formula_calories = calories;
		var working_weight = d.working_weight;
		d.pre_term_formula_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.0267;
		d.pre_term_formula_protein = d.pre_term_formula_ml * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	term_formula_mlday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.67;
		var calories = d.term_formula_mlday * k_cal;
		d.term_formula_calories = calories;
		var working_weight = d.working_weight;
		d.term_formula_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.014;
		d.term_formula_protein_content = d.term_formula_mlday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	neocate_mlday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.67;
		var calories = d.neocate_mlday * k_cal;
		d.neocate_calories = calories;
		var working_weight = d.working_weight;
		d.neocate_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.0186;
		d.neocate_protein_content = d.neocate_mlday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	sagar_mlday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.32;
		var calories = d.sagar_mlday * k_cal;
		d.sagar_calories = calories;
		var working_weight = d.working_weight;
		d.sagar_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.03;
		d.sagar_protein_content = d.sagar_mlday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	mct_oil_dropsday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 0.5;
		var calories = d.mct_oil_dropsday * k_cal;
		d.mct_oil_calories = calories;
		var working_weight = d.working_weight;
		d.mct_oil_per_kilo = calories / parseFloat(working_weight);
		var protein = 0.00;
		d.mct_oil_protein_content = d.mct_oil_dropsday * protein;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	beneprotien_gmkgday(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var k_cal = 4;
		var working_weight = d.working_weight;
		var calories = d.beneprotien_gmkgday * k_cal * parseFloat(working_weight);
		d.beneprotien_calories = calories;
		d.beneprotien_per_kilo = calories / parseFloat(working_weight);
		var protein = 1;
		d.beneprotien_protein_content = d.beneprotien_gmkgday * protein * working_weight;
		total_calories(frm, cdt, cdn);
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	/* 
	"gir_mg",
  "protein_grams",
  "lipid_grams",
  "feeds_and_supplements",
  "column_break_m7tbj",
  "gir_kcal",
  "protein_kcal",
  "lipid_kcal",
  "feeds_and_supplement_kcals",
	*/
	gir_mg(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var working_weight = d.working_weight;
		var k_cal = 5.76* working_weight*d.gir_mg;
		d.gir_kcal = k_cal;
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	protein_grams(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var working_weight = d.working_weight;
		var k_cal = 4* working_weight*d.protein_grams;
		d.protein_kcal = k_cal;
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	lipid_grams(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var working_weight = d.working_weight;
		var k_cal = 9* working_weight*d.lipid_grams;
		d.lipid_kcal = k_cal;
		avg_total_calories(frm, cdt, cdn)
		frm.refresh_fields();

	},
	working_weight(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var ww = d.working_weight;
		if (ww>5){
			frappe.msgprint("Working weight should be less than 5");
			d.working_weight = 0;
			frm.refresh_fields();
		} 

	},

},
);
frappe.ui.form.on('GI', {
	"daily_observations_add": function(frm, cdt, cdn) {
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