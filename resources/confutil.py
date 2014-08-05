#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import codecs   # Encoding is a nightmare that never ends.
import re

def getConfig(path):
    """Returns a dictionary with the keys and values specified in a separate config file at [path]."""
    with open(path, 'r') as confile:
        configDict = {}
        lines = [l for l in confile if l.strip()]
        if lines[0].startswith(codecs.BOM_UTF8): ## Byte order markers sometimes are interpreted as characters
            lines[0] = lines[0][len(codecs.BOM_UTF8):]
        for line in lines:
            key, value = line.split("=")
            key, value = key.strip(), value.strip()
            configDict[key] = value
    return configDict

def getList(path):
    """Returns a list from a comma-separated list of values at [path]."""
    try:
        with open(path, 'r') as f:
            l = re.split(',\s*', f.read().strip())
        return l
    except IOError:
        return []

def strToBool(s):
    """Converts strings to booleans."""
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    return None
