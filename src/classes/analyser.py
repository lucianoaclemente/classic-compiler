# coding: utf-8

from classes.analysers.includeAnalyser import IncludeAnalyser

class Analyser:

    def __init__(self):
        self.constants = []
        self.statement_keys = [
            'label_identifier',
            'constant_definition',
            'type_definition',
            'variable_declaration',
            'procedure_declaration',
            'function_declaration',
            'assignment_statement',
 
        ]
          
    def repstr(self, string, length):
        return (string * length)[0:length]

    # ===========================================================================================
    # Check include files 
    # ===========================================================================================
    def checkInclude(self, subtree, level, include):
        for child in subtree.children:
            if (type(child).__name__ == "Tree" ):
                if (child.data == "include_directive"):
                    filename = IncludeAnalyser(child, level+2)
                    include.append(filename)
                else:
                    self.checkInclude(child, level+2, include)

        return include
                    
    def checkIncludes(self, tree):
        result = []        
        self.checkInclude(tree, 0, result)        
        return result     
        
    # ===========================================================================================
    # Scan and check tree
    # =========================================================================================== 
    def analyse(self, tree, statements):
        for child in tree.children:
            if (type(child).__name__ == "Tree" ):
                if (child.data in self.statement_keys):
                    if (child.data not in statements):
                        statements[child.data] = []     

                    statements[child.data].append(child)                    
                else:
                    self.analyse(child, statements)

        return statements
