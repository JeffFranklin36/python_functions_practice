def hello():
 print('hello user')

hello()

def pack(a, b, c):
 return [a, b, c]

print(pack('sandwich', 'apple juice', 'cheezits'))

def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch_list)):
      if i == 0:
        print(f"First I eat {lunch_list[0]}")
      else:
        print(f"Next I eat {lunch_list[i]}")

eat_lunch([])
eat_lunch(['sandwich'])
eat_lunch(['sandwich', 'apple juice', 'cheezits'])
