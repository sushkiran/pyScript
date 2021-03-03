me = {2, 3, 4, 5, 6}

out = all(x in (4,5) for x in me)
print(out)

you = (4,5,5,4)
out = all(x in (4,5) for x in you)
print(out)