# print('Hello World')
print('hello india')
list1 = [ 'dinesh','vignesh',1]
list2= [ 'banana','orange','water']
print(list1.__add__(list2))
list1.append(2)

list1.insert(-2, 3)
print(list1)


for x in list1 :
    print (x)

text = "hello world"

if 'g' in text :
    print(True)
else:
    print(False)

car = {
    "color":"red",
    "model":"bmw",
    "year":2022
    }

mod=car["model"] 

print(mod)

mod1=print(car.get("model"))
print(car.keys())

for car2 in car.items():
    print(car2)


# git config --global user.name "Dinesh Kumar Thambiran"
# git config --global user.email "dineshkumarthambiran96@gmail.com"