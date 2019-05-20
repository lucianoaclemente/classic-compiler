# coding: utf-8
from classes.analysers.constantdefinition import ConstantDefinition

class Analyser:

    def __init__(self):
        self.constants = []
        
    def repstr(self, string, length):
        return (string * length)[0:length]

    def createConstants(self, subtree, level):
        for child in subtree.children:
            if (type(child).__name__ == "Tree"):
                if (child.data == "constant_definition"):
                    constant = ConstantDefinition(child, level+2)                    
                    self.constants.append(constant)
                else:
                    self.createConstants(child, level+2)
        
    def createDeclarations(self, tree):
        self.createConstants(tree, 0)       