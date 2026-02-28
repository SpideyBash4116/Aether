import re
import sys

# --- LEXER (The Scanner) ---
# Converts raw text into a stream of meaningful tokens.
TOKEN_TYPES = [
    ('NUMBER',  r'\d+(\.\d+)?'),      # Integers or Floats
    ('STRING',  r'"[^"]*"'),          # String literals
    ('ASSIGN',  r':='),               # Go-style declaration
    ('EQUALS',  r'='),                # Re-assignment
    ('PLUS',    r'\+'),               # Operations
    ('MINUS',   r'-'),
    ('MUL',     r'\*'),
    ('DIV',     r'/'),
    ('LPAREN',  r'\('),
    ('RPAREN',  r'\)'),
    ('IDENT',   r'[a-zA-Z_][a-zA-Z0-9_]*'), # Variables/Keywords
    ('NEWLINE', r'\n'),
    ('SKIP',    r'[ \t]+'),           # Spaces and tabs
    ('ERROR',   r'.'),                # Catch-all for illegal chars
]

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def lex(code):
    tokens = []
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)
    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP': continue
        elif kind == 'ERROR': raise SyntaxError(f"Illegal character: {value}")
        tokens.append(Token(kind, value))
    return tokens

# --- PARSER (The Architect) ---
# Turns tokens into an Abstract Syntax Tree (AST).
class ASTNode: pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

class Num(ASTNode):
    def __init__(self, value):
        self.value = float(value)

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

class Assign(ASTNode):
    def __init__(self, name, value, is_decl):
        self.name, self.value, self.is_decl = name, value, is_decl

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type=None):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if expected_type and token.type != expected_type:
                raise SyntaxError(f"Expected {expected_type}, got {token.type}")
            self.pos += 1
            return token
        return None

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse_expression(self):
        # Handles addition and subtraction
        node = self.parse_term()
        while self.peek() and self.peek().type in ('PLUS', 'MINUS'):
            op = self.consume().type
            node = BinOp(node, op, self.parse_term())
        return node

    def parse_term(self):
        # Handles multiplication and division
        node = self.parse_factor()
        while self.peek() and self.peek().type in ('MUL', 'DIV'):
            op = self.consume().type
            node = BinOp(node, op, self.parse_factor())
        return node

    def parse_factor(self):
        token = self.consume()
        if token.type == 'NUMBER': return Num(token.value)
        if token.type == 'IDENT': return Var(token.value)
        if token.type == 'LPAREN':
            node = self.parse_expression()
            self.consume('RPAREN')
            return node

    def parse_statement(self):
        token = self.peek()
        if token.type == 'IDENT':
            name = self.consume().value
            next_t = self.peek()
            if next_t and next_t.type == 'ASSIGN': # Go-style :=
                self.consume()
                return Assign(name, self.parse_expression(), is_decl=True)
            elif next_t and next_t.type == 'EQUALS': # Standard =
                self.consume()
                return Assign(name, self.parse_expression(), is_decl=False)
        return self.parse_expression()

# --- INTERPRETER (The Executioner) ---
class Interpreter:
    def __init__(self):
        self.globals = {}

    def visit(self, node):
        if isinstance(node, Num): return node.value
        if isinstance(node, Var):
            if node.name not in self.globals:
                raise NameError(f"Undefined variable: {node.name}")
            return self.globals[node.name]
        if isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == 'PLUS': return left + right
            if node.op == 'MINUS': return left - right
            if node.op == 'MUL': return left * right
            if node.op == 'DIV': return left / right
        if isinstance(node, Assign):
            val = self.visit(node.value)
            if node.is_decl and node.name in self.globals:
                raise NameError(f"Variable '{node.name}' already declared (use = to update)")
            self.globals[node.name] = val
            return val

# --- MAIN INTERFACE ---
def run_aether():
    interpreter = Interpreter()
    print("Aether v1.0 [Python Heart / Go Bones]")
    while True:
        try:
            text = input("ae> ")
            if not text or text.lower() == 'exit': break
            tokens = lex(text)
            parser = Parser(tokens)
            ast = parser.parse_statement()
            result = interpreter.visit(ast)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_aether()
