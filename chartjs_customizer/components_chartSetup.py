import jsbeautifier
import json

import ofjustpy as oj
import ofjustpy_extn as ojx
import ofjustpy_react as ojr

from .attrmeta_basecfg_helper import uiorgCat, FalseDict, CartesianAxesType
from .attrmeta_basecfg import get_basecfg
from .cfgattr_uic import build_uic_iter

opts = jsbeautifier.default_options()
cfgAttrMeta = get_basecfg()
#UI element for chartSetupConfig
chartSetupCfgUI_iter = build_uic_iter(
    filter(lambda _: _[1].group == uiorgCat.chartSetup, oj.dictWalker(cfgAttrMeta))
    )

def build_components(session_manager):
    
    appstate = session_manager.appstate
    with session_manager.uictx("chartSetup") as chartSetupCtx:
        _ictx = chartSetupCtx
        def on_submitbtn_click(dbref, msg):
            print("go on...build the chart")
        oj.Subsection_("uipanel", "Chart Setup Configs",
                       oj.StackW_("uibox", cgens=chartSetupCfgUI_iter)
                       )
        # oj.Button_(
        #     "SubmitBtn",  text="Submit", value="Build Chart").event_handle(oj.click, on_submitbtn_click)
            
        #submit_ = oj.Halign_(_ictx.SubmitBtn)
        #oj.StackV_("topPanel", cgens=[_ictx.uipanel, submit_])
        oj.StackV_("topPanel", cgens=[_ictx.uipanel])        


    # ======= scale selection/configuration based on plot type =======
    with session_manager.uictx("scaleCfg") as scaleCfgCtx:
        with session_manager.uictx("lineplot") as linePlotCtx:
            with session_manager.uictx("xyaxes") as xyaxesCtx:
                with session_manager.uictx("_xaxes")as _xctx:
                    with session_manager.uictx("_x") as _xxctx:
                        def set_x(dbref, msg):
                            print("set choices to use default x")
                        oj.StackH_("card",
                                   cgens=[oj.Button_(
                                       "set",
                                       value="x",
                                       text="use the default x-axis").event_handle(oj.click, set_x)
                                          ]
                                   )
                    with session_manager.uictx("_xaxes") as _xaxesctx:
                        _ctx = _xaxesctx

                        oj.LabeledInput_("id", label="axes id", placeholder="new id")
                        ojx.EnumSelector_(
                            "axestype", CartesianAxesType, "Choose Axes Type")

                        # def on_addaxesbtn_click(dbref, msg):
                        #     _lctx.scalesNoticeboard.showText("added new axes")
                        oj.Button_("addaxesbtn", value="newid", label="add axes")
                        # oj.StackH_(
                        #     "card",
                        #     cgens=[oj.StackV_("newaxes", cgens=[_ctx.id, _ctx.axestype]), _ctx.addaxesbtn])

                        oj.StackH_(
                            "card",
                            cgens=[oj.StackV_("newaxes", cgens=[_ctx.id]), _ctx.addaxesbtn])
                                                
                    def deck_card_selector(dbref, msg):
                        print("deck selector called :", msg.value)
                        _xctx.deck.target.bring_to_front(msg.value)

                    oj.StackD_("deck", cgens=[_xxctx.card, _xaxesctx.card])
                    oj.Button_(
                        "xbtn", value=_xaxesctx.card.spath, text="X").event_handle(oj.click, deck_card_selector)
                    oj.Button_(
                        "xaxesbtn", value=_xxctx.card.spath, text="XAxes").event_handle(oj.click, deck_card_selector)
                    oj.StackV_("panel", cgens=[oj.StackH_("btns", cgens=[_xctx.xbtn, _xctx.xaxesbtn]),
                                                                                                                                           _xctx.deck])
                    oj.Subsection_("section", "Configure X scales", _xctx.panel)

        with session_manager.uictx("deckpanel") as deckCtx:
            oj.StackD_("panel_scalecfg_allplottypes",
                       cgens = [
                           oj.Span_("None", text="Select plot type to enable scale configuration"),
                           oj.Span_("line", text="Show config option for line plot"),
                           oj.Span_("bar", text="Show config option for bar plot"),
                           oj.Span_("scatter", text="Show config option for bar plot"),                           
                           oj.Span_("bubble", text="Show config option for radial plot"),
                           oj.Span_("polar", text="Show config option for polar plot")

                       ],
                       reactctx = [ojr.Ctx("/cfgbase/type", ojr.isstr, ojr.UIOps.DECK_SHUFFLE)]
                       )
