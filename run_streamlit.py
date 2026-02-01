# -*- coding: utf-8 -*-
"""

@author: ST Mbelebele 208015035
"""

import subprocess

file = "app.py"
file = "app_plots.py"
file = "app_profiler.py"
#file = "app_profiler_menus.py"


subprocess.Popen(
    ["streamlit", "run", file], shell=True
)
