# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""
The SASS language brings countless amazing features to CSS.

Besides being used in web development, CSS is also the way to stylize Qt-based
desktop applications. However, Qt's CSS has a few variations that prevent the
direct use of SASS compiler.

The purpose of qtsass is to fill the gap between SASS and Qt-CSS by handling
those variations.
"""

# yapf: disable

from __future__ import absolute_import

# Standard library imports
import logging

# Local imports
from qtsass.api import (
    compile,
    compile_dirname,
    compile_filename,
    enable_logging,
    watch,
)


# yapf: enable

# Setup Logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
enable_logging()

# Constants
VERSION_INFO = (0, 1, 2, 'dev0')
__version__ = '.'.join(map(str, VERSION_INFO))
