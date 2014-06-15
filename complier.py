# -*- coding: utf-8 -*-
import re
import sys
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
'false':'FALSE', 'true':'TRUE','null':'NULL','<': 'LT', '>': 'GT', 
 '++': 'SELF_PLUS', '--': 'SELF_MINUS', '+': 'PLUS', '-': 'MINUS', '*': 'MUL', '/': 'DIV', '>=': 'GET', '<=': 'LET', 
 '(': 'LL_BRACKET',    ')': 'RL_BRACKET', '{': 'LB_BRACKET', '}': 'RB_BRACKET', '[': 'LM_BRACKET', ']': 'RM_BRACKET', 
 ',': 'COMMA', '\"': 'DOUBLE_QUOTE', ';': 'SEMICOLON', '#': 'SHARP'}

# 关键字
keywords = [['int', 'float', 'double', 'char', 'void'],
           ['if', 'for', 'while', 'do', 'else'], ['import', 'return']]
# 运算符
operators = ['=', '&', '<', '>', '++', '--',
             '+', '-', '*', '/', '>=', '<=', '!=']
# 分隔符
delimiters = ['(', ')', '{', '}', '[', ']', ',', '\"', ';']

# 文件名字
file_name = None
# 文件内容
content = None

class Token(object):
    '''记录分析出来的单词'''

    def __init__(self, type_index, value):
        self.type = DETAIL_TOKEN_STYLE[value] if type_index == 0 or type_index == 3 or type_index == 4 else TOKEN_STYLE[type_index]
        self.value = value


class Lexer(object):
    '''词法分析器'''

    def __init__(self):
        # 用来保存词法分析出来的结果
        self.tokens = []

    # 判断是否是空白字符
    def is_blank(self, index):
        return content[index] == ' ' or content[index] == '\t' or content[index] == '\n' or content[index] == '\r'

    # 跳过空白字符
    def skip_blank(self, index):
        while index < len(content) and self.is_blank(index):
            index += 1
        return index

    # 打印
    def print_log(self, style, value):
        print '(%s, %s)' % (style, value)

    # 判断是否是关键字
    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    # 词法分析主程序
    def main(self):
        i = 0
        while i < len(content):
            i = self.skip_blank(i)

            # 如果是字母或者是以下划线开头
            if content[i].isalpha() or content[i] == '_':
                # 找到该字符串
                temp = ''
                while i < len(content) and (content[i].isalpha() or content[i] == '_' or content[i].isdigit() or content[i] == '*' or content[i] == '.'):
                    temp += content[i]
                    i += 1
                # 判断该字符串
                if self.is_keyword(temp):
                    # self.print_log( '关键字', temp )
                    self.tokens.append(Token(0, temp))
                else:
                    # self.print_log( '标识符', temp )
                    self.tokens.append(Token(1, temp))
                i = self.skip_blank(i)
            # 如果是数字开头
            elif content[i].isdigit():
                temp = ''
                while i < len(content):
                    if content[i].isdigit() or (content[i] == '.' and content[i + 1].isdigit()):
                        temp += content[i]
                        i += 1
                    elif not content[i].isdigit():
                        if content[i] == '.':
                            print 'float number error!'
                            exit()
                        else:
                            break
                # self.print_log( '常量' , temp )
                self.tokens.append(Token(2, temp))
                i = self.skip_blank(i)
            # 如果是分隔符
            elif content[i] in delimiters:
                # self.print_log( '分隔符', content[ i ] )
                self.tokens.append(Token(4, content[i]))
                # 如果是字符串常量
                if content[i] == '\"':
                    i += 1
                    temp = ''
                    while i < len(content):
                        if content[i] != '\"':
                            temp += content[i]
                            i += 1
                        else:
                            break
                    else:
                        print 'error:lack of \"'
                        exit()
                    # self.print_log( '常量' , temp )
                    self.tokens.append(Token(5, temp))
                    # self.print_log( '分隔符' , '\"' )
                    self.tokens.append(Token(4, '\"'))
                i = self.skip_blank(i + 1)
            # 如果是运算符
            elif content[i] in operators:
                # 如果是++或者--
                if (content[i] == '+' or content[i] == '-') and content[i + 1] == content[i]:
                    # self.print_log( '运算符e', content[ i ] * 2 )
                    self.tokens.append(Token(3, content[i] * 2))
                    i = self.skip_blank(i + 2)
                # 如果是>=或者<=
                elif (content[i] == '>' or content[i] == '<') and content[i + 1] == '=':
                    # self.print_log( '运算符', content[ i ] + '=' )
                    self.tokens.append(Token(3, content[i] + '='))
                    i = self.skip_blank(i + 2)
                # 其他
                else:
                    self.print_log( '运算符', content[ i ] )
                    self.tokens.append(Token(3, content[i]))
                    i = self.skip_blank(i + 1)

    

if __name__ == '__main__':
    file_name = sys.argv[1]
    source_file = open(file_name)
    content = source_file.read()
    lexer = Lexer()
    lexer.main()
    for token in lexer.tokens:
        print '(%s, %s)' % (token.type, token.value)

