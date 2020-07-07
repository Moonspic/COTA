#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:01:04 2020

#=================================== Project COTA ==============================================
#===================================    V0.01     ==============================================

# COTA or "Computational Ontological Transactional Algebra" is a framework that is based on the paper 
#"Ontological Algebra"  on Moonspic.org
@author: Bahaa Eiz (Moonspic.org)
"""

import numpy as np 
import math 


INFT_TYPE = 'inf_'
ZERO_TYPE = '0_'
REAL_TYPE='Real'
DOMAIN_TYPE={'INFT_TYPE':'inf_','ZERO_TYPE':'0_','REAL_TYPE': 'Real' }

DOMAIN_LIST = [INFT_TYPE,ZERO_TYPE, REAL_TYPE]


def Denote_OntDom(x,OntDim=None):
    res = None
    npArr = type(np.array([0]))
    
    #TODO: Add class 
    if type(x)==str or type(x) == np.float64 or type(x)== np.int64 or type(x)==float or type(x)==int :
        if OntDim == ZERO_TYPE or OntDim =="ZERO_TYPE" or OntDim== 0 or OntDim=='0' or OntDim=='zero' or OntDim=='Zero':
            res="0_{}".format(x)
            
        elif OntDim == INFT_TYPE or OntDim =="INFT_TYPE" or OntDim== float("inf") or OntDim=='inf' or OntDim=='Inf' or OntDim==math.inf:
            res="inf_{}".format(x)
            
        elif OntDim== REAL_TYPE or OntDim=="REAL_TYPE" or OntDim== None or OntDim=='Real' or OntDim=='REAL' or OntDim=='R':
            res=x
    
    elif type(x)==list or type(x)==npArr:
        
        res = []
        for  e in x:
            res.append(Denote_OntDom(e,OntDim))
        if type(x)==npArr:
            res = np.array(res)
    return res


def GetOntDomain(x, notation=DOMAIN_TYPE, ReturnRealType=False):
    Res = 'Invalid'
    if type(x)!=str:
        if ReturnRealType:
            Res = type(x).__name__
        else:
            #Res = DOMAIN_TYPE['REAL_TYPE']
            Res = 'REAL_TYPE'
    else:
        for k,v in notation.items():
            if v in x:
                try:
                    num = RetriveDomain_Numeric(x,v)
                    if type(num)==float or type(num)==int:
                        Res = k
                    else:
                        Res='Invalid'
                except:
                    Res= 'Invalid' 
    return Res 
                


def RetriveDomain_Numeric(x, floatType=True):
    
    if type(x)!=str:
        num=x 
    #keywords:
    elif x=='inf' or x=='INF':
        num = math.inf
    
    elif 'inf_' in x: 
        num = float(x[4-len(x)])
    elif '0_' in x:
        num =float(x[2-len(x)])

    return num 
                

def Mul_Ont(a,b):
    Result='invalid'
    a_domain = GetOntDomain(a)
    b_domain = GetOntDomain(b)


    a_num= RetriveDomain_Numeric(a)
    b_num = RetriveDomain_Numeric(b)
    
    
    #Both same
    if a_domain == b_domain:
        #print("both are the same")
        r = a_num * b_num
        #print(r)
        Result = Denote_OntDom(r,a_domain)
        #print(Result)
        
        
    #Any is real other domain is dominant
    elif a_domain=="REAL_TYPE":
        #print("one is real")
        GovDom_type = b_domain
        r = a_num * b_num
        Result = Denote_OntDom(r, GovDom_type)
        
    elif b_domain=="REAL_TYPE":
        #print("one is real")
        GovDom_type = a_domain
        r = a_num * b_num
        Result = Denote_OntDom(r, GovDom_type)        
    
    elif (a_domain=="INFT_TYPE" and b_domain == "ZERO_TYPE") or (b_domain=="INFT_TYPE" and a_domain == "ZERO_TYPE"):
        
        #print("Onto")
        if a_num == b_num:
            Result = Denote_OntDom(a_num) #Real
        else:
            Result=="OTHER"
    
    print("Result {}".format(Result))
    return Result
        
def Div_Ont(a,b):
    Result='OTHER'
    a_domain = GetOntDomain(a)
    b_domain = GetOntDomain(b)


    a_num= RetriveDomain_Numeric(a)
    b_num = RetriveDomain_Numeric(b)
    
    
    #Both same
    if a_domain == b_domain:
        #print("both are the same")
        if b==0:
            Result = Denote_OntDom(a_num, "INFT_TYPE")
        else:
            r = a_num / b_num
            #print(r)
            Result = Denote_OntDom(r,a_domain)

        
    elif a_domain=="REAL_TYPE" :
        if b=='inf' or b==math.inf:
        #print("one is real")
            Result = Denote_OntDom(a_num, "ZERO_TYPE")     
    return Result


def Add_Ont(a,b):
    Result='invalid'
    a_domain = GetOntDomain(a)
    b_domain = GetOntDomain(b)


    a_num= RetriveDomain_Numeric(a)
    b_num = RetriveDomain_Numeric(b)
    
    
    #Both same
    if a_domain == b_domain:
        #print("both are the same")
        r = a_num + b_num
        #print(r)
        Result = Denote_OntDom(r,a_domain)
        #print(Result)
    return Result


def Sub_Ont(a,b):
    Result='invalid'
    a_domain = GetOntDomain(a)
    b_domain = GetOntDomain(b)


    a_num= RetriveDomain_Numeric(a)
    b_num = RetriveDomain_Numeric(b)
    
    
    #Both same
    if a_domain == b_domain:
        #print("both are the same")
        r = a_num - b_num
        #print(r)
        Result = Denote_OntDom(r,a_domain)
        #print(Result)
    return Result

