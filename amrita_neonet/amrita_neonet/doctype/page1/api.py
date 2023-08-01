import frappe

@frappe.whitelist()
def say_hello():
	return "Hello"