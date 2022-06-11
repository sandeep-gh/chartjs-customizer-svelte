import justpy as jp
import ofjustpy as oj

from .components_chartSetup import build_components

@jp.SetRoute('/customize_chartjs')
def wp_chartSetup(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    with oj.sessionctx(session_manager):
        oj.Span_("aspan", text="i am a span")
        build_components(session_manager)
        print("DDD+ ", stubStore.scaleCfg.lineplot.xyaxes._xaxes.section)
        #cgens = [stubStore.chartSetup.topPanel, stubStore.scaleCfg.lineplot.xyaxes._xaxes.section]
        cgens = [stubStore.scaleCfg.lineplot.xyaxes._xaxes.panel]
        
        wp = oj.WebPage_("wp_chartjs_customizer",
                         cgens= cgens,
                         template_file='svelte.html',
                         title="a svelte page")()
        wp.session_manager = session_manager
        #wp = jp.WebPage(template_file='svelte.html', title="a svelte page")
    return wp


