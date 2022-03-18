# 1. Countdown countdown(num) returns a list from that num to 0.
a = []

def countdown(num):
    for x in range(num, -1, -1):
        a.append(x),
    print(a)
countdown(5)
# 2. Print and Return, 2nd value is returned but not shown by terminal in VScode. When I try running this code in directly through CMD/Python it runs as expected.
def print_and_return(a,b):
    print(a)
    return b
print_and_return(1,2)
# 3. First Plus Length: Create a function that will receive a list and returns the sum of the first value in the list plus the list's length.
def first_p_length(fp_list):
    x = fp_list[0]
    y = len(fp_list)
    print(x+y)
    return
fp_list = [1,2,3,4,5]
first_p_length(fp_list)
# 4. Values Greater than Second
vgs_list = [5,2,3,2,1,4]
vgs_list2 = []


def morethanvalue2(x):
    if x > vgs_list[1]:
        return True        
    elif len(vgs_list) <= 2:
        return False

Greaterthan = filter(morethanvalue2, vgs_list)

for x in Greaterthan:
    vgs_list2.append(x)
print(len(vgs_list2))
print(vgs_list2)

# 5. This length, that value
lv_list = []
def length_and_value(a,b):
    count = 0
    while count < a:
        lv_list.append(b)
        count += 1
    print(lv_list)
length_and_value(4,7)
