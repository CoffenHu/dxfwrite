#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test dxfwrite.dimlines
# Created: 21.03.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
if sys.version_info[:2]> (2, 6):
    import unittest
else: # python 2.6 and prior needs the unittest2 package
    import unittest2 as unittest

from dxfwrite.dimlines import ArcDimension

class TestArcDimAPI(unittest.TestCase):
    def test_init(self):
        dimline = ArcDimension(
            pos=(5, 5),
            center=(0, 0),
            start=(1, 0),
            end=(1, 1),
            arc3points=False,
            dimstyle='default',
            layer="ARCDIMENSION",
            roundval=1)
        dxf = dimline.__dxf__()
        self.assertTrue("ARCDIMENSION" in dxf)

class TestArcDimImplementation(unittest.TestCase):
    def test_45deg(self):
        expected = "  0\nARC\n 62\n7\n  8\nDIMENSIONS\n 10\n0.0\n 20\n0.0\n"\
                 " 30\n0.0\n 40\n7.07106781187\n 50\n0.0\n 51\n45.0\n  0\n"\
                 "LINE\n 62\n5\n  8\nDIMENSIONS\n 10\n1.3\n 20\n0.0\n 30\n"\
                 "0.0\n 11\n7.07106781187\n 21\n0.0\n 31\n0.0\n  0\nLINE\n"\
                 " 62\n5\n  8\nDIMENSIONS\n 10\n0.919238815543\n 20\n"\
                 "0.919238815543\n 30\n0.0\n 11\n5.0\n 21\n5.0\n 31\n0.0\n"\
                 "  0\nTEXT\n 62\n7\n  8\nDIMENSIONS\n 10\n6.94856061401\n"\
                 " 20\n2.8781880453\n 30\n0.0\n 40\n0.5\n  1\n79\n 50\n-67.5\n"\
                 "  7\nISOCPEUR\n 72\n1\n 73\n2\n 11\n6.94856061401\n 21\n"\
                 "2.8781880453\n 31\n0.0\n  0\nINSERT\n  8\nDIMENSIONS\n  2\n"\
                 "DIMTICK_ARCH\n 10\n7.07106781187\n 20\n0.0\n 30\n0.0\n 41\n"\
                 "1.0\n 42\n1.0\n 50\n90.0\n  0\nINSERT\n  8\nDIMENSIONS\n"\
                 "  2\nDIMTICK_ARCH\n 10\n5.0\n 20\n5.0\n 30\n0.0\n 41\n1.0\n"\
                 " 42\n1.0\n 50\n135.0\n"
        dimline = ArcDimension(pos=(5,5), center=(0, 0), start=(1, 0),
                               end=(1, 1), )
        self.assertEqual(dimline.__dxf__(), expected)

if __name__=='__main__':
    unittest.main()