// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Respiratory', {
// 	// refresh: function(frm) {

// 	// }
// });
// console.log("Hello");
// frappe.ui.form.on('Respiratory', {
// 	// cdt is Child DocType name i.e Quotation Item
// 	// cdn is the row name for e.g bbfcb8da6a
// 	Respiratory_child(frm, cdt, cdn) {

// 		console.log("Hello I am in the child");
// 		let row = frappe.get_doc(cdt, cdn);
// 		console.log(row);
// 	}
// })
// frappe.ui.form.on("Respiratory_child", {
// 	"date": function (frm, cdt, cdn) {
// 		var child = locals[cdt][cdn];
// 		console.log("Date changed to: " + child.date);
// 	}
// });

frappe.ui.form.on('Respiratory_child', {
	// cdt is Child DocType name i.e Quotation Item
	// cdn is the row name for e.g bbfcb8da6a
	date(frm, cdt, cdn) {
		// let row = frappe.get_doc(cdt, cdn);
		console.log(frm);
		console.log("Hello I am in the child");
		console.log(cdt,cdn);
		var child_table = frm.fields_dict.daily_observations.grid.grid_rows;
		// In for loop find the row index of the current row in doc.name
		var ind = -1;
		for (let index = 0; index < child_table.length; index++) {
			if (child_table[index].doc.name == cdn) {
				ind = index;
				break;
			}			
		}
		console.log(ind);

		
	},
	o2c_m(frm, cdt, cdn) {
		calc_maximum_oxidatio(frm, cdt, cdn);
	},
	o2c_o2(frm, cdt, cdn) {
		calc_maximum_oxidatio(frm, cdt, cdn);
	},
	o2c_pa(frm, cdt, cdn) {
		calc_maximum_oxidatio(frm, cdt, cdn);
	},
	o2_24(frm, cdt, cdn) {
		frm.refresh_fields();
	},
	started(frm, cdt, cdn) {
		calc_duration(frm, cdt, cdn);
	},
	stopped(frm, cdt, cdn) {
		calc_duration(frm, cdt, cdn);
	},
	"size": function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		console.log("Size changed to: " + child.size);
		if (child.size >5) {
			frappe.msgprint("Size is greater than 5");
			child.size = -1;
			frm.refresh_fields();
		}
	}
})

function calc_maximum_oxidatio(frm, cdt, cdn) {
	let row = frappe.get_doc(cdt, cdn);
	var child_table = frm.fields_dict.daily_observations.grid.grid_rows;
	var ind = -1;
	for (let index = 0; index < child_table.length; index++) {
		if (child_table[index].doc.name == cdn) {
			ind = index;
			break;
		}
	}
	// console.log(ind);
	var map = parseFloat(frm.doc.daily_observations[ind].o2c_m);
	var o2 = parseFloat(frm.doc.daily_observations[ind].o2c_o2);
	var pao = parseFloat(frm.doc.daily_observations[ind].o2c_pa);
	// OI= % O2 * MeanAirwayPressure (cm of H20/ PaO2 (mmHG)
	// 1kPA= 7.5mmHg
	console.log(map);
	console.log(o2);
	console.log(pao);
	var result = (o2 * map) / pao;
	// console.log(result);
	frm.doc.daily_observations[ind].highest_o2 = result;
	frm.refresh_fields();
}

function calc_duration(frm,cdt,cdn){
	let row = frappe.get_doc(cdt, cdn);
	var child_table = frm.fields_dict.daily_observations.grid.grid_rows;
	var ind = -1;
	for (let index = 0; index < child_table.length; index++) {
		if (child_table[index].doc.name == cdn) {
			ind = index;
			break;
		}
	}
	// console.log(ind);
	var start = frm.doc.daily_observations[ind].started;
	var end = frm.doc.daily_observations[ind].stopped;
	// '2023-04-14 11:43:46'
	// caliculate the difference between the two times and return the difference in minutes even id days are different
	var start_date = new Date(start);
	var end_date = new Date(end);
	var duration = (end_date - start_date) / 1000 / 60;
	// console.log(duration);
	// round the duration to 2 decimal places
	duration = Math.round(duration * 100) / 100;
	frm.doc.daily_observations[ind].duration = duration;
	frm.refresh_fields();
}