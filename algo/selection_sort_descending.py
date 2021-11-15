#Implement the selection sort algorithm that is sorting in descending order.
#O(n^2)
def selection_sort_descending(input_list):
    for i in range(len(input_list)):
        max_index = i
        for j in range(i+1, len(input_list)):
            if (input_list[max_index]< input_list[j]):
                max_index = j
        input_list[i],input_list[max_index]=input_list[max_index],input_list[i]
    print("after using selection sort in descending order:")
    print(input_list)

input1=[3,1,8,6,7]
selection_sort_descending(input1)
input2=[9,2,1,5,9,2,1]
selection_sort_descending(input2)
