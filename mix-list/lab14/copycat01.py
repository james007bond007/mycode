#!/usr/bin/env python3

import shutil, os

os.chdir('/home/student/mycode/mix-list/lab14')

shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

shutil.copytree('5g_research/', '5g_research_backup/')


