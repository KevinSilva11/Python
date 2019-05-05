def compra(valor,qtd,desc):
        parcial = valor * qtd
        desconto = (parcial * desc / 100)
        total = parcial - desconto
        return total


        
