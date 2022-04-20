from vmraid import _


def get_data():
	return {
		"transactions": [
			{"label": _("Sites and Apps"), "items": ["Site", "App"]},
			{"label": _("Backups and Logs"), "items": ["Site Backup", "Chair Manager Command"]},
		]
	}
