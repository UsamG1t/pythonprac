l1 = list(range(5, 16))
l2 = list("abcdefghijk")
l1[4:8] = l2[-5:]

print(l1, l2)

# l1, l2 = list(range(5, 16)), list("abcdefghijk")
# l1[4:8] = l2[-5:]
# print(l1, l2)
