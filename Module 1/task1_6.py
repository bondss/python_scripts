import sys

example_string = str(sys.argv[1])

example_string = example_string.replace(" ", "")
if example_string.lower() == example_string.lower()[::-1]:
    print ("YES")
else:
    print ("NO")