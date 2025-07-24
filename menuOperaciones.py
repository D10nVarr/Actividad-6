def operar_nums(cant_nums):
    nums_sum = 0
    count_pst=0
    count_ngt=0
    for i in range(cant_nums):
        num=int(input("Ingrese un numero: "))
        nums_sum+=num
        if num<0:
            count_pst+=1
        else:
            count_ngt+=1
    print(f"La suma los {cant_nums} números es {nums_sum}, el promedio es {nums_sum/cant_nums}, existen {count_pst} numeros por positivos y {count_ngt} negativos")


nums=int(input("Ingrese la cantidad de numeros: "))

operar_nums(nums)