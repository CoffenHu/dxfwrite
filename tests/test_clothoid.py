#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test clothoid module and curve
# Created: 28.03.2010

import unittest2 as unittest

from dxfwrite.algebra.clothoid import Clothoid as AlgebraClothoid
from dxfwrite.curves import Clothoid as DXFClothoid

expected_points = [
    (0.0, 0.0), (0.4999511740825297, 0.0052079700401204106),
    (0.99843862987320509, 0.041620186803547267),
    (1.4881781381789292, 0.13983245006538086),
    (1.9505753764262783, 0.32742809475246343),
    (2.3516635639763064, 0.62320387651494735),
    (2.6419212729287223, 1.0273042715153904),
    (2.7637635905799862, 1.5086926753401932),
    (2.6704397998515645, 1.9952561538526452),
    (2.3566156629790327, 2.3766072153088964),
    (1.8936094203448928, 2.5322897289776636)
]

expected_mirror_dxf = u"  0\nPOLYLINE\n 62\n256\n  8\n0\n 66\n1\n 10\n0.0\n 20\n"\
"0.0\n 30\n0.0\n 70\n8\n  0\nVERTEX\n  8\n0\n 10\n1.0\n 20\n1.0\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n0.134107984968\n 20\n0.499769091903\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-0.730982368063\n 20\n-0.00184649551056\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-1.59446275629\n 20\n-0.506227583837\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-2.45551162626\n 20\n-1.01474722617\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-3.31328762657\n 20\n-1.52876669054\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-4.16692315582\n 20\n-2.04963128553\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-5.01551804038\n 20\n-2.57866597726\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-5.85813337868\n 20\n-3.11717074804\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-6.6937855919\n 20\n-3.66641564948\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n-7.5214407239\n 20\n-4.22763550456\n 30\n0.0\n  0\nSEQEND\n"

expected_dxf = u"  0\nPOLYLINE\n 62\n256\n  8\n0\n 66\n1\n 10\n0.0\n 20\n0.0\n"\
" 30\n0.0\n 70\n8\n  0\nVERTEX\n  8\n0\n 10\n1.0\n 20\n1.0\n 30\n0.0\n  0\n"\
"VERTEX\n  8\n0\n 10\n1.86589201503\n 20\n1.5002309081\n 30\n0.0\n  0\nVERTEX\n"\
"  8\n0\n 10\n2.73098236806\n 20\n2.00184649551\n 30\n0.0\n  0\nVERTEX\n  8\n0\n"\
" 10\n3.59446275629\n 20\n2.50622758384\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"4.45551162626\n 20\n3.01474722617\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"5.31328762657\n 20\n3.52876669054\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"6.16692315582\n 20\n4.04963128553\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"7.01551804038\n 20\n4.57866597726\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"7.85813337868\n 20\n5.11717074804\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"8.6937855919\n 20\n5.66641564948\n 30\n0.0\n  0\nVERTEX\n  8\n0\n 10\n"\
"9.5214407239\n 20\n6.22763550456\n 30\n0.0\n  0\nSEQEND\n"

class TestAlgebraClothoid(unittest.TestCase):
    def test_approximate(self):
        clothoid = AlgebraClothoid(2.0)
        results = clothoid.approximate(5, 10)
        for expected, result in zip(expected_points, results):
            self.assertAlmostEqual(expected, result)

class TestDXFClothoid(unittest.TestCase):
    def test_api(self):
        clothoid = DXFClothoid(start=(1, 1), paramA=20, length=10, rotation=30,
                               mirrorx = True, mirrory=False, segments=50,
                               color=1, layer='0', linetype='SOLID')
        self.assertNotEqual(clothoid, None)

    def test_implementation(self):
        clothoid = DXFClothoid(start=(1, 1), paramA=25, length=10, rotation=30,
                               mirrorx=False, mirrory=False, segments=10)
        result = clothoid.__dxf__()
        self.assertEqual(expected_dxf, result)

    def test_implementation_mirror(self):
        clothoid = DXFClothoid(start=(1, 1), paramA=25, length=10, rotation=30,
                               mirrorx=True, mirrory=True, segments=10)
        result = clothoid.__dxf__()
        self.assertEqual(expected_mirror_dxf, result)

if __name__=='__main__':
    unittest.main()