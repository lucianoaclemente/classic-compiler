# coding: utf-8
# poedit
import sys, getopt
import gettext as gt
import linecache

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
        print("Usage: %s -p project_path" % sys.argv[0])
        break

try:
    lang = gt.translation('classiccompiler', localedir='locale', languages=['pt_BR'])
    lang.install()
	
    project = Project(project_path)
    
    print(_("Compilando..."))
    print(_("Máquina: %s, CPU: %s") % (project.machine["name"], project.machine["cpu"]))

    compiler = Compiler(project)
    compiler.compile()
	
    #print(compiler.files)
    #print(LabelManager.identifiers)
    #for item in compiler.analyser.constants:
    #    print(item.value)
    
    
    print(_("Compilação concluída!"))
    
except:
    PrintException()










