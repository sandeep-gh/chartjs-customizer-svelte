"""Build html/ui components for cjs config attributes
based on their types
"""
import logging
if logging:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


from typing import NamedTuple, Any
import ofjustpy as oj
import ofjustpy_react as ojr
import ofjustpy_extn as ojx
from tailwind_tags import bg, pink, jc, db, jc, mr, shdw, gray, blue
import traceback
#from . import attrmeta_utils

@ojr.CfgLoopRunner
def on_plotType_select(dbref, msg):
    '''
    plotType is special; scale configuration panel is updated on change in plot type
    '''
    #print("on_plotTypeSelect")
    #msg.page.update_scale_configurator(dbref, msg)
    #msg.page.update_ui_component(dbref, msg)  # in case there are other changes
    return "/type", msg.value


def reactor(dbref, msg):
    msg.page.update_ui_component(dbref, msg)

# def debugColorSelector(dbref, msg):
#     print("Debug ColorSelector ", dbref.key, " ", msg.value)


def no_action(dbref, msg):
    pass


def input_change(dbref, msg):
    pass


def update_chart(dbref, msg):
    #msg.page.react_ui(wf.ReactTag_UI.UpdateChart, None)
    assert False


def build_uic(key, label, attrMeta):
    """
    build uic generator from attr description
    """
    #pcp = [shdw.md, bg/gray/1]
    pcp = []
    if not attrMeta.active:
        pcp.append("hidden")
        logger.debug(f"now building ui:hidden for  {key} {attrMeta}  {pcp}")
    match str(attrMeta.vtype):
        case "<class 'int'>":

            match attrMeta.vrange:
                case type():
                    return oj.Halign_(oj.LabeledInput_(key,
                                                       label,
                                                       attrMeta.default, 
                                                       pcp=pcp).event_handle(oj.change,
                                                                             update_chart)
                                      )
                case[x, y]:
                    # return wf.Wrapdiv_(
                    #     wf.WithBanner_(
                    #         key,  wf.Slider_(key, range(
                    #             x, y), attrMeta.default, update_chart), label, pcp=pcp
                    #     ), [db.f, jc.center, mr/2]
                    # )
                    return oj.Halign_(oj.WithBanner_(key,
                                                     key,
                                                     oj.Slider_(key, range(x,y), pcp=[]).event_handle(oj.click, update_chart), pcp=[]
                                                     )
                                      )

                case _:
                    print("skipping ", key)
                    return None  # not handling multi-attribute ranges

        case "<class 'str'>":
            match attrMeta.vrange:
                case type():
                    return oj.LabeledInput_(key,  label, attrMeta.default, 
                                            pcp=pcp).event_handle(oj.change, update_chart)
                
                case[x, y]:
                    print("skipping str range ", key)
                    return None
                case _:
                    print("skipping str", key)
                    return None
        case "<class 'float'>":
            match attrMeta.vrange:
                case type():
                    # Put float type
                    return oj.LabeledInput_(key,  label, attrMeta.default, 
                                            pcp=pcp).event_handle(oj.change, update_chart)

                case[x, y]:
                    # TODO: check range
                    return oj.LabeledInput_(key,  label, attrMeta.default, 
                                            pcp=pcp).event_handle(oj.change, update_chart)


                case _:
                    logger.debug(f"skipping float: {key}")
                    return None

        case "<aenum 'Color'>":
            return oj.Halign_(
                oj.WithBanner_(key, key, oj.ColorSelector_(key).event_handle(oj.click, update_chart)))
        

        case "<class 'bool'>" | "<aenum 'FalseDict'>":
            return oj.Halign_(
                oj.Checkbox_(
                    key, key,  value=attrMeta.default).event_handle(oj.input, input_change)
                
            )

        case "<aenum 'Position'>" | "<aenum 'TextAlign'>" | "<aenum 'PointStyle'>" | "<aenum 'cubicInterpolationMode'>" | "<aenum 'LineJoinStyle'>":
            print("TODO: ui for  EnumType config not implement")
            # return wf.Wrapdiv_(
            #     wf.SelectorWBanner_(key, label,
            #                         options=[
            #                             _.value for _ in attrMeta.vtype],
            #                         values=[
            #                             _.value for _ in attrMeta.vtype],
            #                         default_idx=[
            #                             _.value for _ in attrMeta.vtype].index(attrMeta.default.value),

            #                         on_select=update_chart, pcp=pcp
            #                         )
            # )
            return ojx.EnumSelector_(key, attrMeta.vtype, label=key, on_select = input_change)

        # by design we don't allow plottype change to be interactive;plottype has to selected initially as is fixed
        # for rest of the lifecycle
        case  "<aenum 'PlotType'>":
               logger.debug("Build ui for plottype")
               return oj.Select_(key,
                                 [oj.Option_(str(_.value), text=str(_.value), value=str(_.value))
                                  for _ in attrMeta.vtype],
                                 #value=next(iter(attrMeta.vtype)).value,
                                 value=getattr(attrMeta.vtype, "Undef").value,
                                 pcp=pcp).event_handle(oj.change, on_plotType_select)
            # return wf.Wrapdiv_(
            #     wf.SelectorWBanner_(key, label,
            #                         options=[
            #                             _.value for _ in attrMeta.vtype],
            #                         values=[
            #                             _.value for _ in attrMeta.vtype],
            #                         default_idx=[
            #                             _.value for _ in attrMeta.vtype].index(attrMeta.default.value),

            #                         on_select=on_plotType_select, pcp=pcp
            #                         )
            # )

    logger.debug(f"Not building ui for:  {key}")
    return None


def build_uic_iter(attrMetaIter):
    """
    attrMeta:  describes a ui component
    attrMetaIter:  a sequence of attrMeta
    label: the label for the category

    """

    # this is the subsection heading
    # yield dur.wrapdiv_(label+"Wrap", dc.Span_(label, label, pcp=[bg/pink/1]))

    logger.debug("now building uic_iter")
    #logger.info('General exception noted.', exc_info=True)
    # for line in traceback.format_stack():
    #     logger.debug(line.strip())
    # logger.debug("end trace")

    def build_uic_wrapper(kpath, attrMeta):
        logger.debug(f"uic_iter {kpath}")
        _ = kpath.split("/")
        if _[-1] == "value":  # value is used for FalseDict type attrmeta
            del _[-1]
        #print ("in uic ", kpath)
        return build_uic(kpath, _[-2]+"/"+_[-1], attrMeta)
    yield from filter(lambda _: _ is not None,
                      map(lambda _: build_uic_wrapper(_[0], _[1]),
                          attrMetaIter)
                      )
    logger.debug("done building uic_iter for = ")
