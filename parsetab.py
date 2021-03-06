
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BACKSLASH LPAREN RPAREN VARIABLE Program : Term  Term : '(' Term ')'  Term : VARIABLE  Term : Term Term  Term : BACKSLASH VARIABLE '.' Term "
    
_lr_action_items = {'(':([0,2,3,4,6,7,9,10,11,],[3,3,3,-3,3,3,-2,3,3,]),'VARIABLE':([0,2,3,4,5,6,7,9,10,11,],[4,4,4,-3,8,4,4,-2,4,4,]),'BACKSLASH':([0,2,3,4,6,7,9,10,11,],[5,5,5,-3,5,5,-2,5,5,]),'$end':([1,2,4,6,9,11,],[0,-1,-3,-4,-2,-5,]),')':([4,6,7,9,11,],[-3,-4,9,-2,-5,]),'.':([8,],[10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Term':([0,2,3,6,7,10,11,],[2,6,7,6,6,11,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Term','Program',1,'p_start','parser.py',19),
  ('Term -> ( Term )','Term',3,'p_paren','parser.py',23),
  ('Term -> VARIABLE','Term',1,'p_variable','parser.py',27),
  ('Term -> Term Term','Term',2,'p_application','parser.py',31),
  ('Term -> BACKSLASH VARIABLE . Term','Term',4,'p_abstraction','parser.py',35),
]
