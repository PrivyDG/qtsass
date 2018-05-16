# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Libsass importers."""

# Standard library imports
from __future__ import absolute_import
import os

# Local imports
from qtsass.conformers import scss_conform


def norm_path(*parts):
    return os.path.normpath(os.path.join(*parts))


def qss_importer(where):
    """
    Returns a function which conforms imported qss files to valid scss to be
    used as an importer for sass.compile.

    :param where: Directory containing scss, css, and sass files
    """

    def find_file(import_file):

        # Create partial import filename
        dirname, basename = os.path.split(import_file)
        if dirname:
            import_partial_file = '/'.join([dirname, '_' + basename])
        else:
            import_partial_file = '_' + basename

        # Build potential file paths for @import "import_file"
        potential_files = []
        for ext in ['', '.scss', '.css', '.sass']:
            full_name = import_file + ext
            partial_name = import_partial_file + ext
            potential_files.append(full_name)
            potential_files.append(partial_name)
            potential_files.append(norm_path(where, full_name))
            potential_files.append(norm_path(where, partial_name))

        # Return first existing potential file
        for potential_file in potential_files:
            if os.path.isfile(potential_file):
                return potential_file

        return None

    def import_and_conform_file(import_file):

        real_import_file = find_file(import_file)
        with open(real_import_file, 'r') as f:
            import_str = f.read()

        return [(import_file, scss_conform(import_str))]

    return import_and_conform_file
