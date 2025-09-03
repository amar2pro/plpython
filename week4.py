with open("week4.txt","r") as f:
    modify = f.read()
    print(modify)


with open("modified_week4.txt","w") as m:
    m.write(modify.lower())

with open("modified_week4.txt","r") as m:
    result = m.read()
    print(result)

filename = input("What is the filename:")

try:
    with open(filename,"r") as d:
        open_file = d.read()
        print(open_file)
except: 
    print("This file does not exist here. Ebu jaribu na ingine")