// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

const mbpMap = {
	">= 30 mmHg": '0',
	"20 - 29 mmHg": 9,
	"< 20 mmHg": 19
};
const tempValues = {
	"> 96 °F": '0',
	"95 - 96 °F": 8,
	"< 95 ° F": 15,
	"> 35.6 °C": '0',
	"35 - 35.6 °C": 8,
	"< 35 °C": 15
};
const poValues = {
	"> 2.49": '0',
	"1.0 - 2.49": 5,
	"0.3 - 0.99": 16,
	"< 0.3": 28
};
const phValues = {
	">= 7.20": '0',
	"7.10 - 7.19": 7,
	"< 7.10": 16
};
const seiValues = {
	"Yes": 19,
	"No": '0'
};

const uriValues = {
	">= 1": "0",
	"0.1 - 0.9": 5,
	"< 0.1": 18
}
const apgMap = {
	 ">= 7":"0",
	 "< 7" : "18",
};
const birMap = {
	">= 1000 g": '0',
	"750 - 999 g": 10,
	"< 750 g": 17
};
const smaValues = {
	"> 3rd %": '0',
	"< 3rd %": 12
};

const rd_values = {
	"0": "0",
	"22": 320,
	"23": 380,
	"24": 430,
	"25": 500,
	"26": 580,
	"27": 670,
	"28": 740,
	"29": 820,
	"30": 920,
	"31": 1030,
	"32": 1140,
	"33": 1280,
	"34": 1420,
	"35": 1580,
	"36": 1750,
	"37": 1920,
	"38": 2120,
	"39": 2350,
	"40": 2520,
	"41": 2660,
	">41": 2750
};


frappe.ui.form.on('Snappe II', {
	// refresh: function(frm) {

	// }
	onload: function (frm) {
		frm.set_value("mean_bp", mbpMap[frm.doc.mean_blood_pressure.trim()]);
		frm.set_value("low_temp", tempValues[frm.doc.lowest_temperature.trim()]);
		frm.set_value("po2", poValues[frm.doc.p02_mmhg___fio2_.trim()]);
		frm.set_value("low_serum", phValues[frm.doc.lowest_serum_ph.trim()]);
		frm.set_value("seizures", seiValues[frm.doc.multiple_seizures.trim()]);
		frm.set_value("urine", uriValues[frm.doc.urine_output.trim()]);
		frm.set_value("apgar", apgMap[frm.doc.apgar_score.trim()]);
		frm.set_value("birthweight", birMap[frm.doc.birth_weight.trim()]);
		frm.set_value("small_ges_age", smaValues[frm.doc.small_for_gestational_age.trim()]);
		frm.set_value("gaw_s", rd_values[frm.doc.gaw.trim()]);
		calculateScore(frm);
	},
	"mean_blood_pressure": function (frm) {
		frm.set_value("mean_bp", mbpMap[frm.doc.mean_blood_pressure.trim()]);
		calculateScore(frm);
	},
	"lowest_temperature": function (frm) {
		frm.set_value("low_temp", tempValues[frm.doc.lowest_temperature.trim()]);
		calculateScore(frm);
	},
	"p02_mmhg___fio2_": function (frm) {
		frm.set_value("po2", poValues[frm.doc.p02_mmhg___fio2_.trim()]);
		calculateScore(frm);
	},
	"lowest_serum_ph": function (frm) {
		frm.set_value("low_serum", phValues[frm.doc.lowest_serum_ph.trim()]);
		calculateScore(frm);
	},
	"multiple_seizures": function (frm) {
		frm.set_value("seizures", seiValues[frm.doc.multiple_seizures.trim()]);
		calculateScore(frm);
	},
	"urine_output_mlkgh": function (frm) {
		frm.set_value("urine", uriValues[frm.doc.urine_output_mlkgh.trim()]);
		calculateScore(frm);
	},
	"apgar_score": function (frm) {
		frm.set_value("apgar", apgMap[frm.doc.apgar_score.trim()]);
		calculateScore(frm);
	},
	"birth_weight": function (frm) {
		frm.set_value("birthweight", birMap[frm.doc.birth_weight.trim()]);
		calculateScore(frm);
	},
	"small_for_gestational_age": function (frm) {
		frm.set_value("small_ges_age", smaValues[frm.doc.small_for_gestational_age.trim()]);
		calculateScore(frm);
	},
	"gaw": function (frm) {
		frm.set_value("gaw_s", rd_values[frm.doc.gaw.trim()]);
		// calculateScore(frm);
	}

});

function calculateScore(frm) {
	var snapSum = parseInt(frm.doc.mean_bp) + parseInt(frm.doc.low_temp) + parseInt(frm.doc.po2) + parseInt(frm.doc.low_serum) + parseInt(frm.doc.seizures) + parseInt(frm.doc.urine);

	var snapSumTotal = parseInt(frm.doc.mean_bp) + parseInt(frm.doc.low_temp) + parseInt(frm.doc.po2) + parseInt(frm.doc.low_serum) + parseInt(frm.doc.seizures) + parseInt(frm.doc.urine) + parseInt(frm.doc.apgar) + parseInt(frm.doc.birthweight) + parseInt(frm.doc.small_ges_age);

	frm.set_value("snap_ii", snapSum+"");
	frm.set_value("snappe_ii", snapSumTotal+"");
}