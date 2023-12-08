def find(search_list:list, value):

    cloned_list = search_list.copy()

    while cloned_list:
        if len(cloned_list) >= 2:
            mid = len(cloned_list) // 2

            if cloned_list[mid] == value:
                return search_list.index(value)

            if value > cloned_list[mid]:
                cloned_list = cloned_list[mid+1:]
            else:
                cloned_list = cloned_list[:mid]

        if len(cloned_list) == 1:
            if cloned_list[0] != value:
                raise ValueError("value not in array")
            return search_list.index(cloned_list[0])

    raise ValueError("value not in array")
