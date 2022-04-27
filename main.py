# TGA MAIN FUNC

def checker(mystr:str):
    open_brackets = "[{("
    close_brackets = "]})"
    
    heap = list()

    for i in mystr:
        if i in open_brackets:
            heap.append(i)

    print(heap)

checker("{}")

