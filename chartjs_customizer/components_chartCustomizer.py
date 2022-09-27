import logging

import os
if os:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
from addict import Dict
from itertools import chain
import jsbeautifier
import json


import ofjustpy as oj
import ofjustpy_extn as ojx
import ofjustpy_react as ojr

#from .cfgattr_uic import build_uic_iter
from .cfgattr_uic_kv import build_uic_iter
from .chartcfg import build_pltcfg
from .attrmeta_basecfg import get_basecfg
from .attrmeta_basecfg_helper import is_visible
from .attrmeta_basecfg_helper import uiorgCat, PlotType
from .attrmeta_basecfg_helper import AxesType, PlotType
from tailwind_tags import space, y
top_level_group = ["options/elements",
                   "options/plugins", "options/scales", "data"]
tier1_level_group = {"options/elements": ["line", "point"],
                     'options/plugins': ['legend'],
                     'options/scales': ['x', 'y'],
                     "data": ['datasets/0', 'datasets/1', 'datasets/2', 'datasets/3', 'datasets/4']}


def build_uigroup_blocks_(grouptag: str,   cfgattrmeta: Dict):
    """Builds a panel containing ui elements for cfgattributes in cfgattrmeta belonging
    to grouptag.
    ui_elemts are stacked in grid/auto-flow.  
    """

    # if user has specified multiple axes make groups for each one
    #tier1_level_group['options/scales'].append("x1")

    def group_iter():
        """    iterator over attrmeta belonging to cfggroup
        """
        def is_in_group(kpath, attrmeta):
            """
            does attrmeta at kpath belongs to grouptag. check attrmeta.grouptag
            for now using all. 
            """
            # if "/data/datasets" not in kpath:
            #     logger.debug(f"{kpath} is in group {grouptag}")
            #     return True  # for testing-- using all attributes
            return True
            # if attrmeta.group == grouptag:              #     return True
            # return False
        yield from filter(lambda _: is_in_group(_[0], _[1]),
                          filter(lambda _: is_visible(_[1]),
                                 oj.dictWalker(cfgattrmeta)
                                 )
                          )
    # ======================= end cfggroup_iter ======================
    
    def subgroup_iter(tlkey, tier1key=None):
        """
                tlkey/tier1key: defines a subgroup
                all cfg items in the subgroup
        """

        if tier1key is None:
            tier1keys = tier1_level_group[tlkey]
        else:
            tier1keys = [tier1key]

        def is_in_subgroup(kpath):
            """
            check if kpath belongs to group defined by tlkey/tier1key
            """
            if tlkey in kpath:
                res = len([True for _ in tier1keys if _ in kpath])
                if tier1key is None:
                    if res == 0:
                        logger.debug(f"{kpath} belongs to {tlkey}/{tier1key}")
                        return True
                    else:
                        return False  # kpath belongs to subcategory
                else:
                    if res > 0:
                        logger.debug(f"{kpath} belongs to {tlkey}/{tier1key}")
                        return True
                    else:
                        return False

        yield from filter(lambda _: is_in_subgroup(_[0]), group_iter())

    def build_ui_panel(tlkey, subkey=None):
        return oj.StackV_(tlkey, cgens = build_uic_iter(subgroup_iter(
                              tlkey, subkey)),
                          pcp=[space/y/2])
        # return oj.StackG_(tlkey, num_cols=2,
        #                   cgens=build_uic_iter(subgroup_iter(
        #                       tlkey, subkey),  # all cfgattr that come under options but not under elements or scales
        #                   )
        #                   )
           
    top_level_ui = Dict([(_, build_ui_panel(_)) for _ in top_level_group])
    tier1_level_ui = Dict()
    for tlkey in top_level_group:
        for subkey in tier1_level_group[tlkey]:
            subpanel_ = oj.Subsubsection_(
                f"{tlkey}_{subkey}",  f"{tlkey}/{subkey}", build_ui_panel(tlkey, subkey))
            tier1_level_ui[tlkey][subkey] = subpanel_

    def cfgblks_iter():
        for tlkey, tlui in top_level_ui.items():
            content_ = oj.StackV_(f"{tlkey}content",
                                  cgens=[tlui, oj.StackV_("subgroup", cgens=tier1_level_ui[tlkey].values())]
                                  )  # all the attr-uic for top level group k
            yield oj.Subsection_(f"{tlkey}panel", tlkey,  content_)

    return cfgblks_iter()

# ============================ for testing ===========================
# setupChoices = Dict()
# setupChoices.plotType = PlotType.Line
# setupChoices.axes.type = AxesType.cartesian #This happens because the plot type is 'Line/Bar/Bubble/Scatter'
# #setupChoices.axes.x.type = CartesianAxisType.linear 
    
# setupChoices.axises =  ['x', 'y'] #We have default cartesian axes 
# cfgAttrMeta = get_basecfg(setupChoices)
# grouptag = uiorgCat.all
# request = Dict()
# request.session_id = "abc"
# session_manager = oj.get_session_manager(request.session_id)
# with oj.sessionctx(session_manager):
#     ui_comptree = [_ for _  in build_uigroup_blocks_(grouptag, cfgAttrMeta)]

# ================================ end ===============================
