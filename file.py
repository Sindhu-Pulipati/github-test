
def print_even(test_list):
    for i in test_list:
        if(i%2==0):
          yield i

test_list=[1,2,3,4,5,6]
print("original list:"+ str(test_list))
print("even_list:")
for j in print_even(test_list):
    print(j, end=" ")

