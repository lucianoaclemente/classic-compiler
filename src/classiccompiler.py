# coding: utf-8
# poedit
import sys
import getopt
import os
import gettext as gt
import linecache

from classes.common import Common
from classes.compiler import Compiler
from classes.project import Project
from classes.helpers.labelmanager import LabelManager

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(_("Ocorreu um erro: (%s, linha %s '%s'): %s") % (filename, lineno, line.strip(), exc_obj))

myopts, args = getopt.getopt(sys.argv[1:],"p:")

project_path = ""

for option, value in myopts:
    if option == '-p':
        project_path = value
    else:
        print("Uso: %s -p project_path" % sys.argv[0])
        break

try:
    Common.params["root_path"] = os.path.dirname(sys.modules['__main__'].__file__)
    Common.params["project_path"] = project_path
    
    lang = gt.translation('classiccompiler', localedir=os.path.join(Common.params["root_path"], 'locale'), languages=['pt_BR'])
    lang.install()
	
    project = Project()
    
    print(_("Compilando..."))
    print(_("Máquina: %s, CPU: %s") % (project.machine["name"], project.machine["cpu"]))

    compiler = Compiler(project)
    compiler.compile()
	
    for file in compiler.files:
        text_file = open("tree_" + file[0].replace('.','_') + ".txt", "w")
        text_file.write(file[1].pretty())
        text_file.close()

    #print(Common.identifiers)
    #print(compiler.analyser.constants)
    #for item in compiler.analyser.constants:
    #    print(item)
   
    print(_("Compilação concluída!"))
    
except:
    PrintException()










