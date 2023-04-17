#Empresa: vendedores= 13% de comision de las ventas   nombre y cuanto han vendid


nombre= input('Ingrese su nombre: ')
ventas= float(input('Ingrese sus ventas: '))

comision= ventas*0.13
redondeada= round(comision, 2)

print(f'{nombre}, su comisión por {ventas} euros en ventas alcanza los {redondeada} euros')




