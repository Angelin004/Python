s_username="ak"
s_password="ak918"

username=input("enter username:")
password=input("enter password:")

def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False
    
a=validate()
print(a)
