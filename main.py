#Grafico uno
#Lista de tokens 
#( 10
#) 20
#or 30
#and 40
#not 50
#True 60
#False 70

#palabra reservadas:
#expresion_logica, termino, factor


def graf1(tokens):
    error = ''
    i=0
    i,error = expresion_logica(tokens,i)
    if error !='';
        return error
    return 'Valido'
    
def expresion_logica(tokens,i):
    if i<len(tokens) and tokens[i] == 10:
        i=i=1

        while i<len(tokens):
            
            if tokens[i] in [30,40]:
               i=i+1
            else:
                break
            
            i,error = termino(tokens,i)
            if error !='';
                return i, error
            
        i,error = termino(tokens,i)
        if error !='';
            return i, error
        


        
    else:
        return i, 'Se esperaba un abrir parentesis'
    
