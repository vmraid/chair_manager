# -*- coding: utf-8 -*-
# Copyright (c) 2017, VMRaid and contributors
# For license information, please see license.txt


import json
import os
import shlex
import time
from subprocess import PIPE, Popen, check_output

import vmraid
from chair_manager.chair_manager.utils import (
	safe_decode,
	verify_whitelisted_call,
)
from vmraid.model.document import Document


class ChairSettings(Document):
	site_config_fields = [
		"background_workers",
		"shallow_clone",
		"admin_password",
		"auto_email_id",
		"auto_update",
		"vmraid_user",
		"global_help_setup",
		"dropbox_access_key",
		"dropbox_secret_key",
		"gunicorn_workers",
		"github_username",
		"github_password",
		"mail_login",
		"mail_password",
		"mail_port",
		"mail_server",
		"use_tls",
		"rebase_on_pull",
		"redis_cache",
		"redis_queue",
		"redis_socketio",
		"restart_supervisor_on_update",
		"root_password",
		"serve_default_site",
		"socketio_port",
		"update_chair_on_update",
		"webserver_port",
		"file_watcher_port",
	]

	def set_attr(self, varname, varval):
		return setattr(self, varname, varval)

	def validate(self):
		self.sync_site_config()
		self.update_git_details()
		current_time = vmraid.utils.time.time()
		if current_time - self.last_sync_timestamp > 10 * 60:
			sync_all(in_background=True)

	def sync_site_config(self):
		common_site_config_path = "common_site_config.json"
		with open(common_site_config_path, "r") as f:
			common_site_config_data = json.load(f)
			for site_config_field in self.site_config_fields:
				try:
					self.set_attr(site_config_field, common_site_config_data[site_config_field])
				except:
					pass

	def update_git_details(self):
		self.vmraid_git_branch = safe_decode(
			check_output(
				"git rev-parse --abbrev-ref HEAD".split(), cwd=os.path.join("..", "apps", "vmraid")
			)
		).strip("\n")

	@vmraid.whitelist()
	def console_command(self, key, caller, app_name=None, branch_name=None):
		commands = {
			"chair_update": ["chair update"],
			"switch_branch": [""],
			"get-app": ["chair get-app {app_name}".format(app_name=app_name)],
		}
		vmraid.enqueue(
			"chair_manager.chair_manager.utils.run_command",
			commands=commands[caller],
			doctype=self.doctype,
			key=key,
			docname=self.name,
		)


@vmraid.whitelist()
def sync_sites():
	verify_whitelisted_call()
	site_dirs = update_site_list()
	site_entries = [x["name"] for x in vmraid.get_all("Site")]
	create_sites = list(set(site_dirs) - set(site_entries))
	delete_sites = list(set(site_entries) - set(site_dirs))

	for site in create_sites:
		doc = vmraid.get_doc({"doctype": "Site", "site_name": site, "developer_flag": 1})
		doc.insert()
		vmraid.db.commit()

	for site in delete_sites:
		doc = vmraid.get_doc("Site", site)
		doc.developer_flag = 1
		doc.save()
		doc.delete()
		vmraid.db.commit()
	# vmraid.msgprint('Sync sites completed')


@vmraid.whitelist()
def sync_apps():
	verify_whitelisted_call()
	app_dirs = update_app_list()
	app_entries = [x["name"] for x in vmraid.get_all("App")]
	create_apps = list(set(app_dirs) - set(app_entries))
	delete_apps = list(set(app_entries) - set(app_dirs))
	create_apps = [app for app in create_apps if app != ""]
	delete_apps = [app for app in delete_apps if app != ""]

	for app in create_apps:
		doc = vmraid.get_doc(
			{
				"doctype": "App",
				"app_name": app,
				"app_description": "lorem ipsum",
				"app_publisher": "lorem ipsum",
				"app_email": "lorem ipsum",
				"developer_flag": 1,
			}
		)
		doc.insert()
		vmraid.db.commit()

	for app in delete_apps:
		doc = vmraid.get_doc("App", app)
		doc.developer_flag = 1
		doc.save()
		doc.delete()
		vmraid.db.commit()
	# vmraid.msgprint('Sync apps completed')


def update_app_list():
	app_list_file = "apps.txt"
	with open(app_list_file, "r") as f:
		apps = f.read().split("\n")
	return apps


def update_site_list():
	site_list = []
	for root, dirs, files in os.walk(".", topdown=True):
		for name in files:
			if name == "site_config.json":
				site_list.append(str(root).strip("./"))
				break
	if "" in site_list:
		site_list.remove("")
	return site_list


@vmraid.whitelist()
def sync_backups():
	verify_whitelisted_call()
	backup_dirs_data = update_backup_list()
	backup_entries = [x["name"] for x in vmraid.get_all("Site Backup")]
	backup_dirs = [
		x["date"] + " " + x["time"] + " " + x["site_name"] + " " + x["stored_location"]
		for x in backup_dirs_data
	]
	create_backups = list(set(backup_dirs) - set(backup_entries))
	delete_backups = list(set(backup_entries) - set(backup_dirs))

	for date_time_sitename_loc in create_backups:
		date_time_sitename_loc = date_time_sitename_loc.split(" ")
		backup = {}
		for x in backup_dirs_data:
			if (
				x["date"] == date_time_sitename_loc[0]
				and x["time"] == date_time_sitename_loc[1]
				and x["site_name"] == date_time_sitename_loc[2]
				and x["stored_location"] == date_time_sitename_loc[3]
			):
				backup = x
				break
		doc = vmraid.get_doc(
			{
				"doctype": "Site Backup",
				"site_name": backup["site_name"],
				"date": backup["date"],
				"time": backup["time"],
				"stored_location": backup["stored_location"],
				"public_file_backup": backup["public_file_backup"],
				"private_file_backup": backup["private_file_backup"],
				"hash": backup["hash"],
				"file_path": backup["file_path"],
				"developer_flag": 1,
			}
		)
		doc.insert()
		vmraid.db.commit()

	for backup in delete_backups:
		doc = vmraid.get_doc("Site Backup", backup)
		doc.developer_flag = 1
		doc.save()
		vmraid.db.commit()
		doc.delete()
		vmraid.db.commit()
	# vmraid.msgprint('Sync backups completed')


def update_backup_list():
	all_sites = []
	archived_sites = []
	sites = []
	for root, dirs, files in os.walk("../archived_sites/", topdown=True):
		archived_sites.extend(dirs)
		break
	archived_sites = ["../archived_sites/" + x for x in archived_sites]
	all_sites.extend(archived_sites)
	for root, dirs, files in os.walk("../sites/", topdown=True):
		for site in dirs:
			if os.path.isfile("../sites/{}/site_config.json".format(site)):
				sites.append(site)
		break
	sites = ["../sites/" + x for x in sites]
	all_sites.extend(sites)

	response = []

	backups = []
	for site in all_sites:
		backup_path = os.path.join(site, "private", "backups")
		try:
			backup_files = (
				safe_decode(
					check_output(shlex.split("ls ./{backup_path}".format(backup_path=backup_path)))
				)
				.strip("\n")
				.split("\n")
			)
			backup_files = [file for file in backup_files if "database.sql" in file]
			for backup_file in backup_files:
				inner_response = {}
				date_time_hash = backup_file.rsplit("_", 1)[0]
				file_path = backup_path + "/" + date_time_hash
				inner_response["site_name"] = site.split("/")[2]
				inner_response["date"] = get_date(date_time_hash)
				inner_response["time"] = get_time(date_time_hash)
				inner_response["stored_location"] = site.split("/")[1]
				inner_response["private_file_backup"] = os.path.isfile(
					backup_path + "/" + date_time_hash + "_private_files.tar"
				)
				inner_response["public_file_backup"] = os.path.isfile(
					backup_path + "/" + date_time_hash + "_files.tar"
				)
				inner_response["hash"] = get_hash(date_time_hash)
				inner_response["file_path"] = file_path[3:]
				response.append(inner_response)
		except:
			pass
			# vmraid.msgprint('There are no backups to sync!')
	return response


def get_date(date_time_hash):
	return date_time_hash[:4] + "-" + date_time_hash[4:6] + "-" + date_time_hash[6:8]


def get_time(date_time_hash):
	time = date_time_hash.split("_")[1]
	return time[0:2] + ":" + time[2:4] + ":" + time[4:6]


def get_hash(date_time_hash):
	return date_time_hash.split("_")[2]


@vmraid.whitelist()
def sync_all(in_background=False):
	if not in_background:
		vmraid.msgprint("Sync has started and will run in the background...")
	verify_whitelisted_call()
	vmraid.enqueue(
		"chair_manager.chair_manager.doctype.chair_settings.chair_settings.sync_sites"
	)
	vmraid.enqueue(
		"chair_manager.chair_manager.doctype.chair_settings.chair_settings.sync_apps"
	)
	vmraid.enqueue(
		"chair_manager.chair_manager.doctype.chair_settings.chair_settings.sync_backups"
	)
	vmraid.set_value(
		"Chair Settings", None, "last_sync_timestamp", vmraid.utils.time.time()
	)
