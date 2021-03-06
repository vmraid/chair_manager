# Chair Manager
<img src="chair_manager/public/images/fa-gamepad.svg" width="250">

Chair Manager is a graphical user interface to emulate the functionalities of Frappé Chair. Like the command line utility it helps you install apps, manage multiple sites, update apps and much more.

## Installation

Create a new site called chair-manager.local and install Chair Manager on the site. 

### Automated (preferred)

```
$ chair setup manager
```
What all it does:
1. Create new site chair-manager.local
2. Gets the `chair_manager` app from https://github.com/vmraid/chair_manager if it doesn't exist already
3. Installs the chair_manager app on the site chair-manager.local

### Manual

```
$ chair new-site chair-manager.local
$ chair get-app chair_manager
$ chair --site chair-manager.local install-app chair_manager
```
## Update

In vmraid-chair directory execute:
```
$ chair update
```

## [Wiki](https://github.com/vmraid/chair_manager/wiki)

## Features

#### What can you do using this app ?
- Update chair
- Backup your sites
- Install/Uninstall apps on your site
- Restore Backups on either existing sites or new sites
- Create new apps and sites

#### App Catalogue

There are 5 main doctypes associated with this app. 


### 1. Chair Settings

- This is a single doctype whose main purpose is to peruse your chair instance and load all the necessary config onto the related doctypes such as App, Site and Site Backup.
- The Update button emulates the ``` chair update ``` command and updates all the installed apps.
- The Sync button does the following functions.
  - Reads your chair instance, greps and loads all the backups onto the Site Backup doctype.
  - Reads, greps and populates the Site doctype with all the existing sitse in the current chair instance.
  - Reads, greps and populates all the installed apps in the App doctype.
- The Chair setting doctype also displays all the config parameters in the common-site-config.json which is applicable to all 
  the sites in your chair instance.

### 2. Site

* The Site doctype shows a list of all the sites in the current chair instance.
* Inside each individual docname of the Site doctype one can find 3 clickable buttons.
  1. Migrate
      * This button emulates the ```chair migrate``` command.
      * It applies schema changes and data migrations if any.
      * Migrate should be run after you pull updates from any Frappé app.
  2. Backup Site 
      * This button backs up the site with all the files in it.
  3. Install App
      * On clicking this button a ui-dialog pops up where one can select and install any app onto the site.
  4. Uninstall App
      * Lets you uninstall an app from the site.
  5. Reinstall
      * Lets you reinstall a site.
  6. Drop Site
      * Lets you delete a site. The backup for the site is automatically taken.
  7. View Site
      * Lets you directly access the site. At the click of a button, a new-tab is opened in your browser opening the site.
  8. Create Alias
      * Create multiple sites all pointing to the same site, i.e. create multiple aliases for the site. 
      * This can also be considered as an alternative to renaming a site.
  9. Delete Alias
      * Delete the aliases created.

### 3. Site Backup

- This doctype contains a list of all the backups present in your chair instance (includes both existent and archived sites).
- Inside each individual docname one can find a Restore button.
- Clicking the Restore button pops up a ui-dialog.
- In this ui-dialog once chose whether to restore the backup either on an existing site or on a new site.

### 4. Chair Manager Command

- This doctype is basically a logger for all the commands run using this app.
- This doctype displays the source of the command ie. the doctype and docname from where the command originated.
- It also displays the date and time on which the command was executed.
- The status of the command can be one of 3 types (Success, Failed or Ongoing)
- Finally the console text field displays the log of the command.

### 5. App

- This doctype shows a list of all installed apps in the current chair instance, and their git information!

#### License

MIT
