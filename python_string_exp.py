# Python string examples.
singlequote = 'Python Learning'

doublequote = "Machine Learning"

triplequote = """---"""

# Strng slicing
print(singlequote[:])                
print(doublequote[:])
print(triplequote[:])

# new strings can be reassigned to the same name
name = 'python'
name = 'python programing'

print(name)

# Con't deleate and update a string but use build-in function del to remove string.
str_name=''
del str_name

# Formatting of Strings
"{} {} {}".format('Geeks', 'For', 'Life')
"{1} {0} {2}".format('Geeks', 'For', 'Life')
"{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
"{0:b}".format(16) # Formatting of Integers
"{0:e}".format(165.6458) # Formatting of Floating
"{0:.2f}".format(1/6) #  Rounding off Integers 

# String methods examples
str = "Python Machine Learning"

print('***********String upper case examples*****************')
# uppercase
print("string is uppercase   : ",str.isupper())
print("string into uppercase : ",str.upper())
upper = str.upper()
print("string in uppercase   : ",upper.isupper())
print()
print('***********String lowser case exp*********************')
# uppercase
print("String is lowercase   : ",str.islower())
print("string into lowercase : ",str.lower())
lower = str.lower()
print("string in lowercase   : ",lower.islower())
print('******************************************************')

name = 'devi'
empid = 'TS638375'
sal = '25000'

print("Emp Name is alpha :",name.isalpha())
print("Emp Name is alpha numeric :",name.isalnum())
print("Emp sal is decimal :",sal.isdecimal())
# str.space()
# str.title()
# str.startswith('python')
# str.endswith('learning')
# str.find('Python')
# str.strip()
# str.lstrip()
# str.rstrip()
# str.center()
# str.ljust()
# str.rjust()
# str.index('p') 
# str.split()
# str.replace('Machine','AI')
# len(str)
# print(''.join(reversed(name)))
# str1.join(str2)
# str.count()
print('******************************************************')



