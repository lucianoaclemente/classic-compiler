# coding: utf-8
class LabelManager:

    identifiers = {}

    prefix = {
        'start':'S',
        'program':'P',
        'library':'L',
        'data':'D',
        'variable':'V',
        'constant':'C'    
    }

    counters = {
        'start':0,
        'program':0,
        'library':0,
        'data':0,
        'variable':0,
        'constant':0    
    }

    def __init__(self):
        None
        
    def next(type, key):
        if key not in LabelManager.identifiers:    
            LabelManager.counters[type] += 1      
            LabelManager.identifiers[key] = LabelManager.prefix[type] + str(LabelManager.counters[type]).zfill(5) 
        else:
            raise Exception(_("O identificador %s já existe") % key)   