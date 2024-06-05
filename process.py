# -*- coding: utf-8 -*-

import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)
sys.path.append(".")

from simre.init_models import main

if __name__ == '__main__':  
    
    nameReq = sys.argv[1] 
    
    if nameReq == 'init':
        main()
    else:
        from simre.similarity import similarity_process
        
        nameFeat = sys.argv[2]
        nameDesc = sys.argv[3]   
        lang = sys.argv[4]
        
        if len(sys.argv) > 5:
            listModelos_final = [int(i) for i in sys.argv[5].split(',')]
        else:
            listModelos_final = [1]
        if len(sys.argv) > 6:
            threshold = sys.argv[6]
        else:
            threshold = 0.7
        if len(sys.argv) > 7:
            preprocess = sys.argv[7]
        else:
            preprocess = True
        
        print('parámetros',nameReq,nameFeat,nameDesc,lang, threshold,listModelos_final,preprocess)
        similarity_process(nameReq, nameFeat, nameDesc, lang, [], listModelos_final, float(threshold), preprocess)   
            
    
