a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('O valor tem alfanúmerico? ', a.isalnum())
print('O valor só tem números? ', a.isnumeric())
print('O valor tem espaços? ',a.isspace())
print('O valor é somente letra? ', a.isalpha())
print('O valor tem somente letras maíusculas? ', a.isupper())
print('O valor tem  somente letras minusculas? ', a.islower())
print('O valor é um número decimal? ', a.isdecimal())
print('O valor está capitalizado? ', a.istitle())
