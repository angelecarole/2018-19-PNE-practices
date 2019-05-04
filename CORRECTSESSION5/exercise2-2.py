from bases import count_a
from bases import count_c
from bases import count_g
from bases import count_t
s = "ACTG"
sb = "AACCTTGG"

print("Please enter the sequence 1", ":", s)

print("Please enter the sequence 2", ":", sb)


# Calculate the total length
t1 = len(s)
t2 = len(sb)

print("This sequence is {} bases in length".format(t1))
print("This sequence is {} bases in length".format(t2))

print("BASE A")
na = count_a(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t1, 1)))

print("BASE T")
na = count_t(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t1, 1)))

print("BASE C")
na = count_c(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t1, 1)))

print("BASE G")
na = count_g(s)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t1, 1)))

print("BASE A")
na = count_a(sb)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t2, 2)))

print("BASE T")
na = count_a(sb)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t2, 2)))

print("BASE C")
na = count_c(sb)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t2, 2)))

print("BASE G")
na = count_a(sb)
print(" Counter: {} ".format(na))
print(" Percentage: {}".format(round(100.0 * na/t2, 2)))
