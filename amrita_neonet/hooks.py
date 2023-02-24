from . import __version__ as app_version

app_name = "amrita_neonet"
app_title = "Amrita Neonet"
app_publisher = "ICTS"
app_description = "Preemie db"
app_email = "nicu@aims.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amrita_neonet/css/amrita_neonet.css"
# app_include_js = "/assets/amrita_neonet/js/amrita_neonet.js"

# include js, css files in header of web template
# web_include_css = "/assets/amrita_neonet/css/amrita_neonet.css"
# web_include_js = "/assets/amrita_neonet/js/amrita_neonet.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amrita_neonet/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "amrita_neonet.utils.jinja_methods",
#	"filters": "amrita_neonet.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "amrita_neonet.install.before_install"
# after_install = "amrita_neonet.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "amrita_neonet.uninstall.before_uninstall"
# after_uninstall = "amrita_neonet.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amrita_neonet.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"amrita_neonet.tasks.all"
#	],
#	"daily": [
#		"amrita_neonet.tasks.daily"
#	],
#	"hourly": [
#		"amrita_neonet.tasks.hourly"
#	],
#	"weekly": [
#		"amrita_neonet.tasks.weekly"
#	],
#	"monthly": [
#		"amrita_neonet.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "amrita_neonet.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "amrita_neonet.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "amrita_neonet.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["amrita_neonet.utils.before_request"]
# after_request = ["amrita_neonet.utils.after_request"]

# Job Events
# ----------
# before_job = ["amrita_neonet.utils.before_job"]
# after_job = ["amrita_neonet.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"amrita_neonet.auth.validate"
# ]
