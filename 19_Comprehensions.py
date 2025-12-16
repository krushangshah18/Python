"""
result = [expression for item in iterable if condition]
"""
li = [1, 2, 3, 4, 5]

sq = [x*x for x in li] 
print(sq)

even_cub = [x*x*x for x in li if x%2==0]
print(even_cub)


forDict = ["alice", "bob", "charlie"]
lens = {name:len(name) for name in forDict if len(name)>3}
print(lens)