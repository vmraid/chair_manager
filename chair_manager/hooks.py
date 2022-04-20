from . import __version__ as app_version

app_name = "chair_manager"
app_title = "Chair Manager"
app_publisher = "VMRaid"
app_description = "GUI for using chair commands "
app_icon = "fa fa-gamepad"
app_color = "grey"
app_email = "info@vmraid.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/chair_manager/css/chair_manager.css"
app_include_js = "/assets/chair_manager/js/chair_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/chair_manager/css/chair_manager.css"
# web_include_js = "/assets/chair_manager/js/chair_manager.js"

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
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "chair_manager.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "chair_manager.install.before_install"
# after_install = "chair_manager.install.after_install"

# Desk Notifications
# ------------------
# See vmraid.core.notifications.get_notification_config

# notification_config = "chair_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "vmraid.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "vmraid.desk.doctype.event.event.has_permission",
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
# 		"chair_manager.tasks.all"
# 	],
# 	"daily": [
# 		"chair_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"chair_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chair_manager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"chair_manager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "chair_manager.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"vmraid.desk.doctype.event.event.get_events": "chair_manager.event.get_events"
# }
