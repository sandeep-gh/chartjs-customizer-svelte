from aenum import Enum, auto, StrEnum
from typing import NamedTuple, Any


class uiorgCat(Enum):
    """attrmeta belongs to one of the categories for organization on the ui
    """
    chartSetup = "chartSetup"
    required = "required"
    simple = "simple"  # TODO:refactor it tobasic
    advanced = "advanced"
    nitpick = "nitpick"  # minor decor changes
    ocd = "ocd"  # miniscule changes
    perf = "perf"
    config = "config"
    TBD = "tbd"
    all = "all"


class AttrMeta(NamedTuple):
    """
    metadata about ui component
    """
    default: Any
    vtype: Any
    vrange: Any
    group: Any
    active: Any
    context: Any  # describes all scenarios when attribute is active


class PlotType(str, Enum):
    Line = "line"
    Bar = "bar"
    Scatter = "scatter"
    Bubble = "bubble"
    Undef = "None"
    


class PointStyle(Enum):
    circle = 'circle'
    cross = 'cross'
    crossRot = 'crossRot'
    dash = 'dash'
    line = 'line'
    rect = 'rect'
    rectRounded = 'rectRounded'
    rectRot = 'rectRot'
    star = 'star'
    triangle = 'triangle'


class CubicInterpolationMode(Enum):
    default = "default"
    monotone = "monotone"


class LineJoinStyle(Enum):
    bevel = "bevel"
    roundo = "round"
    miter = "miter"


class BorderCapStyle(Enum):
    butt = "butt"
    roundo = "round"
    square = "square"


class TextAlign(Enum):
    start = "start"
    center = "center"
    end = "end"


class AxesType(Enum):
    cartesian = 'Cartesian'
    radial = 'radial'


class CartesianAxisType(Enum):
    linear = "linear"
    logarithmic = "logarithmic"
    category = "category"
    time = "time"
    timeseries = "timeseries"
#

class Position(Enum):
    top = "top"
    left = "left"
    bottom = "bottom"
    right = "right"
    chart = "chartArea"
    pass

class Align(Enum):
    start = "start"
    center = "center"
    end = "end"
    
# class PlotType(Enum):
#     line = """type:'line'"""
#     bar = """type:bar"""
#     pass


# options namespace
class MaintainAspectRatio(Enum):
    t = "maintainAspectRatio:true"
    f = "maintainAspectRatio:false"
    pass


class Axis(Enum):
    x = "x"
    y = "y"
    y1 = "y1"

class Color(Enum):
    black = "#000000"
    white = "#FFFFFF"
    red =  "#FF0000"
    

    

class FalseDict(Enum):
    """
    value is either False or a dict
    """
    pass


def is_visible(attrmeta):
    if attrmeta.vtype != None:
        if attrmeta.group != uiorgCat.TBD:
            return True
    return False
