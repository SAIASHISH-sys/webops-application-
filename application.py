'''----------Making A Array Sorting Program------------
                                        -Made By: Sai Ashish Mishra'''
#taking the array from the user in form of basic string input
A=input('enter the array you want to sort out:');
#converting the string data in form of a nested list to use for further operation
a=eval(A);
result_list=[];
#creating an empty list to input data
def base_listsorter(a):
    #using for function to operate on each indivisual element
    for i in a:
        #typing a recursion conditional statement
        if type(i)==list:
            i=base_listsorter(i);
        else:
            #appending each item to the end of the result list after sorting it
            result_list.append(i)
#calling out the function
base_listsorter(a)
#printing the result list
print(result_list);
