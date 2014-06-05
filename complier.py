# -*- coding: utf-8 -*-
#token分类
TOKEN_STYLE = ['KEY_WORD', 'IDENTIFIER', 'DIGIT_CONSTANT','OPERATOR', 'SEPARATOR', 'STRING_CONSTANT']

DETAIL_TOKEN_STYLE = {'abstract':'ABSTRACT', 'assert':'ASSERT', 'boolean':'BOOLEAN', 'break':'BREAK', 
'byte':'BYTE', 'case':'CASE', 'catch':'CATCH', 'char':'CHAR', 'class':'CLASS', 'const':'CONST', 
'continue':'CONTINUE', 'default':'DEFAULT', 'do':'DO', 'double':'DOUBLE', 'else':'ELSE', 'enum':'ENUM', 
'extends':'EXTENDS', 'final':'FINAL', 'finally':'FINALLY', 'float':'FLOAT', 'for':'FOR', 'if':'IF', 
'implements':'IMPLEMENTS', 'import':'IMPORT', 'instanceof':'INSTANCEOF', 'interface':'INTERFACE', 
'package':'PACKAGE', 'short':'SHORT', 'int':'INT', 'long':'LONG', 'while':'WHILE', 'return':'RETURN', 
'switch':'SWITCH', 'native':'NATIVE', 'private':'PRIVATE', 'protected':'PROTECTED', 'public':'PUBLIC', 
'static':'STATIC', 'synchronized':'SYNCHRONIZED', 'transient':'TRANSIENT', 'volatile':'VOLATILE', 
'new':'NEW', 'this':'THIS', 'super':'SUPER', 'void':'VOID', 'byValue':'BYVALUE', 'cast':'CAST', 
'false':'FALSE', 'future':'FUTURE', 'generic':'GENERIC', 'inner':'INNER', 'operator':'OPERATOR',
 'outer':'OUTER', 'rest':'REST', 'true':'TRUE', 'var':'VAR','goto':'GOTO','null':'NULL' 
 }

print DETAIL_TOKEN_STYLE
