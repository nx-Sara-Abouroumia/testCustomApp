app_name = "unsal"
app_title = "Unsal"
app_publisher = "NextarpERPTeam"
app_description = "customizations"
app_email = "s.sbouroumia@nextarp.dev"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/unsal/css/unsal.css"
# app_include_js = "/assets/unsal/js/unsal.js"
doctype_list_js = {"Quotation" : "public/js/quotation.js"}

doctype_js = {
    "Sales Order" : "public/js/sales_order.js",
    "Project" : "public/js/project.js",
    "Purchase Order" : "public/js/purchase_order.js",
    }

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["dt", "in", [
                "Project User"
            ]]
        ]
    }
]




# include js, css files in header of web template
# web_include_css = "/assets/unsal/css/unsal.css"
# web_include_js = "/assets/unsal/js/unsal.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "unsal/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "unsal/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "unsal.utils.jinja_methods",
# 	"filters": "unsal.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "unsal.install.before_install"
# after_install = "unsal.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "unsal.uninstall.before_uninstall"
# after_uninstall = "unsal.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "unsal.utils.before_app_install"
# after_app_install = "unsal.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "unsal.utils.before_app_uninstall"
# after_app_uninstall = "unsal.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "unsal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"unsal.tasks.all"
# 	],
# 	"daily": [
# 		"unsal.tasks.daily"
# 	],
# 	"hourly": [
# 		"unsal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"unsal.tasks.weekly"
# 	],
# 	"monthly": [
# 		"unsal.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "unsal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "unsal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "unsal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["unsal.utils.before_request"]
# after_request = ["unsal.utils.after_request"]

# Job Events
# ----------
# before_job = ["unsal.utils.before_job"]
# after_job = ["unsal.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"unsal.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

