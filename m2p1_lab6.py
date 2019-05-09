    
'''
classe: m2p1_lab6.py
descricao: Lista os titulos em maiúsculo dos orgãos do Congresso.:
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()
i=1
for comissao in  listJson.orgaos_membros('5973'):

    print('Deputado(a) numero:',i)
    print(comissao['nome'])
    i=i+1
    print()

print("Teve um total de", i-1 ,"deputados participantes")
