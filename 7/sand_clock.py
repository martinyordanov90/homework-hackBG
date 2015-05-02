i = 11
stars = "*"
dots = "."
number_dots = 1
number_stars = i

should_reverse = False

for y in range(0, i):
    print((number_dots *  dots)
        + (stars * number_stars)
        + (number_dots * dots))
    if should_reverse:
        number_stars += 2
        number_dots -= 1
    else:
        number_dots += 1
        number_stars -= 2

    if number_stars == 1:
        should_reverse = True

def base(width, stars):
    point_count = (width - stars) // 2
    stars_string = "*" * stars
    one_side_points = "." * point_count

    return one_side_points + stars_string + one_side_points

def clock(n):
    width = n
    while n > 0:
        pritn(base(width, n))
        n -= 2
    n = 3

    while n <= width:
        print(base(width, n))
        n += 2