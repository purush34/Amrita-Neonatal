// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt
const temperatureRanges = {
	"<= 29.6": 5,
	"29.7 to 31.2": 4,
	"31.3 to 32.8": 3,
	"32.9 to 34.4": 2,
	"34.5 to 36": 1,
	"36.1 to 37.5": '0',
	"37.6 to 39.1": 1,
	"39.2 to 40.7": 2,
	">=40.8": 3
};

const baseExcessValues = {
	'< -26': 7,
	'-26 to -23': 6,
	'-22 to -18': 5,
	'-17 to -13': 4,
	'-12 to -8': 3,
	'-7 to -3': 2,
	'-2 to 2': 1,
	'>= 3': '0'
};


frappe.ui.form.on('CRIB score', {
	// refresh: function(frm) {

	// }
	onload: function (frm) {
		if (frm.doc.gender.trim() == "Male") {
			frm.set_value("points", CalcRESULTM(frm));
		}
		else {
			frm.set_value("points", CalcRESULTF(frm));
		}
		var sum = 0;
		sum = parseInt(frm.doc.temp_points) + parseInt(frm.doc.base_points) + parseInt(frm.doc.points);
		frm.set_value("total_crib_ii_score", sum);
		var z = sum
		z = z * 0.45
		z = z - 6.476
		z = Math.exp(z) / (1 + Math.exp(z))
		z = Fmt(100 * z) + " %"
		frm.set_value("predicted_death_rate", z);
	},
	"gender": function (frm) {
		console.log(frm.doc.gender.trim() == "Male");
		if (frm.doc.gender.trim() == "Male") {
			frm.set_value("points", CalcRESULTM(frm));
		}
		else {
			frm.set_value("points", CalcRESULTF(frm));
		}
	},
	"temperature": function (frm) {
		frm.set_value("temp_points", temperatureRanges[frm.doc.temperature.trim()]);
	},
	"base_excess": function (frm) {
		frm.set_value("base_points", baseExcessValues[frm.doc.base_excess.trim()]);
	},
	"gestation": function (frm) {
		if (frm.doc.gender == "Male") {
			frm.set_value("points", CalcRESULTM(frm));
		}
		else {
			frm.set_value("points", CalcRESULTF(frm));
		}
	},
	"birthweight": function (frm) {
		if (frm.doc.gender == "Male") {
			frm.set_value("points", CalcRESULTM(frm));
		}
		else {
			frm.set_value("points", CalcRESULTF(frm));
		}
	},
	"calc": function (frm) {
		var sum = 0;
		sum = parseInt(frm.doc.temp_points) + parseInt(frm.doc.base_points) + parseInt(frm.doc.points);
		frm.set_value("total_crib_ii_score", sum);
		var z = sum
		z = z * 0.45
		z = z - 6.476
		z = Math.exp(z) / (1 + Math.exp(z))
		z = Fmt(100 * z) + " %"
		frm.set_value("predicted_death_rate", z);
	},

});
function Fmt(x) {
	var v
	if (x >= 0) { v = '' + (x + 0.05) } else { v = '' + (x - 0.05) } return v.substring(0, v.indexOf('.') + 2)
}

function CalcRESULTM(frm) {
	var t = parseFloat(frm.doc.birthweight);
	var finalresult = 0;
	var gestationfield = parseInt(frm.doc.gestation);
	if (t >= 1501 && gestationfield == 32) {
		finalresult = 0;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 32) {
		finalresult = 1;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 32) {
		finalresult = 3;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 32) {
		finalresult = 6;
	}
	if (t >= 2501 && gestationfield == 31) {
		finalresult = 1;
	}
	if (t >= 1751 && t <= 2500 && gestationfield == 31) {
		finalresult = 0;
	}
	if (t >= 1501 && t <= 1750 && gestationfield == 31) {
		finalresult = 1;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 31) {
		finalresult = 2;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 31) {
		finalresult = 3;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 31) {
		finalresult = 6;
	}
	if (t >= 501 && t <= 750 && gestationfield == 31) {
		finalresult = 8;
	}
	if (t >= 2251 && gestationfield == 30) {
		finalresult = 3;
	}
	if (t >= 2001 && t <= 2250 && gestationfield == 30) {
		finalresult = 2;
	}
	if (t >= 1751 && t <= 2000 && gestationfield == 30) {
		finalresult = 1;
	}
	if (t >= 1501 && t <= 1750 && gestationfield == 30) {
		finalresult = 2;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 30) {
		finalresult = 3;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 30) {
		finalresult = 4;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 30) {
		finalresult = 6;
	}
	if (t >= 501 && t <= 750 && gestationfield == 30) {
		finalresult = 8;
	}
	if (t >= 1251 && gestationfield == 29) {
		finalresult = 3;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 29) {
		finalresult = 5;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 29) {
		finalresult = 6;
	}
	if (t >= 501 && t <= 750 && gestationfield == 29) {
		finalresult = 8;
	}
	if (t >= 1251 && gestationfield == 28) {
		finalresult = 5;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 28) {
		finalresult = 6;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 28) {
		finalresult = 7;
	}
	if (t >= 501 && t <= 750 && gestationfield == 28) {
		finalresult = 8;
	}
	if (t >= 251 && t <= 500 && gestationfield == 28) {
		finalresult = 10;
	}
	if (t >= 1251 && gestationfield == 27) {
		finalresult = 6;
	}
	if (t >= 751 && t <= 1250 && gestationfield == 27) {
		finalresult = 7;
	}
	if (t >= 501 && t <= 750 && gestationfield == 27) {
		finalresult = 9;
	}
	if (t >= 251 && t <= 500 && gestationfield == 27) {
		finalresult = 10;
	}
	if (t >= 751 && gestationfield == 26) {
		finalresult = 8;
	}
	if (t >= 501 && t <= 750 && gestationfield == 26) {
		finalresult = 10;
	}
	if (t >= 251 && t <= 500 && gestationfield == 26) {
		finalresult = 11;
	}
	if (t >= 1001 && gestationfield == 25) {
		finalresult = 9;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 25) {
		finalresult = 10;
	}
	if (t >= 501 && t <= 750 && gestationfield == 25) {
		finalresult = 11;
	}
	if (t >= 251 && t <= 500 && gestationfield == 25) {
		finalresult = 12;
	}
	if (t >= 1001 && gestationfield == 24) {
		finalresult = 10;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 24) {
		finalresult = 11;
	}
	if (t >= 501 && t <= 750 && gestationfield == 24) {
		finalresult = 12;
	}
	if (t >= 251 && t <= 500 && gestationfield == 24) {
		finalresult = 13;
	}
	if (t >= 751 && gestationfield == 23) {
		finalresult = 12;
	}
	if (t >= 501 && t <= 750 && gestationfield == 23) {
		finalresult = 13;
	}
	if (t >= 251 && t <= 500 && gestationfield == 23) {
		finalresult = 14;
	}
	if (t >= 501 && gestationfield == 22) {
		finalresult = 14;
	}
	if (t >= 251 && t <= 500 && gestationfield == 22) {
		finalresult = 15;
	}
	return finalresult;
}

function CalcRESULTF(frm) {
	var t = parseFloat(frm.doc.birthweight);
	var finalresult = 0;
	var gestationfield = parseInt(frm.doc.gestation);
	if (t >= 1501 && gestationfield == 32) {
		finalresult = 0;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 32) {
		finalresult = 1;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 32) {
		finalresult = 3;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 32) {
		finalresult = 5;
	}
	if (t >= 2501 && gestationfield == 31) {
		finalresult = 1;
	}
	if (t >= 1501 && t <= 2500 && gestationfield == 31) {
		finalresult = 0;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 31) {
		finalresult = 1;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 31) {
		finalresult = 3;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 31) {
		finalresult = 5;
	}
	if (t >= 501 && t <= 750 && gestationfield == 31) {
		finalresult = 7;
	}
	if (t >= 2251 && gestationfield == 30) {
		finalresult = 2;
	}
	if (t >= 1501 && t <= 2250 && gestationfield == 30) {
		finalresult = 1;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 30) {
		finalresult = 2;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 30) {
		finalresult = 3;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 30) {
		finalresult = 5;
	}
	if (t >= 501 && t <= 750 && gestationfield == 30) {
		finalresult = 7;
	}
	if (t >= 1251 && gestationfield == 29) {
		finalresult = 3;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 29) {
		finalresult = 4;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 29) {
		finalresult = 5;
	}
	if (t >= 501 && t <= 750 && gestationfield == 29) {
		finalresult = 7;
	}
	if (t >= 1251 && gestationfield == 28) {
		finalresult = 4;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 28) {
		finalresult = 5;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 28) {
		finalresult = 6;
	}
	if (t >= 501 && t <= 750 && gestationfield == 28) {
		finalresult = 8;
	}
	if (t >= 251 && t <= 500 && gestationfield == 28) {
		finalresult = 10;
	}
	if (t >= 1501 && gestationfield == 27) {
		finalresult = 6;
	}
	if (t >= 1251 && t <= 1500 && gestationfield == 27) {
		finalresult = 5;
	}
	if (t >= 1001 && t <= 1250 && gestationfield == 27) {
		finalresult = 6;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 27) {
		finalresult = 7;
	}
	if (t >= 501 && t <= 750 && gestationfield == 27) {
		finalresult = 8;
	}
	if (t >= 251 && t <= 500 && gestationfield == 27) {
		finalresult = 10;
	}
	if (t >= 1001 && gestationfield == 26) {
		finalresult = 7;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 26) {
		finalresult = 8;
	}
	if (t >= 501 && t <= 750 && gestationfield == 26) {
		finalresult = 9;
	}
	if (t >= 251 && t <= 500 && gestationfield == 26) {
		finalresult = 10;
	}
	if (t >= 1001 && gestationfield == 25) {
		finalresult = 8;
	}
	if (t >= 751 && t <= 1000 && gestationfield == 25) {
		finalresult = 9;
	}
	if (t >= 501 && t <= 750 && gestationfield == 25) {
		finalresult = 10;
	}
	if (t >= 251 && t <= 500 && gestationfield == 25) {
		finalresult = 11;
	}
	if (t >= 751 && gestationfield == 24) {
		finalresult = 10;
	}
	if (t >= 501 && t <= 750 && gestationfield == 24) {
		finalresult = 11;
	}
	if (t >= 251 && t <= 500 && gestationfield == 24) {
		finalresult = 12;
	}
	if (t >= 751 && gestationfield == 23) {
		finalresult = 11;
	}
	if (t >= 501 && t <= 750 && gestationfield == 23) {
		finalresult = 12;
	}
	if (t >= 251 && t <= 500 && gestationfield == 23) {
		finalresult = 13;
	}
	if (t >= 501 && gestationfield == 22) {
		finalresult = 13;
	}
	if (t >= 251 && t <= 500 && gestationfield == 22) {
		finalresult = 14;
	}
	return finalresult;
}

