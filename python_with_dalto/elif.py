ingreso_mensual_USD = 11000
egreso_mensual_USD = 11999


if ingreso_mensual_USD > 10000:
    if ingreso_mensual_USD - egreso_mensual_USD >= 3000:
        print('Bien estas ahorrando, puedes vivir tranquilo')
    elif ingreso_mensual_USD - egreso_mensual_USD >= 500:
        print("Estas bien, pero cuidado que te estas quedando algo apretado")
    elif ingreso_mensual_USD - egreso_mensual_USD < 0:
        print("Estas en deficit")    
    else:
        print("estas gastando full man, hay que ver si te alcanza")
elif ingreso_mensual_USD >= 5000: 
    print('Estas bien en EEUU')
elif ingreso_mensual_USD >= 2500: 
    print('Estas bien en Latinoamerica')
elif ingreso_mensual_USD >= 1000: 
    print('Estas medio jodido')
elif ingreso_mensual_USD >= 500: 
    print('Estas bastante jodido')                
else:
    print('Estas en la M')