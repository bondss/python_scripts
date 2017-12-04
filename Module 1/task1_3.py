import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

const = "Everybody sing a song: "
if x > 1:
    couplet = y*((x*("la"  + "-" ))[:-1]+ " ")
else:
    couplet = y*((x*"la" + " "))

if y==0:
    if z == 1:
        print(const [:-1]  + couplet [:-1] + "!")
    elif z == 0:
        print(const [:-1] + couplet [:-1] + ".")
else:
    if z == 1:
        print(const + couplet [:-1] + "!")
    elif z == 0:
        print(const + couplet [:-1] + ".")
