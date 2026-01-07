l = [1,[2],[3,4,5],[6,[7,8,9]],10]
flatten_list = []
def make_flatten_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            flat_list(item)
        else:
            flatten_list.append(item)
            
make_flatten_list(l)
print(flatten_list)