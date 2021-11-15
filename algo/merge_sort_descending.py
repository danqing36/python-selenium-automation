#Implement the merge sort algorithm that is sorting in descending order.
#O(nlogn)
def merge_sort_descending(input_list):
    if len(input_list)>1:
        mid=len(input_list)//2
        left = input_list[0:mid]
        right = input_list[mid:len(input_list)]
        merge_sort_descending(left)
        merge_sort_descending(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                input_list[k]=left[i]
                i+=1
            else:
                input_list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            input_list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            input_list[k]=right[j]
            j+=1
            k+=1
    print("after using merge sort in descending order:")
    print(input_list)


input1=[3,1,8,6,7]
merge_sort_descending(input1)
input2=[9,2,1,5,9,2,1]
merge_sort_descending(input2)