
nested_list  = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


for i,sublist in enumerate(nested_list):
    for j, item in enumerate(sublist):
        print(f"[{i}][{j}]  - {item}", end=" ")
    print(" ")    