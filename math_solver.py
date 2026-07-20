
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:

        root1 = (-b + (discriminant ** 0.5)) / (2 * a)
        root2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return f"two real roots: {root1} and {root2}"

    elif discriminant == 0:

        root = -b / (2 * a)
        return f"one real repeated root: {root}"

    else:
        # Complex roots calculation
        real_part = -b / (2 * a)
        imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
        return f"complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"


# test
print("quadratic solver :3")
print(solve_quadratic(1, -5, 6))