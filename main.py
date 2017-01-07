import ply.lex as lex
import ply.yacc as yacc
import database as db

tokens = (
	'NUMBER', 'SIZE', 'COLOR', 'KIND', 'ACTION'
	)
# Tokens
t_ACTION = r'db|list'

def t_NUMBER(t):
	r'[\+]{0,1}[0-9]+[\.][0-9]+|[\+]{0,1}[0-9]+'
	print(t.type, t.value)
	return t

def t_SIZE(t):
	r'[SML]|XL'
	print(t.type, t.value)
	return t

def t_COLOR(t):
	r'blue|red'
	print(t.type, t.value)
	return t

def t_KIND(t):
	r'jerse(y|ys)|shorts|shir(t|ts)'
	print(t.type, t.value, '\n')
	return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def p_expression(p):
    '''expression : actionRule
				  | mainRule'''

def p_mainRule(p):
	'''mainRule :  NUMBER SIZE COLOR KIND'''
	db.addElement(p)

def p_actionRule(p):
	'''actionRule :  ACTION'''
	if p[1] == "db":
		db.showDatabase()
	else:
		db.showDatabaseHumanReadable()

def p_error(p):
	print("^--------------- Failure")

parser = yacc.yacc()

while True:
    try:
        s = input('~$ ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
