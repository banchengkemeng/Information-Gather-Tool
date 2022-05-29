#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria

import sys,os

from pkg_resources import DistributionNotFound, VersionConflict
from lib.core.structures import AttributeDict
from lib.core.exceptions import FailedDependenciesInstallation
from lib.core.installation import check_dependencies, install_dependencies

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
    sys.exit(1)

try:
    check_dependencies()
except (DistributionNotFound, VersionConflict):
    option = input("Missing required dependencies to run.\n"
                   "Do you want dirsearch to automatically install them? [Y/n] ")

    if option.lower() == 'y':
        print("Installing required dependencies...")

        try:
            install_dependencies()
        except FailedDependenciesInstallation:
            print("Failed to install dirsearch dependencies, try doing it manually.")
            exit(1)
    else:
        exit(1)


def dirscan_run(url):
    from lib.core.options import options
    wordlist = os.path.dirname(__file__)+'\db\dicc.txt'
    config = os.path.dirname(__file__)+'default.conf'

    #直接配置参数的JSON就可以直接进行扫描
    options = AttributeDict({'urls': [f'{url}'], 'url_file': None, 'stdin_urls': None, 'cidr': None, 'raw_file': None, 'session_file': None, 'extensions': ['php', 'aspx', 'jsp', 'html', 'js'], 'exclude_extensions': [], 'force_extensions': False, 'config': config, 'wordlist': [wordlist], 'prefixes': {''}, 'suffixes': {''}, 'only_selected': None, 'no_extension': None, 'uppercase': False, 'lowercase': False, 'capitalization': False, 'threads_count': 25, 'recursive': False, 'deep_recursive': False, 'force_recursive': False, 'recursion_depth': 0, 'recursion_status_codes': {200,403,301}, 'scan_subdirs': [''], 'exclude_subdirs': ['%ff/', '.;/', '..;/', ';/', './', '../', '%2e/', '%2e%2e/'], 'include_status_codes': [200,403,301], 'exclude_status_codes': [], 'exclude_sizes': [], 'exclude_texts': [], 'exclude_regex': '', 'exclude_redirect': '', 'exclude_response': '', 'skip_on_status': [404,302], 'minimum_response_size': 0, 'maximum_response_size': 0, 'redirects_history': False, 'maxtime': 0,
'full_url': False, 'color': True, 'quiet': False, 'httpmethod': 'GET', 'data': None, 'data_file': None, 'headers': {}, 'header_file': '', 'follow_redirects': False, 'use_random_agents': True, 'auth': None, 'auth_type': None, 'useragent': '', 'cookie': '', 'timeout': 7.5, 'delay': 0.0, 'proxy': [], 'proxy_file': '',
'proxy_auth': None, 'replay_proxy': '', 'tor': None, 'scheme': None, 'maxrate': 0, 'max_retries': 1, 'ip': None, 'exit_on_error': False, 'output_file': None, 'output_format': 'plain', 'log_file': '', 'output_path': '', 'autosave_report': False})

    from lib.controller.controller import Controller

    if options["quiet"]:
        from lib.output.silent import Output
    else:
        from lib.output.verbose import Output

    output = Output(options["color"])

    return list(set(Controller(options, output).ulist))

if __name__ == "__main__":
    main()
