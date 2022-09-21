from addict import Dict
import ofjustpy as oj

from chartjs_customizer.attrmeta_basecfg import get_basecfg
from chartjs_customizer.cfgattr_uic import build_uic_iter
from chartjs_customizer.attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType
from chartjs_customizer.attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxisType
from chartjs_customizer.attrmeta_basecfg_helper import AxesType, PlotType

setupChoices = Dict()
setupChoices.plotType = PlotType.Line
setupChoices.axes.type = AxesType.cartesian
setupChoices.axises =  ['x', 'y'] #We have default cartesian axes 
cfgAttrMeta = get_basecfg(setupChoices)

for _ in oj.dictWalker(cfgAttrMeta):
    print (_[0])
    print ("--------------------------")

