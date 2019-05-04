def count_a(seq):
    """Counting the number of As in the string"""

    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    return result


def count_t(seq):
    """Counting the number of Ts in the string"""

    result = 0
    for b in seq:
        if b == 'T':
            result += 1

    return result


def count_c(seq):
    """Counting the number of Cs in the string"""

    result = 0
    for b in seq:
        if b == 'C':
            result += 1

    return result


def count_g(seq):
    """Counting the number of Gs in the string"""

    result = 0
    for b in seq:
        if b == 'G':
            result += 1

    return result


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
