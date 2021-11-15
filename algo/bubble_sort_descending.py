#Implement the bubble sort algorithm that is sorting in descending order.
#O(n^2)
def bubble_sort_descending(input_list):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if(input_list[i]<input_list[j]):
                input_list[i],input_list[j] = input_list[j],input_list[i]

    print("after using bubble sort in descending order:")
    print(input_list)

input1=[3,1,8,6,7]
bubble_sort_descending(input1)
input2=[9,2,1,5,9,2,1]
bubble_sort_descending(input2)