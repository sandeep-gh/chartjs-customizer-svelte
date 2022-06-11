import justpy as jp
import ofjustpy as oj



@jp.SetRoute('/customize_chartjs')
def wp_chartjs_customizer(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    with oj.sessionctx(session_manager):
        oj.Span_("aspan", text="i am a span")
        wp = oj.WebPage_("wp_chartjs_customizer", cgens=[stubStore.aspan], template_file='svelte.html', title="a svelte page")()
        wp.session_manager = session_manager
        #wp = jp.WebPage(template_file='svelte.html', title="a svelte page")
    return wp


app = jp.app
jp.justpy(wp_chartjs_customizer, start_server=False)
