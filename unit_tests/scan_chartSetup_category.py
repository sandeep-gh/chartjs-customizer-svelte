
from addict import Dict
from chartjs_customizer.attrmeta_basecfg import get_basecfg
from chartjs_customizer.cfgattr_uic import build_uic_iter
from chartjs_customizer.attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType


cfgAttrMeta = get_basecfg(None)
chartSetupCfgUI_iter = build_uic_iter(
    filter(lambda _: _[1].group == uiorgCat.chartSetup, oj.dictWalker(cfgAttrMeta))
    )

request  = Dict()
request.session_id = "abc"
session_manager = oj.get_session_manager(request.session_id)
stubStore = session_manager.stubStore
with oj.sessionctx(session_manager):

    for _ in chartSetupCfgUI_iter :
        print (_)
