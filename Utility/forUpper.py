# -*- coding: utf-8 -*-
# 用来生成关键字的键值对
#还有些空格问题,用sublime或者vim可以轻松搞定
import re
string ='''
 'abstract','assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for', 'if', 'implements', 'import', 'instanceof', 'interface', 'package', 'short', 'int', 'long', 'while', 'return', 'switch', 'native', 'private', 'protected', 'public', 'static', 'synchronized', 'transient', 'volatile', 'new', 'this', 'super', 'void', 'byValue', 'cast', 'false', 'future', 'generic', 'inner', 'operator', 'outer', 'rest', 'true', 'var','goto','null' 
 '''
m = re.split(',',string)
for word in m:
	print word,':',word.upper(),',',

