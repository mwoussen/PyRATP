
# This file has been generated at Mon Apr 18 15:51:30 2011

from openalea.core import *


__name__ = 'PyRATP.demo'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '0.9.0'
__authors__ = ''
__institutes__ = None
__icon__ = ''


__all__ = ['test1', '_64587664', 'micrometeo', '_64587728', 'vegetation', 'complet']



test1 = CompositeNodeFactory(name='test1',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PyRATP', 'read grid'),
   3: ('PyRATP', 'plant from vegestar'),
   4: ('PyRATP', 'fill grid'),
   5: ('pyratp.data', 'vgxTest.vgx'),
   6: ('pyratp.data', 'grid3D_4_4_4.grd')},
                             elt_connections={  10014820: (3, 1, 4, 1),
   10014832: (2, 0, 4, 6),
   10014844: (3, 5, 4, 5),
   10014856: (6, 0, 2, 0),
   10014868: (3, 0, 4, 0),
   10014880: (3, 3, 4, 3),
   10014892: (3, 4, 4, 4),
   10014904: (5, 0, 3, 0),
   10014916: (3, 2, 4, 2)},
                             elt_data={  2: {  'block': False,
         'caption': 'read grid',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x03FF8D50> : "read grid"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -194.27963248178673,
         'posy': -273.77492108594106,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'plant from vegestar',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x03FF8CB0> : "plant from vegestar"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -334.0019450522733,
         'posy': -273.15827862873817,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'fill grid',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x03FF8D10> : "fill grid"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -328.57035851200703,
         'posy': -177.4078049415829,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'vgxTest.vgx',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x04615B50> : "vgxTest.vgx"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -316.31444167542702,
         'posy': -346.70272864861192,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'grid3D_4_4_4.grd',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x04615B70> : "grid3D_4_4_4.grd"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -218.93379478408369,
         'posy': -348.77465730587465,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [],
   5: [(0, 'PackageData(pyratp.data, vgxTest.vgx)'), (1, 'None'), (2, 'None')],
   6: [  (0, 'PackageData(pyratp.data, grid3D_4_4_4.grd)'),
         (1, 'None'),
         (2, 'None')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-194.27963248178673, -273.77492108594106],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-334.0019450522733, -273.15827862873817],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [-328.57035851200703, -177.4078049415829],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-316.31444167542702, -346.70272864861192],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-218.93379478408369, -348.77465730587465],
         'useUserColor': False,
         'userColor': None},
   7: {  'position': [-123.65551126795962, -170.59413391253204],
         'useUserColor': False,
         'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_64587664 = CompositeNodeFactory(name='vegestar grid',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('pyratp.data', 'aa2004petit.vgx'), 3: ('PyRATP', 'grid from vegestar')},
                             elt_connections={  38204384: (2, 0, 3, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'aa2004petit.vgx',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x63e1910> : "aa2004petit.vgx"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -185.0,
         'posy': -28.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'grid from vegestar',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x3cb0890> : "grid from vegestar"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -195.0,
         'posy': 35.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, 'PackageData(pyratp.data, aa2004petit.vgx)'),
         (1, 'None'),
         (2, 'None')],
   3: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-185.0, -28.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [-195.0, 35.0], 'useUserColor': False, 'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




micrometeo = CompositeNodeFactory(name='micrometeo',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PyRATP', 'read_micrometeo'), 3: ('pyratp.data', 'mmeteo052000.mto')},
                             elt_connections={  10014916: (3, 0, 2, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'read_micrometeo',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x04089E10> : "read_micrometeo"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -78.0,
         'posy': -29.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'mmeteo052000.mto',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x046A4E30> : "mmeteo052000.mto"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -61.0,
         'posy': -177.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [  (0, 'PackageData(pyratp.data, mmeteo052000.mto)'),
         (1, 'None'),
         (2, 'None')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-78.0, -29.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [-61.0, -177.0], 'useUserColor': False, 'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_64587728 = CompositeNodeFactory(name='test_grid',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PyRATP', 'read grid'), 3: ('pyratp.data', 'grid3Da_2004.grd')},
                             elt_connections={  36852704: (3, 0, 2, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'read grid',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x8d21ad0> : "read grid"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -269.0,
         'posy': -50.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'grid3Da_2004.grd',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x8d21810> : "grid3Da_2004.grd"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -293.0,
         'posy': -112.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [  (0, 'PackageData(pyratp.data, grid3Da_2004.grd)'),
         (1, 'None'),
         (2, 'None')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-269.0, -50.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [-293.0, -112.0], 'useUserColor': False, 'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




vegetation = CompositeNodeFactory(name='vegetation',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PyRATP', 'read_vegetation'), 3: ('pyratp.data', 'vegetationa_2004.vfn')},
                             elt_connections={  10014916: (3, 0, 2, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'read_vegetation',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x03FF8DB0> : "read_vegetation"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 204.0,
         'posy': 25.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'vegetationa_2004.vfn',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x04616C90> : "vegetationa_2004.vfn"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': 234.0,
         'posy': -134.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [  (0, 'PackageData(pyratp.data, vegetationa_2004.vfn)'),
         (1, 'None'),
         (2, 'None')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [204.0, 25.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [234.0, -134.0], 'useUserColor': False, 'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




complet = CompositeNodeFactory(name='complet',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PyRATP', 'read_micrometeo'),
   3: ('pyratp.data', 'mmeteo052000.mto'),
   4: ('PyRATP', 'read grid'),
   5: ('PyRATP', 'plant from vegestar'),
   6: ('PyRATP', 'fill grid'),
   7: ('pyratp.data', 'vgxTest.vgx'),
   8: ('pyratp.data', 'grid3D_4_4_4.grd'),
   9: ('PyRATP', 'read_vegetation'),
   10: ('pyratp.data', 'vegetationa_2004.vfn'),
   12: ('PyRATP', 'read_skyvault'),
   13: ('pyratp.data', 'skyvaultsoc.skv'),
   14: ('PyRATP', 'do_all')},
                             elt_connections={  11301496: (12, 0, 14, 0),
   11301520: (9, 0, 14, 0),
   11301544: (6, 0, 14, 0),
   11301568: (2, 0, 14, 0),
   11301592: (8, 0, 4, 0),
   11301616: (5, 1, 6, 1),
   11301640: (5, 3, 6, 3),
   11301664: (4, 0, 6, 6),
   11301688: (5, 2, 6, 2),
   11301712: (5, 0, 6, 0),
   11301736: (7, 0, 5, 0),
   11301760: (5, 4, 6, 4),
   11301784: (10, 0, 9, 0),
   11301808: (5, 5, 6, 5),
   11301832: (3, 0, 2, 0),
   11301856: (13, 0, 12, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'read_micrometeo',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x2fee890> : "read_micrometeo"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -323.0,
         'posy': -64.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'mmeteo052000.mto',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x5564bd0> : "mmeteo052000.mto"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -333.0,
         'posy': -216.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'read grid',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x2fee6d0> : "read grid"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -8.2776874295134348,
         'posy': -153.0002637800664,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'plant from vegestar',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x2efd890> : "plant from vegestar"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -148.0,
         'posy': -152.38362132286352,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'fill grid',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x2fee710> : "fill grid"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -142.56841345973373,
         'posy': -56.633147635708241,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'vgxTest.vgx',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x5564b10> : "vgxTest.vgx"',
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -130.31249662315372,
         'posy': -225.92807134273727,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'grid3D_4_4_4.grd',
         'delay': 0,
         'factory': '<openalea.core.data.DataFactory object at 0x5564ad0> : "grid3D_4_4_4.grd"',
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -32.931849731810416,
         'posy': -228.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'read_vegetation',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x2fee810> : "read_vegetation"',
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 93.0,
         'posy': -58.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'vegetationa_2004.vfn',
          'delay': 0,
          'factory': '<openalea.core.data.DataFactory object at 0x5564cd0> : "vegetationa_2004.vfn"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set([2]),
          'posx': 123.0,
          'posy': -217.0,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'read_skyvault',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x2fee790> : "read_skyvault"',
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 272.0,
          'posy': -57.196447909898211,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'skyvaultsoc.skv',
          'delay': 0,
          'factory': '<openalea.core.data.DataFactory object at 0x5564d10> : "skyvaultsoc.skv"',
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set([2]),
          'posx': 348.0,
          'posy': -204.0,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': 'do_all',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x2fee8d0> : "do_all"',
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -81.158761100281566,
          'posy': 12.856833441628762,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [  (0, 'PackageData(pyratp.data, mmeteo052000.mto)'),
         (1, 'None'),
         (2, 'None')],
   4: [],
   5: [],
   6: [],
   7: [(0, 'PackageData(pyratp.data, vgxTest.vgx)'), (1, 'None'), (2, 'None')],
   8: [  (0, 'PackageData(pyratp.data, grid3D_4_4_4.grd)'),
         (1, 'None'),
         (2, 'None')],
   9: [],
   10: [  (0, 'PackageData(pyratp.data, vegetationa_2004.vfn)'),
          (1, 'None'),
          (2, 'None')],
   12: [],
   13: [  (0, 'PackageData(pyratp.data, skyvaultsoc.skv)'),
          (1, 'None'),
          (2, 'None')],
   14: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-323.0, -64.0], 'userColor': None, 'useUserColor': False},
   3: {'position': [-333.0, -216.0], 'userColor': None, 'useUserColor': False},
   4: {'position': [-8.2776874295134348, -153.0002637800664], 'userColor': None, 'useUserColor': False},
   5: {'position': [-148.0, -152.38362132286352], 'userColor': None, 'useUserColor': False},
   6: {'position': [-142.56841345973373, -56.633147635708241], 'userColor': None, 'useUserColor': False},
   7: {'position': [-130.31249662315372, -225.92807134273727], 'userColor': None, 'useUserColor': False},
   8: {'position': [-32.931849731810416, -228.0], 'userColor': None, 'useUserColor': False},
   9: {'position': [93.0, -58.0], 'userColor': None, 'useUserColor': False},
   10: {'position': [123.0, -217.0], 'userColor': None, 'useUserColor': False},
   11: {  'position': [-3.0, 112.0], 'useUserColor': False, 'userColor': None},
   12: {'position': [272.0, -57.196447909898211], 'userColor': None, 'useUserColor': False},
   13: {'position': [348.0, -204.0], 'userColor': None, 'useUserColor': False},
   14: {'position': [-81.158761100281566, 12.856833441628762], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




