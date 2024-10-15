# Método que não recebe parâmetro e tem retorno

def getPI():
    return 3.14


# Método que não recebe parâmetro e não tem retorno

def imprimirPI():
    print(3.14)
    

# Método que recebe parâmetro e tem retorno

def calcularAreaCirculo(r):
    area = getPI() * (r * r)
    return area


# Método que recebe parâmetro e não tem retorno

def imprimirAreaCirculo(r):
    print(calcularAreaCirculo(r))
    
imprimirPI()
imprimirAreaCirculo(5.4)