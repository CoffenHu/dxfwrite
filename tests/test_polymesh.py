#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test dxfwrite.entities.Polymesh
# Created: 23.02.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import unittest2 as unittest

from dxfwrite.entities import Polymesh
from dxfwrite import dxfstr

class TestPolymesh(unittest.TestCase):
    def setUp(self):
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def test_polymesh(self):
        mesh = Polymesh(2, 2)
        mesh.set_vertex(0, 0, (1, 1, 0))
        vt1 = "  0\nVERTEX\n  8\n0\n 10\n1.0\n 20\n1.0\n 30\n0.0\n 70\n64\n"
        mesh.set_vertex(0, 1, (2, 1, 0))
        vt2 = "  0\nVERTEX\n  8\n0\n 10\n2.0\n 20\n1.0\n 30\n0.0\n 70\n64\n"
        mesh.set_vertex(1, 0, (1, 2, 0))
        vt3 = "  0\nVERTEX\n  8\n0\n 10\n1.0\n 20\n2.0\n 30\n0.0\n 70\n64\n"
        mesh.set_vertex(1, 1, (2, 2, 0))
        vt4 = "  0\nVERTEX\n  8\n0\n 10\n2.0\n 20\n2.0\n 30\n0.0\n 70\n64\n"

        expected = "  0\nPOLYLINE\n  8\n0\n 66\n1\n" \
                 " 70\n16\n 71\n2\n 72\n2\n" + vt1 + vt2 + vt3 + vt4 + "  0\nSEQEND\n"
        self.assertEqual(dxfstr(mesh), expected)

if __name__=='__main__':
    unittest.main()