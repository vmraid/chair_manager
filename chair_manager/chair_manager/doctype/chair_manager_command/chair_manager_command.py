# -*- coding: utf-8 -*-
# Copyright (c) 2017, VMRaid and contributors
# For license information, please see license.txt


from subprocess import PIPE, Popen, check_output

import vmraid
from vmraid.model.document import Document
from vmraid.model.naming import make_autoname


class ChairManagerCommand(Document):
	pass
