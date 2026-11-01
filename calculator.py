
from decimal import Decimal, getcontext, InvalidOperation
import math
import cmath
import statistics

# Application configuration
getcontext().prec = 40

DEFAULT_PRECISION = 3
PI = Decimal("3.1415926535897932384626433832795028841971")

# Unit conversion factors, expressed in base units
# Each category is kept separate to prevent incompatible conversions
UNIT_FACTORS = {
    "length": {
        "mm": Decimal("0.001"),
        "cm": Decimal("0.01"),
        "m": Decimal("1"),
        "km": Decimal("1000"),
        "mi": Decimal("1609.34"),
        "yds": Decimal("0.9144"),
        "ft": Decimal("0.3048"),
    },
    "area": {
        "mm2": Decimal("0.000001"),
        "cm2": Decimal("0.0001"),
        "m2": Decimal("1"),
        "km2": Decimal("1000000"),
        "ha": Decimal("10000"),
        "ac": Decimal("4046.86"),
    },
    "volume": {
        "mm3": Decimal("0.000000001"),
        "cm3": Decimal("0.000001"),
        "m3": Decimal("1"),
        "l": Decimal("0.001"),
        "ml": Decimal("0.000001"),
        "fl_oz": Decimal("0.0000295735"),
        "gal": Decimal("0.00378541"),
    },
    "mass": {
        "mg": Decimal("0.000001"),
        "g": Decimal("0.001"),
        "kg": Decimal("1"),
        "t": Decimal("1000"),
        "lbs": Decimal("0.453592"),
        "st": Decimal("6.35029"),
        "oz": Decimal("0.0283495"),
    },
}

# User-defined constant, initially set to 1
constant_memory = Decimal("1")

########################
# P R O C E D U R E S  #
########################

def print_menu(options, x_label="Return to Previous Menu", labels=None):
    """Print a menu of options."""
    for key, option in options.items():
        if labels is not None:
            label = labels.get(key, option)
        elif callable(option):
            label = option.__doc__ or option.__name__
        else:
            label = option

        print(f"{key}: {label}")

    print(f"X: {x_label}")

def get_decimal_input(prompt):
    """Prompt for a numeric value, accepting the saved constant as MEMORY."""
    while True:
        user_input = input(prompt).strip()

        if user_input.upper() == "MEMORY":
            return constant_memory

        try:
            # Strip parentheses if the user enters a value in the form of (value)
            if user_input.startswith("(") and user_input.endswith(")"):
                user_input = user_input[1:-1].strip()
            value = Decimal(user_input)

            if not value.is_finite():
                print("Please enter a finite number.")
                continue

            return value

        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def convert_units(value, from_unit, to_unit):
    """Convert a value between compatible measurement units."""
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    # Find the category containing the source and target units
    source_category = None
    target_category = None

    for category, units in UNIT_FACTORS.items():
        if from_unit in units:
            source_category = category

        if to_unit in units:
            target_category = category

    # Validate that both units exist
    if source_category is None or target_category is None:
        raise ValueError("One or both units are invalid. Please check your input.")

    # Prevent conversions between incompatible dimensions
    if source_category != target_category:
        raise ValueError("Incompatible units. Please ensure both units are of the same category.")

    # Convert to the category's base unit, then to the target unit
    units = UNIT_FACTORS[source_category]

    value_in_base = value * units[from_unit]
    converted_value = value_in_base / units[to_unit]

    return converted_value.quantize(Decimal("0.001"))

def calculate_simple_operation(first_value, operator, second_value):
    """Perform a basic arithmetic operation and return its result."""

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "**": lambda x, y: x ** y,
    }

    if operator not in operations:
        raise ValueError("Invalid operator.")

    if operator == "/" and second_value == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return operations[operator](first_value, second_value)

def simple_arithmetic_menu():
    """Handle user interaction for simple arithmetic."""

    while True:
        try:
            first_value = get_decimal_input("Enter first value: ")
            second_value = get_decimal_input("Enter second value: ")
            operator = input("Enter operation (+, -, *, /, **): ").strip()

            result = calculate_simple_operation(
                first_value, operator, second_value
            )

            print(f"Result: {round(result, DEFAULT_PRECISION)}")
            cont = input("Do you want to perform another operation? (y/n): ").strip().lower()
            if cont == "n":
                break
            elif cont != "y":
                print("Invalid input. Returning to main menu.")
                break

        except ValueError as error:
            print(error)

        except ZeroDivisionError as error:
            print(error)

        except InvalidOperation:
            print("Invalid mathematical operation. Please try again.")


# ADVANCED ARITHMETIC

def compute_surd(radicand, index):
    """Calculate the nth root of a number."""
    if index <= 0 or index != index.to_integral_value():
        raise ValueError("Root index must be a positive integer.")

    if radicand < 0:
        if int(index) % 2 == 0:
            raise ValueError("An even root of a negative number is not real.")

        return -((-radicand) ** (Decimal(1) / index))

    return radicand ** (Decimal(1) / index)


def calculate_surd():
    """Prompt for values and display the nth root."""
    while True:
        try:
            radicand = get_decimal_input(
                "Enter radicand (value inside the surd): "
            )
            index = get_decimal_input("Enter root index: ")
            result = compute_surd(radicand, index)
            print(f"Result: {result:.{DEFAULT_PRECISION}f}")
            break

        except (ValueError, InvalidOperation, OverflowError) as error:
            print(f"Invalid calculation: {error}")


def compute_logarithm(log_base, log_argument):
    """Calculate the logarithm of a number with a specified base."""
    if log_base <= 0 or log_base == 1:
        raise ValueError(
            "Logarithm base must be positive and cannot equal 1."
        )

    if log_argument <= 0:
        raise ValueError("Logarithm argument must be greater than zero.")

    return Decimal(str(math.log(float(log_argument), float(log_base))))


def calculate_logarithm():
    """Prompt for values and display a logarithm."""
    while True:
        try:
            log_base = get_decimal_input("Please enter base of log: ")
            log_argument = get_decimal_input("Please enter argument of log: ")
            result = compute_logarithm(log_base, log_argument)
            print(f"Result: {result:.{DEFAULT_PRECISION}f}")
            break

        except (ValueError, InvalidOperation, OverflowError) as error:
            print(f"Invalid calculation: {error}")

def solve_quadratic(a, b, c):
    """Calculate the roots and completed-square form of a quadratic equation."""

    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")

    discriminant = b ** 2 - 4 * a * c

    # Calculate roots using Decimal when the roots are real.
    if discriminant >= 0:
        sqrt_discriminant = discriminant.sqrt()

        root_1 = (-b + sqrt_discriminant) / (2 * a)
        root_2 = (-b - sqrt_discriminant) / (2 * a)

    # Use complex arithmetic when the roots are imaginary.
    else:
        sqrt_discriminant = cmath.sqrt(complex(discriminant))

        a_complex = complex(a)
        b_complex = complex(b)

        root_1 = (-b_complex + sqrt_discriminant) / (2 * a_complex)
        root_2 = (-b_complex - sqrt_discriminant) / (2 * a_complex)

    # Completed-square form:
    # (x + b/2a)^2 + (b² - 4ac)/4a² = 0
    completed_square_offset = b / (2 * a)
    completed_square_term = discriminant / (4 * a ** 2)

    return root_1, root_2, completed_square_offset, completed_square_term

def calculate_quadratic():
    """Handle user interaction for solving quadratic equations."""

    while True:
        try:
            print("Quadratic Equation: ax² + bx + c = 0")

            a = get_decimal_input("Enter coefficient a: ")
            b = get_decimal_input("Enter coefficient b: ")
            c = get_decimal_input("Enter coefficient c: ")

            (
                root_1,
                root_2,
                completed_square_offset,
                completed_square_term,
            ) = solve_quadratic(a, b, c)

            print(f"Root 1: {root_1}")
            print(f"Root 2: {root_2}")

            print(
                "Completed-square form: "
                f"(x + {completed_square_offset})² "
                f"+ {completed_square_term} = 0"
            )

            break

        except (ValueError, InvalidOperation, OverflowError) as error:
            print(f"Invalid calculation: {error}")

def compute_factorial(number):
    """Calculate the factorial of a non-negative integer."""
    if number < 0 or number != number.to_integral_value():
        raise ValueError("Factorial requires a non-negative integer.")

    return math.factorial(int(number))


def calculate_factorial():
    """Prompt for a non-negative integer and display its factorial."""
    while True:
        try:
            number = get_decimal_input("Enter a non-negative integer: ")
            result = compute_factorial(number)
            print(f"Result: {result}")
            break

        except (ValueError, OverflowError) as error:
            print(f"Invalid calculation: {error}")

def compute_permutation(n, r):
    """Calculate the number of permutations of r objects from n objects."""
    if (
        n < 0
        or r < 0
        or n != n.to_integral_value()
        or r != r.to_integral_value()
    ):
        raise ValueError("Both values must be non-negative integers.")

    if r > n:
        raise ValueError(
            "The number selected cannot exceed the total number."
        )

    return math.perm(int(n), int(r))


def calculate_permutation():
    """Prompt for object counts and display the permutation count."""
    while True:
        try:
            n = get_decimal_input("Enter total number of objects (n): ")
            r = get_decimal_input("Enter number of objects selected (r): ")
            result = compute_permutation(n, r)
            print(f"Result: {result}")
            break

        except (ValueError, OverflowError) as error:
            print(f"Invalid calculation: {error}")

# POLYGON AND SOLID CALCULATOR
# 2D AREA

def compute_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    return length * width


def calculate_rectangle_area():
    """Calculate the area of a rectangle or parallelogram."""
    length = get_decimal_input("Enter length: ")
    width = get_decimal_input("Enter width: ")
    return compute_rectangle_area(length, width)


def compute_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base length and height must be greater than zero.")
    return Decimal("0.5") * base * height


def calculate_triangle_area():
    """Calculate the area of a triangle."""
    base = get_decimal_input("Enter base length: ")
    height = get_decimal_input("Enter perpendicular base height: ")
    return compute_triangle_area(base, height)


def compute_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    return PI * radius ** 2


def calculate_circle_area():
    """Calculate the area of a circle."""
    radius = get_decimal_input("Enter radius: ")
    return compute_circle_area(radius)


def compute_trapezium_area(parallel_side_1, parallel_side_2, height):
    if parallel_side_1 <= 0 or parallel_side_2 <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    return Decimal("0.5") * (parallel_side_1 + parallel_side_2) * height


def calculate_trapezium_area():
    """Calculate the area of a trapezium."""
    parallel_side_1 = get_decimal_input("Enter first parallel side: ")
    parallel_side_2 = get_decimal_input("Enter second parallel side: ")
    height = get_decimal_input("Enter perpendicular height: ")
    return compute_trapezium_area(parallel_side_1, parallel_side_2, height)


# VOLUME

def compute_cuboid_volume(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    return length * width * height


def calculate_cuboid_volume():
    """Calculate the volume of a cuboid."""
    length = get_decimal_input("Enter length: ")
    width = get_decimal_input("Enter width: ")
    height = get_decimal_input("Enter height: ")
    return compute_cuboid_volume(length, width, height)


def compute_cylinder_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")
    return PI * radius ** 2 * height


def calculate_cylinder_volume():
    """Calculate the volume of a cylinder."""
    radius = get_decimal_input("Enter radius: ")
    height = get_decimal_input("Enter height: ")
    return compute_cylinder_volume(radius, height)


def compute_triangular_prism_volume(a, b, c, prism_length):
    if min(a, b, c, prism_length) <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    # Compute the area of the triangular base using Heron's formula
    s = (a + b + c) / 2
    triangle_area = (s * (s - a) * (s - b) * (s - c)).sqrt()
    return triangle_area * prism_length


def calculate_triangular_prism_volume():
    """Calculate the volume of a triangular prism."""
    a = get_decimal_input("Enter length of side a: ")
    b = get_decimal_input("Enter length of side b: ")
    c = get_decimal_input("Enter length of side c: ")
    prism_length = get_decimal_input("Enter length of prism: ")
    return compute_triangular_prism_volume(a, b, c, prism_length)


def compute_sphere_volume(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    return (Decimal(4) / Decimal(3)) * PI * radius ** 3


def calculate_sphere_volume():
    """Calculate the volume of a sphere."""
    radius = get_decimal_input("Enter radius: ")
    return compute_sphere_volume(radius)


def compute_rectangular_pyramid_volume(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    return (length * width * height) / Decimal(3)


def calculate_rectangular_pyramid_volume():
    """Calculate the volume of a rectangular pyramid."""
    length = get_decimal_input("Enter base length: ")
    width = get_decimal_input("Enter base width: ")
    height = get_decimal_input("Enter perpendicular height: ")
    return compute_rectangular_pyramid_volume(length, width, height)


def compute_tetrahedron_volume(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero.")
    return side_length ** 3 / (Decimal(6) * Decimal(2).sqrt())


def calculate_tetrahedron_volume():
    """Calculate the volume of a regular tetrahedron."""
    side_length = get_decimal_input("Enter side length: ")
    return compute_tetrahedron_volume(side_length)


def compute_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")
    return (PI * radius ** 2 * height) / Decimal(3)


def calculate_cone_volume():
    """Calculate the volume of a cone."""
    radius = get_decimal_input("Enter radius: ")
    height = get_decimal_input("Enter perpendicular height: ")
    return compute_cone_volume(radius, height)

# SURFACE AREA

def compute_cuboid_sa(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")
    return Decimal(2) * (length * width + length * height + width * height)


def calculate_cuboid_sa():
    """Calculate the surface area of a cuboid."""
    length = get_decimal_input("Enter cuboid length: ")
    width = get_decimal_input("Enter cuboid width: ")
    height = get_decimal_input("Enter cuboid height: ")
    return compute_cuboid_sa(length, width, height)


def compute_cylinder_sa(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")
    return Decimal(2) * PI * radius * (radius + height)


def calculate_cylinder_sa():
    """Calculate the surface area of a cylinder."""
    radius = get_decimal_input("Enter base radius: ")
    height = get_decimal_input("Enter cylinder height: ")
    return compute_cylinder_sa(radius, height)


def compute_triangular_prism_sa(
    a, b, c, prism_length
):
    if min(a, b, c, prism_length) <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    if (
        a + b <= c
        or a + c <= b
        or b + c <= a
    ):
        raise ValueError("The three base edges must satisfy the triangle inequality.")

    # Compute the area of the triangular base using Heron's formula
    s = (a + b + c) / 2
    triangular_base_area = (s * (s - a) * (s - b) * (s - c)).sqrt()
    return (
        Decimal(2) * triangular_base_area
        + (a + b + c) * prism_length
    )


def calculate_triangular_prism_sa():
    """Calculate the surface area of a triangular prism."""
    a = get_decimal_input("Enter length of side a: ")
    b = get_decimal_input("Enter length of side b: ")
    c = get_decimal_input("Enter length of side c: ")
    prism_length = get_decimal_input("Enter length of prism: ")
    return compute_triangular_prism_sa(
        a, b, c, prism_length
    )


def compute_sphere_sa(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    return Decimal(4) * PI * radius ** 2


def calculate_sphere_sa():
    """Calculate the surface area of a sphere."""
    radius = get_decimal_input("Enter sphere radius: ")
    return compute_sphere_sa(radius)


def compute_rectangular_pyramid_sa(base_length, base_width, height):
    if base_length <= 0 or base_width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    # A right rectangular pyramid has its apex directly above the centre
    # of the rectangular base, giving two pairs of equal triangular faces
    slant_height_for_length_faces = (
        (base_width / Decimal(2)) ** 2 + height ** 2
    ).sqrt()
    slant_height_for_width_faces = (
        (base_length / Decimal(2)) ** 2 + height ** 2
    ).sqrt()

    return (
        base_length * base_width
        + base_length * slant_height_for_length_faces
        + base_width * slant_height_for_width_faces
    )


def calculate_rectangular_pyramid_sa():
    """Calculate the surface area of a right rectangular pyramid."""
    base_length = get_decimal_input("Enter base length: ")
    base_width = get_decimal_input("Enter base width: ")
    height = get_decimal_input("Enter perpendicular pyramid height: ")
    return compute_rectangular_pyramid_sa(base_length, base_width, height)


def compute_tetrahedron_sa(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero.")
    return Decimal(3).sqrt() * side_length ** 2


def calculate_tetrahedron_sa():
    """Calculate the surface area of a regular tetrahedron."""
    side_length = get_decimal_input("Enter tetrahedron side length: ")
    return compute_tetrahedron_sa(side_length)


def compute_cone_sa(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")

    slant_height = (height ** 2 + radius ** 2).sqrt()
    return PI * radius * (radius + slant_height)


def calculate_cone_sa():
    """Calculate the surface area of a cone."""
    radius = get_decimal_input("Enter cone base radius: ")
    height = get_decimal_input("Enter perpendicular height of cone: ")
    return compute_cone_sa(radius, height)


# STATISTICS

def get_number_list():
    """Prompt for a list of finite numbers separated by commas or spaces."""
    while True:
        user_input = input(
            "Please enter numbers separated by commas or spaces: "
        ).strip()

        try:
            num_list = [
                Decimal(value)
                for value in user_input.replace(",", " ").split()
            ]

            if not num_list:
                print("Please enter at least one number.")
                continue

            if not all(value.is_finite() for value in num_list):
                print("Please enter only finite numbers.")
                continue

            return num_list

        except InvalidOperation:
            print(
                "Invalid input. Please enter numbers separated by commas or spaces."
            )

def compute_mean(num_list):
    """Return the mean of a list of numbers."""
    if len(num_list) == 0:
        raise ValueError("Cannot compute mean of an empty list.")
    return sum(num_list) / len(num_list)


def mean():
    """Prompt for numbers and display their mean."""
    result = compute_mean(get_number_list())
    print(f"Mean: {result:.3f}")


def compute_median(num_list):
    """Return the median of a list of numbers."""
    if len(num_list) == 0:
        raise ValueError("Cannot compute median of an empty list.")
    return statistics.median(num_list)


def median():
    """Prompt for numbers and display their median."""
    result = compute_median(get_number_list())
    print(f"Median: {result:.3f}")


def compute_mode(num_list):
    """Return the mode of a list of numbers."""
    if len(num_list) == 0:
        raise ValueError("Cannot compute mode of an empty list.")
    return statistics.mode(num_list)


def mode():
    """Prompt for numbers and display their mode."""
    result = compute_mode(get_number_list())
    print(f"Mode: {result:.3f}")



def compute_iqr(num_list):
    """Return the interquartile range of a list of numbers."""
    num_list = sorted(num_list)
    if len(num_list) < 2:
        raise ValueError("At least 2 numbers are required to calculate IQR.")
    q1 = statistics.median(num_list[:len(num_list) // 2])
    q3 = statistics.median(num_list[len(num_list) // 2 + (len(num_list) % 2):])
    return q3 - q1


def iqr():
    """Prompt for numbers and display their interquartile range."""
    try:
        result = compute_iqr(get_number_list())
        print(f"IQR: {result:.3f}")
    except ValueError as error:
        print(error)


def compute_range(num_list):
    """Return the range of a list of numbers."""
    if len(num_list) == 0:
        raise ValueError("Cannot compute range of an empty list.")
    return max(num_list) - min(num_list)


def statistics_range():
    """Prompt for numbers and display their range."""
    try:
        result = compute_range(get_number_list())
        print(f"Range: {result:.3f}")
    except ValueError as error:
        print(error)

def main_menu():
    # Displays menu and handles user selection
    menu_choice = {
        "1": simple_arithmetic_menu,
        "2": advanced_arithmetic_menu,
        "3": unit_conversion_menu,
        "4": shape_calculator_menu,
        "5": constants_menu,
        "6": statistics_menu,
    }
    menu_labels = {
        "1": "Simple Arithmetic",
        "2": "Advanced Arithmetic",
        "3": "Unit Conversion",
        "4": "Polygon and Solid Calculator",
        "5": "Common Constants",
        "6": "Statistics",
    }

    while True:
        print("\n==== C A L C U L A T O R ====")
        print("Please select an option:")
        print_menu(menu_choice, x_label="Exit", labels=menu_labels)

        choice = input("Enter an option: ").upper()

        if choice in menu_choice:
            menu_choice[choice]()
        elif choice == "X":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

# Sub-menus

def advanced_arithmetic_menu():
    """Handle advanced arithmetic operations like surds, logarithms, quadratics, factorials, and permutations."""
    while True:
        operations = {
            "A": calculate_surd,
            "B": calculate_logarithm,
            "C": calculate_quadratic,
            "D": calculate_factorial,
            "E": calculate_permutation
            }

        aa_menu_labels = {
            "A": "Surds (nth roots)",
            "B": "Logarithms",
            "C": "Quadratics",
            "D": "Factorials",
            "E": "Permutations",
        }
        
        print("\n--- ADVANCED ARITHMETIC ---")
        print_menu(operations, x_label="Return to Main Menu", labels=aa_menu_labels)

        adv_arithmetic_choice = input("Enter an option: ").upper()

        if adv_arithmetic_choice in operations:
            operations[adv_arithmetic_choice]()
        elif adv_arithmetic_choice == "X":
            return
        else:
            print("Invalid option.")


def unit_conversion_menu():
    """Handle unit conversion."""
    categories = {
        category: category.title()
        for category in UNIT_FACTORS
    }

    while True:
        try:
            print("\n--- UNIT CONVERSION ---")
            print("Available categories:")
            for key, label in categories.items():
                print(f"{label} ")
            print("X: Return to Main Menu")

            category = input("Enter category: ").lower().strip()

            if category == "x":
                return

            if category not in UNIT_FACTORS:
                print("Invalid category.")
                continue

            print(f"\nAvailable units: {', '.join(UNIT_FACTORS[category])}")

            from_unit = input("Enter the current unit: ").lower().strip()
            to_unit = input("Enter the target unit: ").lower().strip()

            value = get_decimal_input("Enter the value to convert: ")

            converted_value = convert_units(value, from_unit, to_unit)

            if converted_value is not None:
                print(f"{value} {from_unit} = {converted_value} {to_unit}")
        except (ValueError, InvalidOperation) as error:
            print(f"Invalid conversion: {error}")

def shape_calculator_menu():
    """Handle geometry calculations and display their results."""
    while True:
        shape_menus = {
            "A": area_menu,
            "B": volume_menu,
            "C": surface_area_menu
        }
        print("\n--- SHAPE CALCULATOR ---")
        print_menu(
            shape_menus,
            x_label="Return to Main Menu",
            labels={
                "A": "Area",
                "B": "Volume",
                "C": "Surface Area",
            },
        )

        shape_choice = input("Select an option: ").strip().upper()

        if shape_choice in shape_menus:
            shape_menus[shape_choice]()
        elif shape_choice == "X":
            return
        else:
            print("Invalid selection.")

# Shape calculator sub-menus
def area_menu():
    """Calculate the area of a shape."""
    while True:
        areas = {
            "A": calculate_rectangle_area,
            "B": calculate_triangle_area,
            "C": calculate_circle_area,
            "D": calculate_trapezium_area,
        }

        print("\n--- AREA ---")
        print_menu(areas, x_label="Return to Shapes Menu")

        area_choice = input("Select a shape: ").strip().upper()

        if area_choice in areas:
            try:
                result = areas[area_choice]()
                print(f"Result: {result:.{DEFAULT_PRECISION}f}")
            except (ValueError, InvalidOperation, OverflowError) as error:
                print(f"Invalid calculation: {error}")
        elif area_choice == "X":
            break
        else:
            print("Invalid selection.")

def volume_menu():
    """Calculate the volume of a solid."""
    while True:
        volumes = {
            "A": calculate_cuboid_volume,
            "B": calculate_cylinder_volume,
            "C": calculate_triangular_prism_volume,
            "D": calculate_sphere_volume,
            "E": calculate_rectangular_pyramid_volume,
            "F": calculate_tetrahedron_volume,
            "G": calculate_cone_volume,
        }

        print("\n--- VOLUME ---")
        print_menu(volumes, x_label="Return to Shapes Menu")

        volume_choice = input("Select a shape: ").strip().upper()

        if volume_choice in volumes:
            try:
                result = volumes[volume_choice]()
                print(f"Result: {result:.{DEFAULT_PRECISION}f}")
            except (ValueError, InvalidOperation, OverflowError) as error:
                print(f"Invalid calculation: {error}")
        elif volume_choice == "X":
            break
        else:
            print("Invalid selection.")

def surface_area_menu():
    """Calculate the surface area of a solid."""
    while True:
        surfaces = {
            "A": calculate_cuboid_sa,
            "B": calculate_cylinder_sa,
            "C": calculate_triangular_prism_sa,
            "D": calculate_sphere_sa,
            "E": calculate_rectangular_pyramid_sa,
            "F": calculate_tetrahedron_sa,
            "G": calculate_cone_sa,
        }
        print("\n--- SURFACE AREA ---")
        print_menu(surfaces, x_label="Return to Shapes Menu")

        surface_choice = input("Enter shape: ").strip().upper()

        if surface_choice in surfaces:
            try:
                result = surfaces[surface_choice]()
                print(
                    f"Result: {result:.{DEFAULT_PRECISION}f} "
                )
            except (ValueError, InvalidOperation, OverflowError) as error:
                print(f"Invalid calculation: {error}")
        elif surface_choice == "X":
            break
        else:
            print("Invalid selection.")

def constants_menu():
    """Handles constant storage and retrieval."""
    constant_choices = {
        "A" : math_constants,
        "B" : scientific_constants,
        "C" : custom_constants
    }
    while True:
        print("\n--- COMMON CONSTANTS ---")
        print_menu(constant_choices, x_label="Return to Main Menu")

        choice = input("Enter an option: ").upper()
        if choice in constant_choices:
            constant_choices[choice]()
        elif choice == "X":
            return
        else:
            print("Invalid option.")

# Constants sub-menus
def math_constants():
    """Choose and save a mathematical constant."""
    math_constants = {
        "A": PI,
        "B": Decimal("2.7182818284590452353602874713527"),
        "C": Decimal("1.6180339887498948482045868343656"),  # Golden Ratio
        "D": PI * Decimal(2),
    }
    print_menu(
        math_constants,
        labels={
            "A": "π (pi)",
            "B": "e (Euler's Constant)",
            "C": "φ (Golden Ratio)",
            "D": "τ (Circle Constant)",
        },
    )
    choice = input("Choose a constant: ").upper()
    if choice in math_constants:
        global constant_memory
        constant_memory = math_constants[choice]
        print(f"Saved {constant_memory} to memory.")
    elif choice == "X":
        return
    else:
        print("Invalid option.")

def scientific_constants():
    """Choose and save a scientific constant."""
    scientific_constants = {
        "A": "6.02e23",  # Avogadro’s number
        "B": "2.99792458e8",  # Speed of light
        "C": "6.67430e-11",  # Gravitational constant
        "D": "6.62607015e-34"  # Planck's constant
    }
    print_menu(
        scientific_constants,
        labels={
            "A": "Avogadro's Constant",
            "B": "Speed of Light",
            "C": "Gravitational Constant",
            "D": "Planck's Constant",
        },
    )
    choice = input("Choose a constant: ").upper()
    if choice in scientific_constants:
        global constant_memory
        constant_memory = Decimal(scientific_constants[choice])
        print(f"Saved {scientific_constants[choice]} to memory.")
    elif choice == "X":
        return
    else:
        print("Invalid option.")

def custom_constants():
    """Set a custom constant."""
    try:
        global constant_memory
        constant_memory = get_decimal_input("Enter your custom constant: ")
        print("Saved to memory.")
    except InvalidOperation:
        print("Invalid input.")

def statistics_menu():
    """Handles statistical calculations."""
    while True:
        operations = {
            "A": mean,
            "B": median,
            "C": mode,
            "D": statistics_range,
            "E": iqr
                }
        print("\n--- STATISTICS ---")
        print_menu(operations, x_label="Return to Main Menu")
        choice = input("Enter an option: ").upper()
        
        if choice in operations:
            operations[choice]()
        elif choice == "X":
            return
        else:
            print("Invalid option.")

# Run the main menu when this file is executed directly.
if __name__ == "__main__":
    main_menu()