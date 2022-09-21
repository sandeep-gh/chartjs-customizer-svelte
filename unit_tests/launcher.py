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

#from chartjs_customizer import components_chartCustomizer    
from chartjs_customizer.wp_chartSetup  import wp_chartSetup as primary_endpoint
from chartjs_customizer.wp_chartCustomizer  import wp_chartCustomizer 

import justpy as jp
#from chartjs_customizer import wp_chartCustomizer
app = jp.app
#jp.Route("/", primary_endpoint)
jp.Route("/", wp_chartCustomizer)
# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')




# app = jp.app
# jp.justpy(wp_chartSetup,  debug=True, start_server=False)
# request = Dict()
# request.session_id = "asession"
# wp = wp_chartSetup(request)
# stubStore = wp.session_manager.stubStore
# print (stubStore.scaleCfg.deckpanel.keys())
# plottype_stub = stubStore.chartSetup['/type']
# msg = Dict()
# msg.page = wp
# msg.value = 'line'
# plottype_stub.target.on_change(msg)
