# -*- coding: utf-8 -*-
import getopt
import sys
from jenkinslocal.jenkinsclass import *

if __name__ == '__main__':
    #valida os parametros passados em linha de comando
    #somente dois parametros estão disponiveis, liga e desliga
    # https://docs.python.org/2/library/getopt.html
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:b:ldh", ["help", "output="])
    except Exception as e:
        # usage()
        print(str(e))
        sys.exit(2)

    instanceID = None
    projetojenkins = None
    ligar = None
    desligar = None

    #opts é uma tupla
    for o in opts:
        if o[0] == '-p':
            projetojenkins = o[1]
        elif o[0] == '-b':
            instanceID = o[1]
        elif o[0] == '-l':
            ligar = True
            desligar = False
        elif o[0] == '-d':
            desligar = True
            ligar = False
        else:
            #adicionar modo de usar
            pass
    #projetojenkins,instanceID,liga,desliga
    jk = JenkinsUser()

    if(ligar):
        jk.ligar_instancia(projetojenkins,instanceID,ligar)

    if(desligar):
        jk.desligar_instancia(projetojenkins,instanceID,desligar)

