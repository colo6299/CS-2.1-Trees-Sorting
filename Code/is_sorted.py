
# if the current item in the list is smaller than the next item at any point,
# then the list is not in sorted order.
def is_sorted(list_in):
    for index, item in enumerate(list_in):
        if list_in[index + 1] is not None:
            if item > list_in[index + 1]:
                return False
    return True

# if 
def bubble_sort(list_in):
    i = 0
    finished = True
    while True:
        ndx = i % len(list_in)
        if ndx is not len(list_in) - 1:
            current_item = list_in[ndx]
            next_item = list_in[ndx+1]
            if current_item > next_item:
                list_in[ndx] = next_item
                list_in[ndx+1] = current_item
                finished = False
            
            if ndx == len(list_in) - 1:
                if finished:
                    return
                else: 
                    finished = True
        i += 1


if __name__ == "__main__":
    ls = [1,4,5,2,7]
    bubble_sort(ls)
    print(ls)

                