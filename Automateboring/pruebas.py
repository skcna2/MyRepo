import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumberRegex.search("My numero es 444-234-5677")

print("The phone numbr found: " + mo.group())

print(mo.group(0) == mo.group())

phoneNumberRegexpar = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumberRegexpar.search("My número es 444-244-5555 ")
print(mo.group(1)) #muestra el contenido del primer parentesis  
print(mo.group(2)) #muestra el contenido del segundo parentesis
print(mo.group(0)) #muestra 
print(mo.groups()) #muestra todos los grupos

areaCode, mainNumber = mo.groups()

print(areaCode)
print(mainNumber)


