import justpy as jp
import ofjustpy as oj
import ofjustpy_react as ojr
from .components_chartSetup import build_components
from . import actions

ui_app_trmap_iter = [
    ("/type", "/cfgbase/type", lambda _: f"/scaleCfg/deckpanel/{_}" )
    ]
@jp.SetRoute('/customize_chartjs')
def wp_chartSetup(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    appstate = session_manager.appstate
    appstate.cfgbase.type = None
    with oj.sessionctx(session_manager):
        build_components(session_manager)
        # aspan_ = oj.Span_("aspan", text="dummy text",
        #                   reactctx = [ojr.Ctx("/cfgbase/type", ojr.isstr, ojr.UIOps.UPDATE_TEXT)]
        #          )
        cgens = [stubStore.chartSetup.topPanel,
                 stubStore.scaleCfg.deckpanel.panel_scalecfg_allplottypes]
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


