ano=0
mes=0
dia=0
dian=0
dia=int(input('Dia: '))
mes=int(input('Mês: '))
ano=int(input('Ano: '))
dian = dia +1
mesn = mes +1
if (mes > 0 and mes <= 12):
    if (mes == 12):
        if (dia < 0 or dia > 31):
            print('Dia inválido') 
        elif (dia == 31):
            dia = 1
            mes = 1
            ano = ano + 1
            print('O dia é',dia,', o mês',mes,'e o ano,',ano)
        else:
            print('O dia é',dian,', o mês',mes,'e o ano,',ano)          
    elif ((mes < 7 and ((mes % 2) == 0)) or (mes > 7 and ((mes % 2) != 0))):
        if (dia < 0 or dia > 30):
            print('Dia inválido')         
        elif (mes == 2):
            if ((ano % 4) != 0):
                if (dia < 0 or dia > 28):
                    print('Dia inválido')
                elif (dia == 28):
                    dia = 1
                    print('O dia é',dia,', o mês',mesn,'e o ano,',ano)
                else:
                    print('O dia é',dian,', o mês',mes,'e o ano,',ano)                  
            else:
                if (dia < 0 or dia > 29):
                    print('Dia inválido')
                elif (dia == 29):
                    dia = 1
                    print('O dia é',dia,', o mês',mesn,'e o ano,',ano)
                else:
                    print('O dia é',dian,', o mês',mes,'e o ano,',ano)
        elif (dia == 30):
            dia = 1   
            print('O dia é',dia,', o mês',mesn,'e o ano,',ano)
        else:
            print('O dia é',dian,', o mês',mes,'e o ano,',ano)                                      
    else:
        if (dia < 0 or dia > 31):
            print('Dia inválido')  
        elif (dia == 31):
            dia = 1
            print('O dia é',dia,', o mês',mesn,'e o ano,',ano)
        else:
            print('O dia é',dian,', o mês',mes,'e o ano,',ano)
else:
    print ('Mês inválido')