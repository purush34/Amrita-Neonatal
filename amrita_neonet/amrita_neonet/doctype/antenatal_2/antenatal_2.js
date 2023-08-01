// Copyright (c) 2023, ICTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Antenatal-2', {
	// refresh: function(frm) {

	// }
	/* 
	"sb_1",
  "hr_1",
  "c_1",
  "t_1",
  "r_1",
  "total_1",
  "five_min",
  "sb_5",
  "hr_5",
  "c_5",
  "t_5",
  "r_5",
  "total_5",
  "ten_min",
  "sb_10",
  "hr_10",
  "c_10",
  "t_10",
  "r_10",
  "total_10",
  "fifteen_min",
  "sb_15",
  "hr_15",
  "c_15",
  "t_15",
  "r_15",
  "total_15",
  "twenty_min",
  "sb_20",
  "hr_20",
  "c_20",
  "t_20",
  "r_20",
  "total_20",
	*/
	"calculate": function(frm) {
		var tot_1 = frm.doc.sb_1 + frm.doc.hr_1 + frm.doc.c_1 + frm.doc.t_1 + frm.doc.r_1;
		var tot_2 = frm.doc.sb_5 + frm.doc.hr_5 + frm.doc.c_5 + frm.doc.t_5 + frm.doc.r_5;
		var tot_3 = frm.doc.sb_10 + frm.doc.hr_10 + frm.doc.c_10 + frm.doc.t_10 + frm.doc.r_10;
		var tot_4 = frm.doc.sb_15 + frm.doc.hr_15 + frm.doc.c_15 + frm.doc.t_15 + frm.doc.r_15;
		var tot_5 = frm.doc.sb_20 + frm.doc.hr_20 + frm.doc.c_20 + frm.doc.t_20 + frm.doc.r_20;
		frm.set_value("total_1", tot_1);
		frm.set_value("total_5", tot_2);
		frm.set_value("total_10", tot_3);
		frm.set_value("total_15", tot_4);
		frm.set_value("total_20", tot_5);
		frm.refresh_field("total_1");
		frm.refresh_field("total_5");
		frm.refresh_field("total_10");
		frm.refresh_field("total_15");
		frm.refresh_field("total_20");
	},
  "date_and_time": function(frm){
    calcPROM(frm);
  },
  "duration_of_prom": function(frm){
    calcPROM(frm);
  },
});

function calcPROM(frm){
  if (!frm.doc.date_and_time || !frm.doc.duration_of_prom){
    return;
  }
  var date1 = new Date(frm.doc.date_and_time);
  var date2 = new Date(frm.doc.duration_of_prom);
  var hourDiff = date2 - date1; //in ms
  // var secDiff = hourDiff / 1000; //in s
  // var minDiff = hourDiff / 60 / 1000; //in minutes
  var hDiff = hourDiff / 3600 / 1000 / 24; //in hours
  frm.set_value("duration_in_days", hDiff);

}
