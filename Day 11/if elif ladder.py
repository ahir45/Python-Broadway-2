# if .. elif.. elif..else ladder

a = 5
b = 4
# in this example we have used if elif else ladder so if one of the condition is met then other conditions are not checked
if a == 5:
    print("First print 5")
elif a == 5:
    print("Second print 5")
else:
    print("No 5")

if a == 5:
    print("First print 5")
if a == 5:
    print("Second print 5")
else:
    print("No 5")

if a > b:
    print(a)
elif b == a:
    print(b)
elif b > a:
    print(a)
else:
    print(b)

# nested if

a = [1, 2, 3, 4]
if a:
    if type(a) == list:
        print(a)
    else:
        print("Its not")
else:
    print("a is empty")
