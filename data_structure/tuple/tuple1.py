# unpack

food = ("apple", "cake", "juice")

(x,y,z) = food

print(x)


# now when we do like this


vegetables = ("carrot", "potato", "spinach")

(a,b,*c) = vegetables

print(a)
print(c)   # returns in separate list
print(*c)  # returns normal data