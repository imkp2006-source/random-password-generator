import random
import string 
#string.ascii_letters  , string.digits , string.puncuations 
pass_len = int(input("Enter the length of your password:"))
charvalues = string.ascii_letters + string.digits + string.punctuation
password =  ""

#List comprehension[function for i in  range(n)] to convatenate use ."string"join()

res ="X".join([random.choice(charvalues) for i in range(pass_len)])

"""
for i in  range(pass_len):
    password += random.choice(charvalues)
"""
print("your random password is:", res)
