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

    
from tailwind_tags import twcc2hex
from addict import Dict

import ofjustpy as oj

#from chartjs_customizer import components_chartCustomizer    
from chartjs_customizer.wp_chartSetup  import wp_chartSetup as primary_endpoint
from chartjs_customizer.wp_chartCustomizer  import wp_chartCustomizer 

import justpy as jp
#from chartjs_customizer import wp_chartCustomizer
app = jp.build_app()
#app = jp.app
#jp.Route("/", primary_endpoint)
app.add_jproute("/", wp_chartCustomizer)
# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')




#app = jp.app
# jp.justpy(wp_chartSetup,  debug=True, start_server=False)
# request = Dict()
# request.session_id = "asession"
# wp = wp_chartCustomizer(request)

# stubStore = wp.session_manager.stubStore
# cfg_stub = stubStore['/options/scales/x/axis']
# msg = Dict()
# msg.value = "new-axis-title"
# msg.page = wp
# cfg_stub.target.on_change(msg)
# plottype_stub = stubStore.chartSetup['/type']
# msg = Dict()
# msg.page = wp
# msg.value = 'line'
# plottype_stub.target.on_change(msg)


# # from here track react-pipeline for update_chart
