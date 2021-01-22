# coding: utf-8
from lark import Lark, Transformer

class EBNF:
    def __init__(self, filename):
        self.ebnf = open(filename, mode="r", encoding="utf-8")
        self.grammar = self.ebnf.read()
        self.parser = Lark(self.grammar, start="program", keep_all_tokens="false")
        
    def parse(self, program):
        program = open(program, mode="r", encoding="utf-8")        
        code = program.read()
        tree = self.parser.parse(code)
        
        return tree
    