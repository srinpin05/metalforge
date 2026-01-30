#Lexer has to take the input string and convert into a flat list of tokens
code = """
X = 5
if (X==5)
    print 'Hello'
print 'hi'
"""
def lex(source: str) -> list[str]:
    tokens = []
    i = 0
    j = 0
    while i < len(source):
        char = source[i]
        if source[i].isspace():
            i+=1
        elif source[i].isdigit():
            j = i
            while j < len(source) and source[j].isdigit():
                j+=1
            word = source[i:j]    
            i = j
            tokens.append(("INT", word))
        elif source[i] == "+":
            tokens.append(("ADD", source[i]))
            i+=1
        elif source[i] == "-":
            tokens.append(("SUB", source[i]))
            i+=1
        elif source[i] == "*":
            tokens.append(("MULT", source[i]))
            i+=1
        elif source[i] == "/":
            tokens.append(("DIV", source[i]))
            i+=1
        elif source[i] == "(":
            tokens.append(("LP", source[i]))
            i+=1
        elif source[i] == ")":
            tokens.append(("RP", source[i]))
            i+=1
        elif source[i] == "<":
            tokens.append(("LT", source[i]))
            i+=1
        elif source[i] == ">":
            tokens.append(("GT", source[i]))
            i+=1
        elif source[i] == "=":
            if source[i+1] == "=":
                tokens.append(("BOOLEQS", source[i:i+2]))
                i+=2
            else:
                tokens.append(("EQS", source[i]))
                i+=1
        elif source[i] == "'":
            i+=1
            j = i
            while j < len(source) and source[j] != "'":
                j+=1
            word = source[i:j]
            tokens.append(("STR", word))
            i = j + 1
        elif source[i].isalpha():
            j = i
            while j < len(source) and source[j].isalnum():
                j+=1
            word = source[i:j]    
            i = j
            if word == "print":
                tokens.append(("PRINT", word))
            elif word == "if":
                tokens.append(("IF", word))
            elif word == "else":
                tokens.append(("ELSE", word))
            else:
                tokens.append(("IDENT", word))
        else:
            raise SyntaxError(f"unexpected character: {source[i]}")
    return tokens
print(lex(code))

#AST nodes

from dataclasses import dataclass

@dataclass
class If:
    condition: any
    body: list

@dataclass
class Print:
    value: any

@dataclass
class Int:
    value: int

@dataclass
class Var:
    name: str

@dataclass
class Assign:
    name: Var
    value: any

@dataclass
class BinOp:
    left: any
    op: str
    right: any



#Parser: need to take tokens and create ASTs
