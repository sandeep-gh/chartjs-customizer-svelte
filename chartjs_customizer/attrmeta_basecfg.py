import logging
if logging:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

from typing import NamedTuple, Any
from addict import Dict, walker as dictWalker
from aenum import Enum, auto
from dpath.util import get as dget, set as dset, new as dnew, delete as dpop
# from justpy_chartjs.tags.style_values import Align, Position
# from justpy_chartjs.tags.style_values import Axis
#import webapp_framework as wf
import tailwind_tags as twt
from tailwind_tags import color2hex as hexify

from .attrmeta_basecfg_helper import AttrMeta, PlotType, uiorgCat, Color, BorderCapStyle, LineJoinStyle, CubicInterpolationMode, TextAlign, PointStyle,  Position

from .attrmeta_basecfg_helper import AxesType
all_context = [('*', '*')]


def OptionsElementsLineCfg(_cfg):

    _cfg.tension = AttrMeta(0, float, [0, 1], uiorgCat.advanced, True, [
        ('/type', 'line')])

    _cfg.backgroundColor = AttrMeta(
        twt.gray/1, Color, Color, uiorgCat.simple, True, [('/type', 'line')])
    _cfg.borderWidth = AttrMeta(
        2, int, [0, 5], uiorgCat.simple, True, [('/type', 'line')])
    _cfg.borderColor = AttrMeta(
        twt.gray/2, Color, Color, uiorgCat.simple,  True, [('/type', 'line')])
    _cfg.borderCapStyle = AttrMeta(
        BorderCapStyle.butt, BorderCapStyle, BorderCapStyle, uiorgCat.nitpick, True, [('/type', 'line')])

    # TODO: handle this later; require idea of segment
    #     segments
    # An Array of numbers that specify distances to alternately draw a line and a gap (in coordinate space units). If the number of elements in the array is odd, the elements of the array get copied and concatenated. For example, [5, 15, 25] will become [5, 15, 25, 5, 15, 25]. If the array is empty, the line dash list is cleared and line strokes return to being solid.
    _cfg.borderDash = AttrMeta([], None, None, uiorgCat.TBD,
                               False, [('/type', 'line')])
    _cfg.borderDashOffset = AttrMeta(
        0.0, float, float, uiorgCat.nitpick, True, [('/type', 'line')])
    _cfg.borderJoinStyle = AttrMeta(
        LineJoinStyle.miter, LineJoinStyle, LineJoinStyle, uiorgCat.nitpick, True, [('/type', 'line')])
    _cfg.capBezierPoints = AttrMeta(
        True, bool, bool, uiorgCat.advanced, False, [('/type', 'line')])
    _cfg.cubicInterpolationMode = AttrMeta(
        CubicInterpolationMode.default, CubicInterpolationMode, CubicInterpolationMode, uiorgCat.advanced, True, [('/type', 'line')])
    _cfg.fill = AttrMeta(None, None, None, uiorgCat.TBD,
                         False, [('/type', 'line')])  # TODO: bool/string
    _cfg.stepped = AttrMeta(False, bool, bool, uiorgCat.simple,
                            False, [('/type', 'line')])


def OptionsPluginsLegend(_cfg):
    _cfg.display = AttrMeta(
        True, bool, bool, uiorgCat.simple, True, all_context)

    _cfg.position = AttrMeta(
        Position.top, Position, Position, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.align = AttrMeta(
        TextAlign.center, TextAlign, TextAlign, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.maxHeight = AttrMeta(
        20, int, int, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.maxWidth = AttrMeta(
        80, int, int, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.fullSize = AttrMeta(
        False, bool, bool, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.reverse = AttrMeta(
        False, bool, bool, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.rtl = AttrMeta(
        False, bool, bool, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])


def OptionsPluginsLegendLabels(_cfg):

    _cfg.boxWidth = AttrMeta(
        40, int, int, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])
    _cfg.boxHeight = AttrMeta(
        12, int, int, uiorgCat.simple, True,  [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])
    _cfg.color = AttrMeta(
        twt.blue/5, Color, Color, uiorgCat.simple, False, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    # TODO: labels.fond

    _cfg.padding = AttrMeta(
        40, int, int, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    # TODO: filter, sort
    _cfg.usePointStyle = AttrMeta(
        False, bool, bool, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])

    _cfg.pointStyle = AttrMeta(PointStyle.circle,   PointStyle, PointStyle, uiorgCat.simple, True, [
        ('/options/plugins/legend/labels/usePointStyle', True), ('/options/plugins/legend/labels/usePointStyle', False)])

    _cfg.textAlign = AttrMeta(
        TextAlign.center, TextAlign, TextAlign, uiorgCat.simple, False, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])


def OptionsPluginsLegendTitle(_cfg):
    _cfg.display = AttrMeta(
        True, bool, bool, uiorgCat.simple, True, [('/options/plugins/legend/display', True), ('/options/plugins/legend/display', False)])  # TODO: fix bug adict changed during iteration;

    # _cfg.color = AttrMeta(
    #     twt.blue/5, Color, Color, uiorgCat.simple, True, [('/options/plugins/legend/title/display', True), ('/options/plugins/legend/title/display', False)])
    # # # TODO:font
    # _cfg.paddding = AttrMeta(
    #     0, int, int, uiorgCat.simple, True,  [('/options/plugins/legend/title/display', True), ('/options/plugins/legend/title/display', False)])

    # _cfg.text = AttrMeta(
    #     "legend_title", str, str, uiorgCat.simple, False, [('/options/plugins/legend/title/display', True), ('/options/plugins/legend/title/display', False)])
    pass
def AxisCfgOptions(_cfg):
    """
    options common to all axes
    """

    _ = _cfg
    #_.type = AttrMeta('linear',?? , uiorgCat.advanced) #TODO:  ?? <- CartesianAxisType or globalAxisType
    _.alignToPixels = AttrMeta(False, bool, bool, uiorgCat.TBD, False, [])
    _.backgroundColor = AttrMeta("", Color, Color, uiorgCat.simple, False,[])
    #TBD: padding
    _.display = AttrMeta(True, bool, bool, uiorgCat.simple, True, [])
    _.min = AttrMeta(None, int, int, uiorgCat.config, False, [])
    _.max = AttrMeta(None, int, int, uiorgCat.config, False, [])
    _.reversed = AttrMeta(False, bool, bool, uiorgCat.TBD, False,[])
    # should the data be scaled
    _.stacked = AttrMeta(False, bool, bool, uiorgCat.config, False,[])
    _.suggestedMax = AttrMeta(None, int, int, uiorgCat.TBD, False, [])
    _.suggestedMin = AttrMeta(None, int, int, uiorgCat.TBD, False, [])
    # move away from chart area
    _.weight = AttrMeta(0, int, int, uiorgCat.TBD, False, [])

def AxisTitleCfgOptions(_cfg):
    _ = _cfg
    _.display = AttrMeta(True, bool, bool, uiorgCat.simple, False,[])
    _cfg.align = AttrMeta(TextAlign.center,
                          TextAlign,
                          TextAlign,
                          uiorgCat.simple,
                          True,
                          [
                              ('/options/plugins/legend/display', True),
                              ('/options/plugins/legend/display', False)
                          ]
                          )
    _.text	= AttrMeta("axes-title", str, str, uiorgCat.simple, True,
                           [
                               ('/options/plugins/legend/display', True),
                               ('/options/plugins/legend/display', False)
                           ])
    _.color = AttrMeta("",
                       Color,
                       Color,
                       uiorgCat.nitpick,
                       False,
                       [
                           ('/options/plugins/legend/display', True),
                           ('/options/plugins/legend/display', False)
                       ])
    #_.font
    _.padding = AttrMeta(
        2, int, [0, 5], uiorgCat.nitpick, False, [])  # padding for label backdrop
    
def CartesianAxisCfgOption(_cfg):
    _ = _cfg
    _.bounds	= AttrMeta("axis_bounds", str, str, uiorgCat.simple, False, [])
    #_.position = TODO: string or object
    _.stack  = AttrMeta("axis_stack", str, str, uiorgCat.simple, False, [])
    _.stackWeight  = AttrMeta(None, int, int, uiorgCat.advanced, False, [])
    _.axis   =  AttrMeta("axis_title", str, str, uiorgCat.simple, False, [])
    _.offset = AttrMeta(False, bool, bool, uiorgCat.config, False, [])
    
    #_.title	object		
#

def AxesTicksCfgOptions(_cfg):
    """
    Tick option for all axes
    """
    _ = _cfg
    _.backdropColor = AttrMeta(
        "", Color, Color, uiorgCat.nitpick, False, [])  # background color for label
    _.backdropPadding = AttrMeta(
        2, int, [0, 5], uiorgCat.advanced, False, [])  # padding for label backdrop
    _.callback = AttrMeta(None, None, None, uiorgCat.TBD, False, [])
    _.display = AttrMeta(False, bool, bool, uiorgCat.simple, True, [])
    _.color = AttrMeta("", Color, Color, uiorgCat.nitpick, False, [])  # TBD
    _.font = AttrMeta(None, None, None, uiorgCat.TBD, False, [])
    # _.major = Dict(, False, []) #TBD: major tick formatting
    _.padding = AttrMeta(2, int, int, uiorgCat.nitpick, False, [])
    _.showLabelBackdrop = AttrMeta(False, bool, bool, uiorgCat.nitpick, False, [])
    _.textStrokeColor = AttrMeta("", Color, Color, uiorgCat.TBD, False, [])
    _.textStrokeWidth = AttrMeta(0, int, int, uiorgCat.TBD, False, [])

    _.z = AttrMeta(0, int, int, uiorgCat.advanced, False, [])
    
def CartesianTicksCfgOptions(_cfg):
    _ = _cfg
    _.align = AttrMeta('center', ['start', 'center', 'end'], [
                                'start', 'center', 'end'], uiorgCat.ocd, False, [])
    _.crossAlign = AttrMeta("near", ["near", "center", "far"], [
                                     "near", "center", "far"], uiorgCat.ocd, False, [])
    _.sampleSize = AttrMeta(None, None, None, uiorgCat.TBD, False, [])
    _.autoSkip = AttrMeta(True, bool, bool, uiorgCat.advanced, False, [])
    _.autoSkipPadding = AttrMeta(3, int, int, uiorgCat.advanced, False, [])
    _.includeBounds = AttrMeta(None, None, None, uiorgCat.TBD, False, [])
    _.labelOffset = AttrMeta(0, int, [0, 5], uiorgCat.nitpick, False, [])
    _.maxRotation = AttrMeta(50, int, [0, 5], uiorgCat.advanced, False, [])
    _.minRotation = AttrMeta(0, int, [0, 5], uiorgCat.advanced, False, [])
    _.mirror = AttrMeta(False, bool, bool, uiorgCat.advanced, False, [])

def AxisGridCfgOptions(_cfg):
    _cfg.display = AttrMeta(
        False, bool, bool, uiorgCat.simple, True, [('/type', 'line')])
    _cfg.color = AttrMeta(
        twt.gray/1, Color, Color, uiorgCat.simple, False, [('/options/scales/xAxis/grid/display', 'line')])
    _cfg.borderColor = AttrMeta(
        twt.gray/2, Color, Color, uiorgCat.simple, False, [('/options/scales/xAxis/grid/display', 'line')])
    _cfg.tickColor = AttrMeta(
        twt.gray/1, Color, Color, uiorgCat.simple, False, [('/options/scales/xAxis/grid/display', 'line')])
    _cfg.circular = AttrMeta(
        None, None, None, uiorgCat.simple, False, [('/options/scales/xAxis/grid/display', 'line')])  # from for radar chart


def get_basecfg(setupChoices):
    """
    setupChoices: the choices user made at chartSetup
    """
    _base = cfgAttrMeta_base = Dict(track_changes=True)
    _base.type = AttrMeta(PlotType.Undef, PlotType,
                          PlotType, uiorgCat.chartSetup, True, all_context)

    def Options():
        options = _base.options

        def Elements():
            elements = options.elements

            def Line():
                linecfg = elements.line
                OptionsElementsLineCfg(linecfg)
            Elements.Line = Line

        Elements()
        Options.Elements = Elements

        def Plugins():
            plugins = options.plugins

            def Legend():
                legend = plugins.legend
                OptionsPluginsLegend(legend)
                legendtitle = legend.title
                OptionsPluginsLegendTitle(legendtitle)

                legendlabels = legend.labels
                OptionsPluginsLegendLabels(legendlabels)

            Plugins.Legend = Legend

            def Tooltips():
                tooltips = plugins.tooltips
                # TODO:tobe filled uplater
                print("will deal with later")
                pass
            Plugins.Tooltips = Tooltips
        Plugins()
        Options.Plugins = Plugins

        def Scales():
            scales = options.scales
            def Axis(axis_id):
                if axis_id:
                    axis = scales[axis_id]
                    AxisCfgOptions(axis)
                    title = axis.title
                    AxisTitleCfgOptions(title)

                    grid = axis.grid
                    AxisGridCfgOptions(grid)

                    ticks = axis.ticks
                    AxesTicksCfgOptions(ticks)
            def CartesianAxis(axis_id):
                #following convention of chart.js to use
                #obj for complex/nested json values
                if axis_id:
                    axis = scales[axis_id]
                    #AxisCfgOptions(axis)
                    CartesianAxisCfgOption(axis)

                    
                    #apply object options common to all cartesian axis
                    # e.g grid , title, position, ticks
                    #grid = axis.grid
                    #CartesianGrid(grid)
                    # ticks
                    ticks = axis.ticks
                    #AxesTicksCfgOptions(ticks)
                    CartesianTicksCfgOptions(ticks)
                # def Grid():
                #     # TODO: grid shouldn't belong to scales; 
                #     grid = axis.grid
                #     CartesianGrid(grid)
                # CartesianAxis.Grid = Grid
            CartesianAxis(None)
            Axis(None)
            
            Scales.CartesianAxis = CartesianAxis
            Scales.Axis = Axis
        Scales()
        Options.Scales = Scales

    #dry call --> makes Options and its nested function a class/instance;
    #Options.Elements and Options.Scales is now active
    Options()

    #Options.Elements.Line()
    if setupChoices:
        match setupChoices.axes.type:
            case AxesType.cartesian:
               for axis in setupChoices.axises:
                   Options.Scales.Axis(axis)
                   Options.Scales.CartesianAxis(axis)
    Options.Plugins.Legend()  # also includes Legend.Labels,Legend.Title
    
    return _base
