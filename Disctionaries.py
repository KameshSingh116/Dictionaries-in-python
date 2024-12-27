marks={
   "harry":100,
   "potter":200,
   0:"peshawar"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry":1000})
print(marks.values())

#The outputs for both 'get' function and the use of square brackets is same
#But for 'get' the value returned on the absence of the key given is "None"
#And for square brackets case it will be error on giving the key which is not present in the dictionary.
print(marks.get("harry"))
print(marks["harry"])

#pop
my_dict={'key1':'value1','key2':'value2'}
value=my_dict.pop('key1')
print(value)

#popitem()
#remves and returns the last key:value pair inserted into the dictionary.
last_item=my_dict.popitem()
print(last_item)

print(my_dict)

my_dict.update({'key3':'value3','key4':'value4'})
print(my_dict)

del my_dict['key3']
print(my_dict)

my_dict.update({'key5':'value5','key6':'value6'})

print(my_dict)

if 'key5' in my_dict:
    print("Hai bhai Hai!")

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

new_dict=my_dict.copy()

print(new_dict)

my_dict.clear()

print(my_dict)

#default
value=my_dict.setdefault('key7','default_value')
print(value)

ewy=my_dict.setdefault('key5','default_value')
print(ewy)

print(my_dict)
print(new_dict)

qwe=new_dict.setdefault('key5','default_value')
print(qwe)


#length
print(len(new_dict))

#dictionary comprehensions
#we can make dictionaries with a key and values based on the conditions we have given.
#we can provide a range foor the formation of the dictionary keys and values

squares={x:x**2 for x in range(6)}
print(squares)