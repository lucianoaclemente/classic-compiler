# coding: utf-8
from classes.analysers.constantdefinition import ConstantDefinition
from classes.analysers.includedirective import IncludeDirective

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

    def createInclude(self, subtree, level, include):
        for child in subtree.children:
            if (type(child).__name__ == "Tree"):
                if (child.data == "include_directive"):
                    filename = IncludeDirective(child, level+2)
                    include.append(filename)
                else:
                    self.createInclude(child, level+2, include)

                    
    def checkIncludes(self, tree, include):
        self.createInclude(tree, 0, include)
        
    def checkDeclarations(self, tree):
        self.createConstants(tree, 0)

        
        