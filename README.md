# Infix-Evaluation
Infix input seperated by spaces and output should be result of operation
using 2 stacks in python i implement infix input and output would be a result of mathmatic operation
operation like this : 55 - 3 * 2 
  operand    operators
   stack       stack
   | 55 |      | e |
   | 55 |      | + |
 |(55)(3)|     | + |
 |(55)(3)|    |(-)(*)|
|(55)(3)(2)|  |(-)(*)|
 |(55)(6)|     |(-)|
   | 49 |      | e |
  
  output should be last operand pushed in stack of operands
  output = 49
