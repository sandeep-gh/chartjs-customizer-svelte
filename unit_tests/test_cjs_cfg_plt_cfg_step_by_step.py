import jsbeautifier
import json

from addict import Dict
import ofjustpy as oj

from chartjs_customizer.attrmeta_basecfg import get_basecfg
from chartjs_customizer.cfgattr_uic import build_uic_iter
from chartjs_customizer.attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType
from chartjs_customizer.attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType
from chartjs_customizer.attrmeta_basecfg_helper import AxesType, PlotType

from chartjs_customizer.chartcfg import (add_dataset, build_pltcfg, update_cfgattrmeta,
                                         update_chartCfg, build_pltcfg)

setupChoices = Dict()
setupChoices.plotType = PlotType.Line
setupChoices.axes.type = AxesType.cartesian
setupChoices.axises =  ['x', 'y'] #We have default cartesian axes 
cfgAttrMeta = get_basecfg(setupChoices)

opts = jsbeautifier.default_options()
res = jsbeautifier.beautify(json.dumps(cfgAttrMeta, default=str), opts)
cjs_cfg = Dict(track_changes=True)
update_chartCfg(cfgAttrMeta, cjs_cfg)
cfgAttrMeta.clear_changed_history()
opts = jsbeautifier.default_options()

cjs_plt_cfg = build_pltcfg(cjs_cfg)
#res = jsbeautifier.beautify(json.dumps(cjs_plt_cfg, default=str), opts)
#print(res)

# post cjs_cfg initialization
# testing update
import pickle
with open("cjs_cfg.pickle", "wb") as fh:
    pickle.dump(cjs_cfg, fh)
    
print (oj.dget(cjs_cfg, "/options/scales/x/ticks/display"))


ui_app_kmap = [(_[0], _[0], None) for _ in oj.dictWalker(cfgAttrMeta)
    ]

print (ui_app_kmap)


# for _ in oj.dictWalker(cfgAttrMeta):
#     print (_[0])
#     print ("--------------------------")


    
