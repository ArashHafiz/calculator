
from decimal import Decimal, getcontext, InvalidOperation
import math
import cmath
import statistics

# Application configuration
getcontext().prec = 40

APP_NAME = "Arash's Calculator"
DEFAULT_PRECISION = 3
PI = Decimal("3.1415926535897932384626433832795028841971")

# Unit conversion factors, expressed in base units.
# Each category is kept separate to prevent incompatible conversions.
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

# User-defined constant, initially set to 1.
constant_memory = Decimal("1")

########################
# P R O C E D U R E S  #
########################

def get_decimal_input(prompt):
    """Prompt for a numeric value, accepting the saved constant as MEMORY."""
    while True:
        user_input = input(prompt).strip()

        if user_input.upper() == "MEMORY":
            return constant_memory

        try:
            # Strip parentheses if the user enters a value in the form of (value).
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

    # Find the category containing the source and target units.
    source_category = None
    target_category = None

    for category, units in UNIT_FACTORS.items():
        if from_unit in units:
            source_category = category

        if to_unit in units:
            target_category = category

    # Validate that both units exist.
    if source_category is None or target_category is None:
        print("Invalid unit entered.")
        return None

    # Prevent conversions between incompatible dimensions.
    if source_category != target_category:
        print("Incompatible units. Both units must belong to the same category.")
        return None

    # Convert to the category's base unit, then to the target unit.
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

def simple_arithmetic():
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
            break

        except ValueError as error:
            print(error)

        except ZeroDivisionError as error:
            print(error)

        except InvalidOperation:
            print("Invalid mathematical operation. Please try again.")


# ADVANCED ARITHMETIC


def calculate_surd():
    """Calculate the nth root of a number."""

    while True:
        try:
            radicand = get_decimal_input(
                "Enter radicand (value inside the surd): "
            )
            index = get_decimal_input("Enter root index: ")

            if index <= 0 or index != index.to_integral_value():
                raise ValueError("Root index must be a positive integer.")

            if radicand < 0:
                if int(index) % 2 == 0:
                    raise ValueError(
                        "An even root of a negative number is not real."
                    )

                result = -((-radicand) ** (Decimal(1) / index))
            else:
                result = radicand ** (Decimal(1) / index)

            print(f"Result: {result:.{DEFAULT_PRECISION}f}")
            break

        except (ValueError, InvalidOperation, OverflowError) as error:
            print(f"Invalid calculation: {error}")


def calculate_logarithm():
    """Calculate the logarithm of a number with a specified base."""

    while True:
        try:
            log_base = get_decimal_input("Please enter base of log: ")
            log_argument = get_decimal_input("Please enter argument of log: ")

            if log_base <= 0 or log_base == 1:
                raise ValueError(
                    "Logarithm base must be positive and cannot equal 1."
                )

            if log_argument <= 0:
                raise ValueError(
                    "Logarithm argument must be greater than zero."
                )

            result = (
                Decimal(str(math.log(float(log_argument), float(log_base))))
            )

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

def calculate_factorial():
    """Calculate the factorial of a non-negative integer."""

    while True:
        try:
            number = get_decimal_input("Enter a non-negative integer: ")

            if number < 0 or number != number.to_integral_value():
                raise ValueError(
                    "Factorial requires a non-negative integer."
                )

            result = math.factorial(int(number))

            print(f"Result: {result}")
            break

        except (ValueError, OverflowError) as error:
            print(f"Invalid calculation: {error}")

def calculate_permutation():
    """Calculate the number of permutations of r objects from n objects."""

    while True:
        try:
            n = get_decimal_input("Enter total number of objects (n): ")
            r = get_decimal_input("Enter number of objects selected (r): ")

            if (
                n < 0
                or r < 0
                or n != n.to_integral_value()
                or r != r.to_integral_value()
            ):
                raise ValueError(
                    "Both values must be non-negative integers."
                )

            if r > n:
                raise ValueError(
                    "The number selected cannot exceed the total number."
                )

            result = math.perm(int(n), int(r))

            print(f"Result: {result}")
            break

        except (ValueError, OverflowError) as error:
            print(f"Invalid calculation: {error}")

# POLYGON AND SOLID CALCULATOR
# 2D AREA

def calculate_rectangle_area():
    """Calculate the area of a rectangle or parallelogram."""
    length = get_decimal_input("Enter length: ")
    width = get_decimal_input("Enter width: ")

    if length <= 0 or width <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    return length * width


def calculate_triangle_area():
    """Calculate the area of a triangle."""
    base = get_decimal_input("Enter base length: ")
    height = get_decimal_input("Enter perpendicular base height: ")

    if base <= 0 or height <= 0:
        raise ValueError("Base length and height must be greater than zero.")

    return Decimal("0.5") * base * height


def calculate_circle_area():
    """Calculate the area of a circle."""
    radius = get_decimal_input("Enter radius: ")

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    return PI * radius ** 2


def calculate_trapezium_area():
    """Calculate the area of a trapezium."""
    parallel_side_1 = get_decimal_input("Enter first parallel side: ")
    parallel_side_2 = get_decimal_input("Enter second parallel side: ")
    height = get_decimal_input("Enter perpendicular height: ")

    if parallel_side_1 <= 0 or parallel_side_2 <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    return Decimal("0.5") * (parallel_side_1 + parallel_side_2) * height


# VOLUME

def calculate_cuboid_volume():
    """Calculate the volume of a cuboid."""
    length = get_decimal_input("Enter length: ")
    width = get_decimal_input("Enter width: ")
    height = get_decimal_input("Enter height: ")

    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    return length * width * height


def calculate_cylinder_volume():
    """Calculate the volume of a cylinder."""
    radius = get_decimal_input("Enter radius: ")
    height = get_decimal_input("Enter height: ")

    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")

    return PI * radius ** 2 * height


def calculate_triangular_prism_volume():
    """Calculate the volume of a triangular prism."""
    base = get_decimal_input("Enter base length of triangle: ")
    base_height = get_decimal_input("Enter perpendicular height of triangle: ")
    prism_length = get_decimal_input("Enter length of prism: ")

    if base <= 0 or base_height <= 0 or prism_length <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    triangle_area = Decimal("0.5") * base * base_height
    return triangle_area * prism_length


def calculate_sphere_volume():
    """Calculate the volume of a sphere."""
    radius = get_decimal_input("Enter radius: ")

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    return (Decimal(4) / Decimal(3)) * PI * radius ** 3


def calculate_rectangular_pyramid_volume():
    """Calculate the volume of a rectangular pyramid."""
    length = get_decimal_input("Enter base length: ")
    width = get_decimal_input("Enter base width: ")
    height = get_decimal_input("Enter perpendicular height: ")

    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    return (length * width * height) / Decimal(3)


def calculate_tetrahedron_volume():
    """Calculate the volume of a regular tetrahedron."""
    side_length = get_decimal_input("Enter side length: ")

    if side_length <= 0:
        raise ValueError("Side length must be greater than zero.")

    return side_length ** 3 / (Decimal(6) * Decimal(2).sqrt())


def calculate_cone_volume():
    """Calculate the volume of a cone."""
    radius = get_decimal_input("Enter radius: ")
    height = get_decimal_input("Enter perpendicular height: ")

    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")

    return (PI * radius ** 2 * height) / Decimal(3)


# SURFACE AREA
# These functions return (surface_area, unit). The menu is responsible for
# displaying the result, keeping output handling consistent with area/volume.

def cuboid_sa():
    """Calculate the surface area of a cuboid."""
    length = get_decimal_input("Enter cuboid length: ")
    width = get_decimal_input("Enter cuboid width: ")
    height = get_decimal_input("Enter cuboid height: ")
    unit = input("Enter length unit: ").strip()

    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    surface_area = Decimal(2) * (length * width + length * height + width * height)
    return surface_area, unit


def cylinder_sa():
    """Calculate the surface area of a cylinder."""
    radius = get_decimal_input("Enter base radius: ")
    height = get_decimal_input("Enter cylinder height: ")
    unit = input("Enter length unit: ").strip()

    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")

    surface_area = Decimal(2) * PI * radius * (radius + height)
    return surface_area, unit


def triangle_prism_sa():
    """Calculate the surface area of a triangular prism."""
    base = get_decimal_input("Enter base length of triangle: ")
    second_side = get_decimal_input("Enter second base edge length: ")
    third_side = get_decimal_input("Enter third base edge length: ")
    base_height = get_decimal_input("Enter perpendicular height of triangle: ")
    prism_length = get_decimal_input("Enter length of prism: ")
    unit = input("Enter length unit: ").strip()

    if min(base, second_side, third_side, base_height, prism_length) <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    if base + second_side <= third_side or base + third_side <= second_side or second_side + third_side <= base:
        raise ValueError("The three base edges must satisfy the triangle inequality.")

    triangular_base_area = Decimal("0.5") * base * base_height
    surface_area = (
        Decimal(2) * triangular_base_area
        + (base + second_side + third_side) * prism_length
    )
    return surface_area, unit


def sphere_sa():
    """Calculate the surface area of a sphere."""
    radius = get_decimal_input("Enter sphere radius: ")
    unit = input("Enter length unit: ").strip()

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    return Decimal(4) * PI * radius ** 2, unit


def rectangle_pyramid_sa():
    """Calculate the surface area of a right rectangular pyramid."""
    base_length = get_decimal_input("Enter base length: ")
    base_width = get_decimal_input("Enter base width: ")
    height = get_decimal_input("Enter perpendicular pyramid height: ")
    unit = input("Enter length unit: ").strip()

    if base_length <= 0 or base_width <= 0 or height <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    # A right rectangular pyramid has its apex directly above the centre
    # of the rectangular base, giving two pairs of equal triangular faces.
    slant_height_for_length_faces = (
        (base_width / Decimal(2)) ** 2 + height ** 2
    ).sqrt()
    slant_height_for_width_faces = (
        (base_length / Decimal(2)) ** 2 + height ** 2
    ).sqrt()

    surface_area = (
        base_length * base_width
        + base_length * slant_height_for_length_faces
        + base_width * slant_height_for_width_faces
    )
    return surface_area, unit


def tetrahedron_sa():
    """Calculate the surface area of a regular tetrahedron."""
    side_length = get_decimal_input("Enter tetrahedron side length: ")
    unit = input("Enter length unit: ").strip()

    if side_length <= 0:
        raise ValueError("Side length must be greater than zero.")

    surface_area = Decimal(3).sqrt() * side_length ** 2
    return surface_area, unit


def cone_sa():
    """Calculate the surface area of a cone."""
    radius = get_decimal_input("Enter cone base radius: ")
    height = get_decimal_input("Enter perpendicular height of cone: ")
    unit = input("Enter length unit: ").strip()

    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be greater than zero.")

    slant_height = (height ** 2 + radius ** 2).sqrt()
    surface_area = PI * radius * (radius + slant_height)
    return surface_area, unit


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
                "Invalid input. Please enter numbers separated by "
                "commas or spaces."
            )

def mean():
    # Calculates mean of a list of numbers
    num_list = get_number_list()
    result = sum(num_list) / len(num_list)
    print(f"Mean: {result:.3f}")

def median():
    # Calculates median of a list of numbers
    num_list = sorted(get_number_list())
    result = statistics.median(num_list)
    print(f"Median: {result:.3f}")

def mode():
    # Calculates mode of a list of numbers
    try:
        num_list = get_number_list()
        result = statistics.mode(num_list)
        print(f"Mode: {result:.3f}")
    except statistics.StatisticsError:
        print("No mode found (all numbers equal).")

def iqr():
    # Calculates interquartile range of list of numbers
    num_list = sorted(get_number_list())
    q1 = statistics.median(num_list[:len(num_list) // 2]) # Calculates lower quartile (median of lower half)
    q3 = statistics.median(num_list[len(num_list) // 2 + (len(num_list) % 2):])   # Calculates upper quartile (median of upper half)
    print(f"IQR: {q3 - q1:.3f}")


def statistics_range():
    # Calculates range of list of numbers
    num_list = sorted(get_number_list())
    result = num_list[len(num_list) - 1] - num_list[0]
    print(f"Range: {result:.3f}")
            
                
def main_menu():
    # Displays menu and handles user selection
    while True:
        print("\n==== C A L C U L A T O R ====")
        print("Welcome to Arash's calculator! Please pick an option:")
        print("1: Simple Arithmetic")
        print("2: Advanced Arithmetic")
        print("3: Unit Conversion")
        print("4: Polygon and Solid Calculator")
        print("5: Common Constants")
        print("6: Statistics")
        print("X: Exit")

        choice = input("Enter an option: ").upper()

        menu_choice = {
            "1" : simple_arithmetic,
            "2" : advanced_arithmetic_menu,
            "3" : unit_conversion_menu,
            "4" : shape_calculator_menu,
            "5" : constants_menu,
            "6" : statistics_menu,
        }

        if choice in menu_choice:
            menu_choice[choice]()
        elif choice == "X":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

# Sub-menus

def advanced_arithmetic_menu():
    # Advanced arithmetic menu
    print("\n--- ADVANCED ARITHMETIC ---")
    print("A: Surds (Rooting)")
    print("B: Logarithms")
    print("C: Quadratics")
    print("D: Factorials")
    print("E: Permutations")
    print("X: Return to Main Menu")

    choice = input("Enter an option: ").upper()
    operations = {
        "A": calculate_surd,
        "B": calculate_logarithm,
        "C": calculate_quadratic,
        "D": calculate_factorial,
        "E": calculate_permutation
    }

    if choice in operations:
        operations[choice]()
    elif choice == "X":
        return
    else:
        print("Invalid option.")


def unit_conversion_menu():
    """Handle unit conversion."""
    print("\n--- UNIT CONVERSION ---")
    print("Available categories: Length, Area, Volume, Mass")

    category = input("Enter category: ").lower().strip()

    if category not in UNIT_FACTORS:
        print("Invalid category.")
        return

    print(f"\nAvailable units: {', '.join(UNIT_FACTORS[category])}")

    from_unit = input("Enter the current unit: ").lower().strip()
    to_unit = input("Enter the target unit: ").lower().strip()

    value = get_decimal_input("Enter the value to convert: ")

    converted_value = convert_units(value, from_unit, to_unit)

    if converted_value is not None:
        print(f"{value} {from_unit} = {converted_value} {to_unit}")

def shape_calculator_menu():
    """Handle geometry calculations and display their results."""

    while True:
        print("\n--- SHAPE CALCULATOR ---")
        print("1. Area")
        print("2. Volume")
        print("3. Surface Area")
        print("4. Return to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            areas = {
                "1": calculate_rectangle_area,
                "2": calculate_triangle_area,
                "3": calculate_circle_area,
                "4": calculate_trapezium_area,
            }

            print("\n--- AREA ---")
            for key, function in areas.items():
                print(f"{key}. {function.__doc__}")

            shape_choice = input("Select a shape: ").strip()

            if shape_choice in areas:
                try:
                    result = areas[shape_choice]()
                    print(f"Result: {result:.{DEFAULT_PRECISION}f}")
                except (ValueError, InvalidOperation, OverflowError) as error:
                    print(f"Invalid calculation: {error}")
            else:
                print("Invalid selection.")

        elif choice == "2":
            volumes = {
                "1": calculate_cuboid_volume,
                "2": calculate_cylinder_volume,
                "3": calculate_triangular_prism_volume,
                "4": calculate_sphere_volume,
                "5": calculate_rectangular_pyramid_volume,
                "6": calculate_tetrahedron_volume,
                "7": calculate_cone_volume,
            }

            print("\n--- VOLUME ---")
            for key, function in volumes.items():
                print(f"{key}. {function.__doc__}")

            volume_choice = input("Select a shape: ").strip()

            if volume_choice in volumes:
                try:
                    result = volumes[volume_choice]()
                    print(f"Result: {result:.{DEFAULT_PRECISION}f}")
                except (ValueError, InvalidOperation, OverflowError) as error:
                    print(f"Invalid calculation: {error}")
            else:
                print("Invalid selection.")

        elif choice == "3":
            surfaces = {
                "A": cuboid_sa,
                "B": cylinder_sa,
                "C": triangle_prism_sa,
                "D": sphere_sa,
                "E": rectangle_pyramid_sa,
                "F": tetrahedron_sa,
                "G": cone_sa,
            }

            print("\n--- SURFACE AREA ---")
            for key, function in surfaces.items():
                print(f"{key}: {function.__doc__}")

            surface_choice = input("Enter shape: ").strip().upper()

            if surface_choice in surfaces:
                try:
                    result, unit = surfaces[surface_choice]()
                    print(
                        f"Result: {result:.{DEFAULT_PRECISION}f} "
                        f"{unit}²"
                    )
                except (ValueError, InvalidOperation, OverflowError) as error:
                    print(f"Invalid calculation: {error}")
            else:
                print("Invalid selection.")

        elif choice == "4":
            break

        else:
            print("Invalid selection.")

def constants_menu():
    # Handles constant storage and retrieval
    print("\n--- COMMON CONSTANTS ---")
    print("1: Mathematical Constants")
    print("2: Scientific Constants")
    print("3: Save Your Own Constant")
    print("X: Return to Main Menu")

    choice = input("Enter an option: ").upper()
    if choice == "1":
        math_constants = {
            "A": PI,
            "B": Decimal("2.7182818284590452353602874713527"),
            "C": Decimal("1.6180339887498948482045868343656"),  # Golden Ratio
            "D": PI * Decimal(2),
        }
        print("A: π (pi)")
        print("B: e (Euler's Constant)")
        print("C: φ (Golden Ratio)")
        print("D: τ (Circle Constant)")
        math_choice = input("Choose a constant: ").upper()
        if math_choice in math_constants:
            global constant_memory
            constant_memory = math_constants[math_choice]
            print(f"Saved {constant_memory} to memory.")

    elif choice == "2":
        scientific_constants = {
            "A": "6.02e23",  # Avogadro’s number
            "B": "2.99792458e8",  # Speed of light
            "C": "6.67430e-11",  # Gravitational constant
            "D": "6.62607015e-34"  # Planck's constant
        }
        print("A: Avogadro's Constant")
        print("B: Speed of Light")
        print("C: Gravitational Constant")
        print("D: Planck's Constant")
        science_choice = input("Choose a constant: ").upper()
        if science_choice in scientific_constants:
            constant_memory = Decimal(scientific_constants[science_choice])
            print(f"Saved {scientific_constants[science_choice]} to memory.")

    elif choice == "3":
        try:
            constant_memory = get_decimal_input("Enter your custom constant: ")
            print("Saved to memory.")
        except InvalidOperation:
            print("Invalid input.")

    elif choice == "X":
        return
    
    else:
        print("Invalid option.")

def statistics_menu():
    # Handles statistical calculations
    print("\n--- STATISTICS ---")
    print("A: Mean")
    print("B: Median")
    print("C: Mode")
    print("D: Range")
    print("E: IQR")
    print("X: Return to Main Menu")

    choice = input("Enter an option: ").upper()
    operations = {
        "A": mean,
        "B": median,
        "C": mode,
        "D": statistics_range,
        "E": iqr
    }
    if choice in operations:
        operations[choice]()
    elif choice == "X":
        return
    else:
        print("Invalid option.")

# Run the main menu when this file is executed directly.
if __name__ == "__main__":
    main_menu()