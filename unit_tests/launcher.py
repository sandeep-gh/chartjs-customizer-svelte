from tailwind_tags import twcc2hex
from addict import Dict
import logging
import os
if os:
    try:
        os.remove("launcher.log")
    except:
        pass

import sys
if sys:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="launcher.log",
                        level=logging.DEBUG, format=FORMAT)

from chartjs_customizer.wp_chartSetup  import wp_chartSetup
import justpy as jp
app = jp.app
jp.justpy(wp_chartSetup,  debug=True, start_server=False)
# request = Dict()
# request.session_id = "asession"
# wp_chartSetup(request)