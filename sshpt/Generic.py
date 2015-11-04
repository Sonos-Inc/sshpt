#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Copyright 2011 Dan McDougall <YouKnowWho@YouKnowWhat.com>
#       Copyright 2015 Jonghak Choi <haginara@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; Version 3 of the License
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, the license can be downloaded here:
#
#       http://www.gnu.org/licenses/gpl.html

import re
import threading


### ---- Private Functions ----
def normalizeString(string):
    """Removes/fixes leading/trailing newlines/whitespace and escapes double quotes with double quotes (to comply with CSV format)"""
    string = re.sub(r'(\r\n|\r|\n)', '\n', string) # Convert all newlines to unix newlines
    string = string.strip() # Remove leading/trailing whitespace/blank lines
    srting = re.sub(r'(")', '""', string) # Convert double quotes to double double quotes (e.g. 'foo "bar" blah' becomes 'foo ""bar"" blah')
    return string


class GenericThread(threading.Thread):
    """A baseline thread that includes the functions we want for all our threads so we don't have to duplicate code."""
    def quit(self):
        self.quitting = True
