import justpy as jp
import ofjustpy as oj
import ofjustpy_react as ojr
from .components_chartSetup import build_components
from . import actions
import ofjustpy_react as ojr
from .attrmeta_basecfg import get_basecfg

#, lambda _: f"/scaleCfg/deckpanel/{_}" 
ui_app_kmap = [
    ("/type", "/cfgbase/type", lambda _: f"/scaleCfg/deckpanel/{_}"),
    ("/chartSetup", "/chartSetup", None)
    ]

def wp_chartSetup(request):
    print ("wp_chartSetup INVOKED .......................................")
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    appstate = session_manager.appstate
    appstate.cfgAttrMeta = get_basecfg(None)
    appstate.cfgbase.type = None
    with oj.sessionctx(session_manager):
        build_components(session_manager)
        # aspan_ = oj.Span_("aspan", text="dummy text",
        #                   reactctx = [ojr.Ctx("/cfgbase/type", ojr.isstr, ojr.UIOps.UPDATE_TEXT)]
        #          )

        #@ojr.CfgLoopRunner
        def on_redirectbtn_click(dbref, msg):
            stubStore.wp_chartSetup.target.redirect = "/chartCustomizer"
            return 
        oj.Button_("rdbtn", text="Redirect").event_handle(oj.click, on_redirectbtn_click)
        cgens = [stubStore.chartSetup.topPanel,
                 stubStore.scaleCfg.deckpanel.panel_scalecfg_allplottypes,
                 stubStore.rdbtn
                 ]
        #cgens = [stubStore.scaleCfg.lineplot.xyaxes._xaxes.panel]

        # ============ porting to ofjustpy react framework ===========
        
        wp = oj.WebPage_("wp_chartSetup",
                         cgens= cgens,
                         WPtype=ojr.WebPage,
                         ui_app_trmap_iter = ui_app_kmap,
                         session_manager = session_manager,
                         action_module = actions,
                         
                         template_file='svelte.html',
                         reactctx = [ojr.Ctx("/chartSetup", ojr.isstr, ojr.UIOps.REDIRECT)],
                         title="Customize chart using chart.js")()
        wp.session_manager = session_manager
        # def page_ready(dbref, msg):
        #     print ("page is ready")
        # wp.redirect = "/chartCustomizer"
        # wp.on("page_ready", page_ready)
        #wp = jp.WebPage(template_file='svelte.html', title="a svelte page")
    return wp

# app = jp.app
# jp.Route("/", wp_chartSetup)


