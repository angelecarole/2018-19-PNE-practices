from bases import count_a
from bases import count_c
from bases import count_g
from bases import count_t

s = "ACTGG"

print("Please enter the sequence", ":", s )

# Calculate the total length
tl = len(s)

print("This sequence is {} bases in length".format(tl))

print("BASE A")

na = count_a(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/tl, 1)))

print("BASE T")

na = count_t(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/tl, 1)))

print("BASE C")

na = count_c(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/tl, 1)))

print("BASE G")

na = count_g(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/tl, 1)))
