
# ( número de peças, valor de peças < limite , valor de peças > limite)
def mult(pecas, vMin, vMax):
    limite=5 # até 5 peças vMin, depois vMax
    pecas= int(pecas)
    if pecas > limite:
        rMult= (limite*vMin)+((pecas-limite)*vMax)
    else:
        rMult= pecas*vMin
    return rMult

# ( int numero de pecas, string tipo de peca em maiuscula)
def calculaPecas(pecas, tipoPeca):
  #valor das peças B C D e M primeiras (< limite) e ultimas (>limite) de forma que possa ser alterado nem q manualmente aqui no código
    
  valorBCDM_p=100 
  valorBCDM_u=75
    
    #valor das peças A primeiras (<limite) e ultimas (>limite) de forma que possa ser alterado nem q manualmente aqui no código
    
  valorA_p=350 
  valorA_u=300
    
    # identifica o tipo da peça, caso no futuro haja alteração individual só adicionar novas variaveis referentes
  if tipoPeca== "A":
    valorPecas= mult(pecas,valorA_p,valorA_u)
  elif tipoPeca== "B" or tipoPeca=="C" or tipoPeca=="D" or tipoPeca=="M":
    valorPecas= mult(pecas,valorBCDM_p,valorBCDM_u)
  else :
    return "erro"
  maoDeObra = 400
  valorIron = valorPecas
  valorPecas = valorPecas + maoDeObra
  return [valorPecas, maoDeObra, valorIron]
