
def colapse_list(list_):
    colapsed_list = []
    for item in list_:
        if type(item) == list:
            colapse_list(item)
        colapsed_list.append(item)
    return colapsed_list
        


mylist = [123123, 23131, 12313, 21231, [[34, 234232], 543], [1231, 123123]]

print(colapsed_list)