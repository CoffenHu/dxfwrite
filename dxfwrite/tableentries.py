#!/usr/bin/env python
#coding:utf-8
# Purpose: tables entries R12
# module belongs to package: dxfwrite.py
# Created: 09.02.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

__author__ = "mozman <mozman@gmx.at>"

from dxfwrite.base import *
from dxfwrite.linepattern import LinePatternDef

_DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION = {
    'LTYPE': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'description': AttribDef(DXFString, 3, priority=101),
        'pattern': AttribDef(PassThroughFactory, priority=102),
        },
    'LAYER': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'color': AttribDef(DXFInt, 62, priority=101),
        'linetype': AttribDef(DXFString, 6, priority=102),
        },
    'STYLE': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'height': AttribDef(DXFFloat, 40, priority=101),
        'width': AttribDef(DXFFloat, 41, priority=102),
        'last_height': AttribDef(DXFFloat, 42, priority=103),
        'oblique': AttribDef(DXFAngle, 50, priority=104),
        'generation_flags': AttribDef(DXFInt, 71, priority=105),
        'font': AttribDef(DXFString, 3, priority=106),
        'bigfont': AttribDef(DXFString, 4, priority=107),
        },
    'VIEW': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'height': AttribDef(DXFFloat, 40, priority=101),
        'width': AttribDef(DXFFloat, 41, priority=102),
        'center_point': AttribDef(DXFPoint2D, 0, priority=103),
        'direction_point': AttribDef(DXFPoint3D, 1, priority=104),
        'target_point': AttribDef(DXFPoint3D, 2, priority=105),
        'lens_length': AttribDef(DXFFloat, 42, priority=106),
        'front_clipping': AttribDef(DXFFloat, 43, priority=107),
        'back_clipping': AttribDef(DXFFloat, 44, priority=108),
        'view_twist': AttribDef(DXFAngle, 50, priority=109),
        'view_mode': AttribDef(DXFInt, 71, priority=110),
        },
    'VPORT': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'lower_left': AttribDef(DXFPoint2D, 0,priority=101),
        'upper_right': AttribDef(DXFPoint2D, 1, priority=102),
        'center_point': AttribDef(DXFPoint2D, 2, priority=103),
        'snap_base': AttribDef(DXFPoint2D, 3, priority=104),
        'snap_spacing': AttribDef(DXFPoint2D, 4, priority=105),
        'grid_spacing': AttribDef(DXFPoint2D, 5, priority=106),
        'direction_point': AttribDef(DXFPoint3D, 6, priority=107),
        'target_point': AttribDef(DXFPoint3D, 7, priority=108),
        'height': AttribDef(DXFFloat, 40, priority=112),
        'aspect_ratio': AttribDef(DXFFloat, 41, priority=113),
        'lens_length': AttribDef(DXFFloat, 42, priority=109),
        'front_clipping': AttribDef(DXFFloat, 43, priority=110),
        'back_clipping': AttribDef(DXFFloat, 44, priority=111),
        'snap_rotation': AttribDef(DXFAngle, 50, priority=115),
        'view_twist': AttribDef(DXFAngle, 51, priority=116),
        'status': AttribDef(DXFInt, 68, priority=117),
        'id': AttribDef(DXFInt, 69, priority=118),
        'view_mode': AttribDef(DXFInt, 71, priority=122),
        'circle_zoom': AttribDef(DXFInt, 72, priority=123),
        'fast_zoom': AttribDef(DXFInt, 73, priority=124),
        'ucs_icon': AttribDef(DXFInt, 74, priority=126),
        'snap_on': AttribDef(DXFInt, 75, priority=127),
        'grid_on': AttribDef(DXFInt, 76, priority=128),
        'snap_style': AttribDef(DXFInt, 77, priority=129),
        'snap_isopair': AttribDef(DXFInt, 78, priority=130)
        },
    'APPID': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        },
    'UCS': {
        'name': AttribDef(DXFString, 2, priority=52),
        'flags': AttribDef(DXFInt, 70, priority=53),
        'origin': AttribDef(DXFPoint3D, 0,priority=101),
        'xaxis': AttribDef(DXFPoint3D, 1, priority=102),
        'yaxis': AttribDef(DXFPoint3D, 2, priority=103),
        },
    }

class _TableEntry(object):
    """ Base class for table entries.
    """
    TABLE_NAME = "ABSTRACT_TABLE"
    DXF_ATTRIBUTES = {}

    def __init__(self, name, **kwargs):
        self.attribs = {}
        # set attribs from kwargs
        self['name'] = name
        for key, value in kwargs.items():
            self[key] = value

    def is_valid_attribute_name(self, key):
        """ True if an AttribDef for key exists. """
        return key in self.DXF_ATTRIBUTES

    def __setitem__(self, key, value):
        if self.is_valid_attribute_name(key):
            self.attribs[key] = self._get_dxf_atom(key, value) # factory is called
        else:
            raise KeyError("Invalid attribute '%s' for TableEntry '%s'." % (str(key), self.__class__.__name__))

    def __getitem__(self, key):
        if self.is_valid_attribute_name(key):
            element = self.attribs[key]
            try:
                return element.value # DXFAtom
            except AttributeError:
                return element # DXFList or list or tuple
        else:
            raise KeyError("Invalid attribute '%s' for TableEntry '%s'." % (str(key), self.__class__.__name__))

    def _get_dxf_atom(self, attribname, value):
        """ create an object for attribname by factory from attribute_definition """
        attrib = self.DXF_ATTRIBUTES[attribname]
        return attrib.factory(value, attrib.group_code)

    def _priority(self, key):
        """ get priority of attribute key """
        return self.DXF_ATTRIBUTES[key].priority

    def get_attribs(self):
        """ get attribs sorted by priority """
        priority_attribs = ( (self._priority(key), value)
                 for key, value in self.attribs.items() )
        return ( value for priority, value  in sorted(priority_attribs) )

    def __dxf__(self):
        return dxfstr(self.__dxftags__())

    def __dxftags__(self):
        dxf = DXFList()
        dxf.append(DXFAtom(self.TABLE_NAME))
        dxf.extend(self.get_attribs()) # sorted attribs
        return dxf


class Linetype(_TableEntry):
    """ DXF LTYPE table entry - linetype definition

    INIT-PARAMETER

    name
        linetype name
    flags
        Standard flags (bit-coded values): (see module flags.py STD_FLAGS_...)
    description
        descriptive text for linetype
    pattern
        LinePatternDef object
    """
    TABLE_NAME = 'LTYPE'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['LTYPE']

    def __init__(self, name, **kwargs):
        default = {
            'flags': 0,
            'description': ""
        }
        default.update(kwargs)
        super(Linetype, self).__init__(name, **default)

class Layer(_TableEntry):
    """ DXF LAYER table entry - layer definition

    INIT-PARAMETER

    name
        layer name
    flags
        standard flag values, bit-coded
        STD_FLAGS_LAYER_FROZEN = If set, layer is frozen
        STD_FLAGS_LAYER_FROZEN_BY_DEFAULT = If set, layer is frozen by
            default in new Viewports
        STD_FLAGS_LAYER_LOCKED = If set, layer is locked
    color
        color-number (if negative, layer is off)
    linetype
        name of linetype (string)
    """
    TABLE_NAME = 'LAYER'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['LAYER']

    def __init__(self, name, **kwargs):
        default = {
            'flags': 0,
            'color': 1,
            'linetype': "CONTINUOUS"
        }
        default.update(kwargs)
        super(Layer, self).__init__(name, **default)

class Style(_TableEntry):
    """ DXF STYLE table entry - textstyle definition

    INIT-PARAMETER

    name
        textstyle name
    flags
        standard flag values (int), bit-coded
    generation_flags
        text generation flags (int), default = 0
        STYLE_TEXT_BACKWARD = Text is backward (mirrored in X)
        STYLE_TEXT_UPSIDEDOWN = Text is upside down (mirrored in Y)
    height
        fixed text height, (float), 0 if not fixed = default
    last_height
        last height used (float), default=1.
    width
        width factor (float), default=1.
    oblique
        oblique angle in degree (float), default=0.
    font
        primary font filename (string), default="ARIAL"
    bigfont
        big-font file name(string), default=""
    """
    TABLE_NAME = 'STYLE'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['STYLE']

    def __init__(self, name, **kwargs):
        default = {
            'flags': 0,
            'height': 0,
            'width': 1,
            'oblique': 0,
            'generation_flags': 0,
            'last_height': 1,
            'font': "ARIAL.TTF",
            'bigfont': ""
        }
        default.update(kwargs)
        super(Style, self).__init__(name, **default)

class View(_TableEntry):
    """ DXF VIEW table entry - view definition
    """
    TABLE_NAME = 'VIEW'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['VIEW']

    def __init__(self, name, **kwargs):
        """ Create a new view.

        :param string name: view name
        :param int flags: standard flag values, bit-coded, default=0
            STD_FLAGS_PAPER_SPACE, if set this is a paper space view.
        :param float height, width: view height and width, in DCS?!, default=1.0
        :param center_point: view center point, in DCS?! (xy-tuple), default=(.5, .5)
        :param direction_point: view direction from target point, in WCS!!
            (xyz-tuple), default=(0, 0, 1)
        :param target_point: target point, in WCS!! (xyz-tuple), default=(0, 0, 0)
        :param float lens_length: lens length, default=50
        :param float front_clipping: front and back clipping planes,
            offsets from target point, default=0
        :param back_clipping: see front_clipping
        :param float view_twist: twist angle in degree, default=0
        :param int view_mode: view mode, bit-coded, default=0

        """
        default = {
            'flags': 0,
            'height': 1.0,
            'width': 1.0,
            # index_shift set at output, don't care
            'center_point': (0.5, 0.5) ,
            'direction_point': (0, 0, 1) ,
            'target_point': (0, 0, 0),
            'lens_length': 50,
            'front_clipping': 0,
            'back_clipping': 0,
            'view_twist': 0,
            'view_mode': 0
        }
        default.update(kwargs)
        super(View, self).__init__(name, **default)

class VPort(_TableEntry):
    """ DXF VPORT table entry - viewport definition
    """
    TABLE_NAME = 'VPORT'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['VPORT']

    def __init__(self, name, **kwargs):
        """ Create a new viewport table entry.

        :param str name: viewport name
        :param int flags: standard flag values, bit-coded, default=0
        :param lower_left: lower-left corner of viewport, (xy-tuple), default=(0, 0)
        :param upper_right: upper-right corner of viewport, (xy-tuple), default=(1, 1)
        :param center_point: view center point, in WCS, (xy-tuple), default=(.5, .5)
        :param snap_base: snap base point, (xy-tuple), default=(0, 0)
        :param snap_spacing: snap spacing, X and Y (xy-tuple), default=(.1, .1)
        :param grid_spacing: grid spacing, X and Y (xy-tuple), default=(.1, .1)
        :param direction_point: view direction from target point (xyz-tuple), default=(0, 0, 1)
        :param target_point: view target point (xyz-tuple), default=(0, 0, 0)
        :param aspect_ratio: viewport aspect ratio (float), default=1.
        :param float lens_length: lens length, default=50
        :param float front_clipping: front and back clipping planes, offsets
            from target point , default=0
        :param float back_clipping: see front_clipping
        :param float view_twist: twist angle in degree, default=0
        :param float circle_zoom: circle zoom percent, default=100
        :param int view_mode: view mode, bit-coded, default=0
        :param int fast_zoom: fast zoom setting, default=1
        :param int ucs_icon: UCSICON settings, default=3
        :param int snap_on: snap on/off, default=0
        :param int grid_on: grid on/off, default=0
        :param int snap_style: snap style, default=0
        :param int snap_isopair: snap isopair, default=0
        """
        default = {
            'flags': 0,
            'lower_left': (0, 0),
            'upper_right': (1, 1),
            'center_point': (0.5, 0.5),
            'snap_base': (0, 0),
            'snap_spacing': (0.1, 0.1),
            'grid_spacing': (0.1, 0.1),
            'direction_point': (0, 0, 1),
            'target_point': (0, 0, 0),
            'aspect_ratio': 1,
            'lens_length': 50,
            'front_clipping': 0,
            'back_clipping': 0,
            'height': 1,
            'snap_rotation': 0,
            'view_twist': 0,
            'status': 0,
            'id': 0,
            'circle_zoom': 100,
            'view_mode': 0,
            'fast_zoom': 1,
            'ucs_icon': 3,
            'snap_on': 0,
            'grid_on': 0,
            'snap_style': 0,
            'snap_isopair': 0
        }
        default.update(kwargs)
        super(VPort, self).__init__(name, **default)

class AppID(_TableEntry):
    TABLE_NAME = 'APPID'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['APPID']

    def __init__(self, name, **kwargs):
        default = {
            'flags': 0,
        }
        default.update(kwargs)
        super(AppID, self).__init__(name, **default)

class UCS(_TableEntry):
    """ DXF UCS - user coordinate system

    INIT-PARAMETER

    name
        layer name
    origin
        origin in WCS
    xaxis
        xaxis direction in WCS
    yaxis
        yaxis direction in WCS
    """
    TABLE_NAME = 'UCS'
    DXF_ATTRIBUTES = _DXF12_TABLE_ENTRY_ATTRIBUTE_DEFINITION['UCS']

    def __init__(self, name, **kwargs):
        default = {
            'flags': 0,
            'origin': (0., 0., 0.),
            'xaxis':  (1., 0., 0.),
            'yaxis':  (0., 1., 0.),
        }
        default.update(kwargs)
        super(UCS, self).__init__(name, **default)
