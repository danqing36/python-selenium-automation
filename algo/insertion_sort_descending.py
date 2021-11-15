#Implement the insertion sort algorithm that is sorting in descending order.
#O(n^2)
def insertion_sort_descending(input_list):
    for i in range(1,len(input_list)):
        sort_value = input_list[i]
        j = i-1
        while(j>=0 and input_list[j]<sort_value):
            input_list[j+1]=input_list[j]
            j-=1
        input_list[j+1]=sort_value

    print("after using insertion sort in descending order:")
    print(input_list)


input1=[3,1,8,6,7]
insertion_sort_descending(input1)
input2=[9,2,1,5,9,2,1]
insertion_sort_descending(input2)