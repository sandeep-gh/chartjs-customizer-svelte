import logging
if logging:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


import justpy as jp
import ofjustpy as oj
import ofjustpy_react as ojr
from .components_chartCustomizer import build_uigroup_blocks_

from addict import Dict
from . import actions
from ofjustpy.dpathutils import dget, dnew, dpop, stitch_from_dictiter
from .attrmeta_basecfg import get_basecfg
from .attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType
from .attrmeta_basecfg_helper import AxesType, PlotType, uiorgCat

import jsbeautifier
import json
from dpath.util import set as dset
from .chartcfg import (add_dataset, build_pltcfg, update_cfgattrmeta,
                       update_chartCfg)

# setupChoices = Dict()
# setupChoices.plotType = PlotType.Line
# setupChoices.axes.type = AxesType.cartesian #This happens because the plot type is 'Line/Bar/Bubble/Scatter'
# #setupChoices.axis.type = CartesianAxisType.linear
# setupChoices.axises =  ['x', 'y'] #We have cartesian axesj
# cfgAttrMeta = get_basecfg(setupChoices)

def init(appstate):
    """
    initialize everything before page load 
    """
    cfgAttrMeta = get_basecfg(appstate.chartSetup)
    opts = jsbeautifier.default_options()
    res = jsbeautifier.beautify(json.dumps(cfgAttrMeta, default=str), opts)
    #print (res)
    cjs_cfg = Dict(track_changes=True)
    update_chartCfg(cfgAttrMeta, cjs_cfg)
    cfgAttrMeta.clear_changed_history()
    res = jsbeautifier.beautify(json.dumps(cjs_cfg, default=str), opts)



    #cycle through 1 round of updates; chartcfg (from setup), cfgAttrMeta (from chartcfg) and back to chartcfg

    # TODO: this should be tied up to 
    dset(cjs_cfg, "/type", "line")
    add_dataset(cjs_cfg)
    dnew(cjs_cfg, "/data/labels", "[1,2,4,5,6,7]")
    update_cfgattrmeta(cjs_cfg, cfgAttrMeta)
    update_chartCfg(cfgAttrMeta, cjs_cfg)
    update_chartCfg(cfgAttrMeta, cjs_cfg)
    cfgAttrMeta.clear_changed_history()
    cjs_cfg.clear_changed_history()
    opts = jsbeautifier.default_options()
    logger.debug("cjs_cfg")
    logger.debug(jsbeautifier.beautify(json.dumps(cjs_cfg), opts))


# ========================= done update cycle ========================
ui_app_trmap_iter = [
    ]

def wp_chartCustomizer(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    appstate = session_manager.appstate
    appstate.cfgbase.type = None
    setupChoices = Dict()
    setupChoices.plotType = PlotType.Line
    setupChoices.axes.type = AxesType.cartesian #This happens because the plot type is 'Line/Bar/Bubble/Scatter'
    #jsetupChoices.axis.type = CartesianAxisType.linear
    
    setupChoices.axises =  ['x', 'y'] #We have default cartesian axes 
    appstate.cfgAttrMeta = get_basecfg(setupChoices)

    with oj.sessionctx(session_manager):
        #build_components(session_manager)

        # aspan_ = oj.Span_("aspan", text="dummy text"
        #          )
        cgens =  build_uigroup_blocks_(uiorgCat.all, appstate.cfgAttrMeta)
        #cgens = [stubStore.scaleCfg.lineplot.xyaxes._xaxes.panel]

        # ============ porting to ofjustpy react framework ===========
        
        wp = oj.WebPage_("wp_chartjs_customizer",
                         cgens= cgens,
                         WPtype=ojr.WebPage,
                         ui_app_trmap_iter = ui_app_trmap_iter,
                         session_manager = session_manager,
                         action_module = actions,
                         
                         template_file='svelte.html',
                         title="Customize chart using chart.js")()
        wp.session_manager = session_manager
        #wp = jp.WebPage(template_file='svelte.html', title="a svelte page")
    return wp



# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')
