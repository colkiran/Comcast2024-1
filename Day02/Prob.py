import re
def find_first_number_index(lst):
    for i, item in enumerate(lst):
        if re.match(r'\d', str(item)):
            return i
    return -1


input_list = ["divya", "lakshmi", 1, 3, 5]
index = find_first_number_index(input_list)

print(index)

# --------------------------------------------

res = ['apple', 'blue', 'cream', 'dog', 'green', 'orange', 'pink', 'violet', 'white', 'xray', 'yellow', 'zebra', 1, 10,
       1029, 184, 2, 2431, 276, 29, 3, 4, 5, 6, 7, 8, 9]
j = 0

def fun(lst):
    for i in res:
        try:
            if not i.isnumeric():
               return res.index(i) + 1
        except:
            print(f"is a number{i}")

print(fun(res))


#-----------------------------------------

count=0

for index, element in enumerate(res):

    # Check if the element is not a string

    if not isinstance(element, str):

        break

    else:

        count=count+1

print(count)
