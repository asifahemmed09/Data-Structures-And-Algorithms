import utils.session
n = 4
count = 0

# head recursion
def print_hello():
    global count
    if count == n:
        return
    count += 1
    print("Hello")
    print_hello()

print_hello()

count2 = 0
# tail recursion
def print_hello_world():
    global count2
    if count2 == n:
        return
    count2 += 1
    print_hello_world()
    print("Hello World")

print_hello_world()
