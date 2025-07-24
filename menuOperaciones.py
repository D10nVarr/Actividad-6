def operar_nums(cant_nums):
    nums_sum = 0
    cont=0
    for i in range(cant_nums):
        num=int(input("Ingrese un numero: "))
        nums_sum+=num

    print(f"La suma los {cant_nums} números es {nums_sum}, el promedio es {nums_sum/cant_nums}, ")

#def promediar_nums(cant_nums):
 #   avrg_nums=[]
  #  for i in cant_nums:
   #     print("Ingrese un numero: ")
    #    avrg_nums.append(i)
   # return avrg_nums

nums=int(input("Ingrese la cantidad de numeros: "))

operar_nums(nums)