# Оператор is: a is b -> a и b - один и тот же объект

my_refregirator = ['колбаса', 'сыр', 'масло']
his_refregirator = ['колбаса', 'сыр', 'масло']
his_refregirator = my_refregirator.copy() #[:]
my_refregirator += ['мясо']
print(his_refregirator)
print(my_refregirator is his_refregirator)
print(my_refregirator == his_refregirator)
print(id(my_refregirator) == id(his_refregirator))
temp = 1
print(type(temp))
print(temp is None)



#a = {'a' : 1}
#print(id(d))
#d['a'] += 1
#print(id(d))

#def print_goodbye(arg):
   # print ('Goodbye', end ='')

#def print_cruel(arg):
  #  print('cruel', end='')

#def print_world(arg):
   # print('world', end='')


#def main():
   # print_goodbye(1)
   # print_cruel(2)
  #  print_world(3)

#main()




#def generate_list():
   # for i in range(5):
       # yield i # генератор (возвращает, но не завершает)


#array = tuple(generate_list())

#print(array)


