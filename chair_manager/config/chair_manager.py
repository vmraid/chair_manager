from vmraid import _


def get_data():
	chair_setup = {
		"label": _("Chair Setup"),
		"icon": "octicon octicon-briefcase",
		"items": [
			{
				"name": "App",
				"type": "doctype",
				"label": _("App"),
				"description": _("VMRaid Apps"),
			},
			{
				"name": "Site",
				"type": "doctype",
				"label": _("Site"),
				"description": _("Chair Sites"),
			},
		],
	}

	chair_management = {
		"label": _("Chair Management"),
		"type": "module",
		"items": [
			{
				"name": "Site Backup",
				"type": "doctype",
				"label": _("Site Backup"),
				"description": _("Site Backup"),
			},
			{
				"name": "Chair Manager Command",
				"type": "doctype",
				"label": _("Chair Manager Command"),
				"description": _("Chair Manager Command"),
			},
			{
				"name": "Chair Settings",
				"type": "doctype",
				"label": _("Chair Settings"),
				"description": _("Chair Settings"),
			},
		],
	}

	return [chair_setup, chair_management]
