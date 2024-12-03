data=[10,501,22,37, 100, 999, 87, 351]
result=filter(lambda x:x>4, data)
print(list(result))

elements=[2,3,4,5,6]
result=list(map(lambda x:x%2==0, elements))
print("check if each element is even", result)
elements=["Apple", "banana", "Grapes","Apricot"]
result=list(map(lambda x:x.startswith ('A'), elements))
print("check if each elements starts with ('A')':", result)


#import re
#def validate_input(input_value,input_type):"



#Email="aksgeethu@mail.com
#bd_mobile="+8599646576545"
telephone_USA=+1252568645
password="AksGeethu@15"
print("email valid:",validate_input(email, "Email"))
print("Bangladesh mobile valid:", validate_input(bd_mobile, "bangladesh_mobile"))
print("USA telephone valid:", validate_input(telephone_USA,"USA_telephone"))
print("Password valid:", validate_input(password, "password"))

