import cmath, math

def quadratic(a, b, c):
    try:
	    a, b, c = int(a), int(b), int(c)
	    if a == 0:
	        raise Exception
    except ValueError:
	    return "Illegal input."
    except Exception:
	    return "a could not be zero."
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
    else:
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)
    return 'x1 = {}\nx2 = {}'.format(x1, x2)


