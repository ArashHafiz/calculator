from decimal import Decimal, getcontext, InvalidOperation
import math
import cmath
import statistics

# Initialization
choice = ""
constant_memory = 1
getcontext().prec = 40

########################
# P R O C E D U R E S  #
########################

def get_decimal_input(prompt):
    # General function that allows user to enter input in Decimal
    # Also allows for the retrieval of saved constants by typing in 'memory'
    while True:
        try:
            value = input(prompt).upper()
            return constant_memory if value == "MEMORY" else Decimal(value)
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def convert_units(value, from_unit, to_unit):
        # General function that allows for conversion between selected units using base unit
        unit_factors = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "mi": 1609.34, "yds": 0.9144, "ft": 0.3048,
        "mm2": 1e-6, "cm2": 1e-4, "m2": 1, "km2": 1e6, "ha": 1e4, "ac": 4046.86,
        "mm3": 1e-9, "cm3": 1e-6, "m3": 1, "l": 1e-3, "ml": 1e-6, "fl_oz": 2.95735e-5, "gal": 3.78541e-3,
        "mg": 1e-6, "g": 1e-3, "kg": 1, "t": 1000, "lbs": 0.453592, "st": 6.35029, "oz": 0.0283495
    }
        try:
            if from_unit in unit_factors and to_unit in unit_factors:
                # Convert to base unit, then to target unit
                value_in_base = Decimal(value) * Decimal(unit_factors[from_unit])  # Convert to base unit
                converted_value = value_in_base / Decimal(unit_factors[to_unit])   # Convert to target unit
                return round(converted_value, 3)
            else:
                print("Invalid unit entered.")
                return None
        except InvalidOperation:
            print("Invalid number entered.")
            return None

def simple_arithmetic():
    # Procedure for simple arithmetic section
    while True:
        try:
            # Dictionary of operators and corresponding symbols
            simple_operators = {
                "+":lambda x, y : x + y,
                "-":lambda x, y : x - y,
                "/":lambda x, y : x / y,
                "*":lambda x, y : x * y,
                "**":lambda x,y : x ** y
                }        
            
            simple_calc_1 = get_decimal_input("Enter first value: ")

            simple_calc_2 = get_decimal_input("Enter second value: ")
            
            simple_calc_op = input("Enter operation: ")
            
            # Check if operator valid and performs calculation
            if simple_calc_op in simple_operators:
                simple_calc_ans = simple_operators[simple_calc_op](simple_calc_1, simple_calc_2)
                print(round(simple_calc_ans, 3))
                break
            else:
                print("Invalid operator, please try again.")

        except InvalidOperation:
            print("Invalid value entered, please enter a real number.")


# ADVANCED ARITHMETIC

def calculate_surd():
    # Procedure for surd calculation
    while True: 
        try:
            radicand = get_decimal_input("Enter radicand (value inside the surd): ")
        
            index = get_decimal_input("Enter index (nth root): ")
            
            print(round(radicand**(1/index),3))
            break
        except InvalidOperation:
            print("Invalid value. Ensure the radicand is a real number and the index is a positive integer greater than 1.")

def calculate_logarithm():
    # Procedure for logarithm calculation
    while True:
        try:
            log_base = get_decimal_input("Please enter base of log: ")
            
            log_argument = get_decimal_input("Please enter argument of log: ")
                                                                                  
            print(round(math.log(log_argument, log_base),3))
            break
        except InvalidOperation:
            print("Invalid value for logarithm. Please enter a positive real number.")

def calculate_quadratic():
    # Procedure for quadratic calculation
    while True:
        try:
            print("Quadratic Equation: ax^2 + bx + c = 0")
            a = get_decimal_input("Enter value for a: ")
            b = get_decimal_input("Enter value for b: ")
            c = get_decimal_input("Enter value for c: ")

            if a == 0:
                print("This is not a quadratic equation (a cannot be 0).")
                return
            
            # Convert a, b, c to complex to be able to work out complex and real situations
            a, b, c = complex(a), complex(b), complex(c)

            # Calculate the discriminant
            discriminant = (b**2) - (4*a*c)

            # Compute square root of discriminant
            sqrt_d = cmath.sqrt(discriminant)  

            # Compute solutions
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)

            # Display solutions
            print("\nSolutions:")
            print(f"x₁ = {x1.real:.3f} {'+ ' + str(x1.imag) + 'i' if x1.imag != 0 else ''}")
            print(f"x₂ = {x2.real:.3f} {'+ ' + str(x2.imag) + 'i' if x2.imag != 0 else ''}")

            # Completed square form: (x + b/2a)^2 - (discriminant/4a)
            completed_square_term = (b / (2*a)) ** 2 - (c / a)
            print("\nCompleted Square Form:")
            print(f"( x + {round(b / (2*a), 3)} )² + {round(completed_square_term, 3)} = 0")
        
        except InvalidOperation:
            print("Invalid value for quadratic. Please try again.")

def calculate_factorial():
    # Procedure for factorial calculation
    try:
        factorial_argument = int(input("Please enter argument of factorial: "))
        try:
            print(math.factorial(factorial_argument))
        except ValueError:
            print("Invalid value for a factorial. Please enter a positive integer.")

    except ValueError:
        print("Invalid value for factorial. Please enter a positive integer.")

def calculate_permutation():
    # Procedure for permutation calculation
    try:
        print("A permutation can be defined as nPr = n!/(n-r)!")
        permutation_n = int(input("Please enter n value: "))
        permutation_n_factorial = math.factorial(permutation_n)

        print("n! =",permutation_n_factorial)
        permutation_n_minus_r = permutation_n - int(input("Please enter r value: "))
        permutation_n_minus_r_factorial = math.factorial(permutation_n_minus_r)

        print("nPr =", permutation_n_factorial / permutation_n_minus_r_factorial)
    except ValueError:
        print("Invalid value. Please enter a positive integer where n > r.")
    except ZeroDivisionError:
        print("Invalid value. Please make it so that n > r.")

# POLYGON AND SOLID CALCULATOR
#2D Area
def parallelogram_rectangle_area():
    try:
        rectangle_area_base = get_decimal_input("Enter base length: ")
        
        rectangle_area_height = get_decimal_input("Enter height: ")
        
        rectangle_area_unit = get_decimal_input("Enter unit of length: ")

        print("Parallelogram/rectangle area is",round(rectangle_area_base*rectangle_area_height,3),rectangle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def triangle_area():
    try:
        triangle_area_base = get_decimal_input("Enter base length: ")
        
        triangle_area_height = get_decimal_input("Enter perpendicular height: ")
        
        triangle_area_unit = input("Enter unit of length: ")

        print("Triangle area is",round(Decimal(0.5)*triangle_area_base*triangle_area_height,3),triangle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def circle_area():
    try:
        circle_area_radius = get_decimal_input("Enter radius length: ")
        
        circle_area_unit = input("Enter unit of length: ")

        print("Circle area is",round(Decimal(math.pi)*circle_area_radius**2,3),circle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def trapezium_area():
    try:
        trapezium_area_length_a = get_decimal_input("Enter first side length: ")
        
        trapezium_area_length_b = get_decimal_input("Enter second side length: ")
        
        trapezium_area_height = get_decimal_input("Enter perpendicular height: ")
        
        trapezium_area_unit = input("Enter unit of length: ")

        print("Trapezium (UK definition) area is",round(Decimal(0.5)*(trapezium_area_length_a+trapezium_area_length_b)*
                                                        trapezium_area_height,3),trapezium_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

#VOLUME
def cuboid_volume():
    try:
        cuboid_volume_l = get_decimal_input("Enter length of base: ")
        
        cuboid_volume_w = get_decimal_input("Enter width of base: ")

        cuboid_volume_h = get_decimal_input("Enter height of cuboid: ")
        
        cuboid_volume_unit = input("Enter length unit: ")

        print("Volume of cuboid is",round(cuboid_volume_l*cuboid_volume_w*cuboid_volume_h,3),cuboid_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def cylinder_volume():
    try:
        cylinder_volume_r = get_decimal_input("Enter radius of base: ")
        
        cylinder_volume_h = get_decimal_input("Enter height of cylinder: ")
        
        cylinder_volume_unit = input("Enter length unit: ")

        print("Volume of cylinder is",round((Decimal(math.pi)*cylinder_volume_r**2)*cylinder_volume_h,3),cylinder_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")
def triangle_prism_volume():
    try:
        triangle_prism_volume_b = get_decimal_input("Enter base length: ")
        
        triangle_prism_volume_hb = get_decimal_input("Enter perpendicular height of base: ")
    
        triangle_prism_volume_hp = get_decimal_input("Enter height of prism: ")
        
        triangle_prism_volume_unit = input("Enter unit of length: ")

        print("Volume of triangular prism is",round(Decimal(0.5)*triangle_prism_volume_b*
                                                    triangle_prism_volume_hb*triangle_prism_volume_hp,3),
                                                    triangle_prism_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def sphere_volume():
    try:
        sphere_volume_r = get_decimal_input("Enter sphere radius: ")

        sphere_volume_unit = input("Enter length unit: ")

        print("Volume of sphere is",round(Decimal(4/3)*Decimal(math.pi)*sphere_volume_r**3,3),sphere_volume_unit+"^3")

    except InvalidOperation:
            print("Invalid value. Please enter a number.")

def rectangle_pyramid_volume():
    try:
        rectangle_pyramid_volume_l = get_decimal_input("Enter base length: ")
        
        rectangle_pyramid_volume_w = get_decimal_input("Enter base width: ")
        
        rectangle_pyramid_volume_h = get_decimal_input("Enter pyramid height: ")

        rectangle_pyramid_volume_unit = input("Enter length unit: ")

        print("Volume of rectangle-based pyramid is",
              round(Decimal(1/3)*rectangle_pyramid_volume_l*rectangle_pyramid_volume_w*rectangle_pyramid_volume_h,3),
              rectangle_pyramid_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def tetrahedron_volume():
    try:
        tetrahedron_volume_l = get_decimal_input("Enter side length: ")
        
        tetrahedron_volume_unit = input("Please enter length unit: ")

        print("Volume of regular tetrahedron is",round((tetrahedron_volume_l**3)/(6*2**Decimal(1/2)),3),tetrahedron_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def cone_volume():
    try:
        cone_volume_r = get_decimal_input("Enter base radius: ")

        cone_volume_h = get_decimal_input("Enter perpendicular height of cone: ")
        
        cone_volume_unit = input("Enter length unit: ")

        print("Volume of cone is",round(Decimal(1/3)*Decimal(math.pi)*(cone_volume_r**2)*cone_volume_h,3),cone_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value, please enter number.")

#SURFACE AREA
def cuboid_sa():
    try:
        cuboid_sa_l = get_decimal_input("Enter cuboid length: ")
        
        cuboid_sa_w = get_decimal_input("Enter cuboid width: ")
        
        cuboid_sa_h = get_decimal_input("Enter cuboid height: ")

        cuboid_sa_unit = input("Enter length unit: ")

        print("Cuboid surface area is",round(2*cuboid_sa_l*cuboid_sa_w+2*cuboid_sa_l*cuboid_sa_h+2*cuboid_sa_h*cuboid_sa_w,3),cuboid_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def cylinder_sa():
    try:
        cylinder_sa_r = get_decimal_input("Enter base radius: ")
        
        cylinder_sa_h = get_decimal_input("Enter cylinder height: ")
        
        cylinder_sa_unit = input("Enter length unit: ")

        print("Cylinder surface area is",round(2*Decimal(math.pi)*cylinder_sa_r*cylinder_sa_h+2*math.pi*cylinder_sa_r**2,3),cylinder_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def triangle_prism_sa():
    try:
        triangle_prism_sa_b = get_decimal_input("Enter base length: ")
        
        triangle_prism_sa_s1 = get_decimal_input("Enter second base edge length: ")
        
        triangle_prism_sa_s2 = get_decimal_input("Enter third base edge length: ")
        
        triangle_prism_sa_h = get_decimal_input("Enter base perpendicular height: ")
        
        triangle_prism_sa_unit = input("Enter unit: ")

        print("Triangular prism surface area is",round(triangle_prism_sa_b*triangle_prism_sa_h+
                                                       (triangle_prism_sa_b+triangle_prism_sa_s1+triangle_prism_sa_s2)*triangle_prism_sa_h,3),
                                                        triangle_prism_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def sphere_sa():
    try:
        sphere_sa_r = get_decimal_input("Enter base radius: ")
    
        sphere_sa_unit = input("Enter unit: ")

        print("Sphere surface area is",round(4*Decimal(math.pi)*sphere_sa_r**2,3),sphere_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def rectangle_pyramid_sa():
    try:
        pyramid_sa_base_l = get_decimal_input("Enter base length: ")
        
        pyramid_sa_base_w = get_decimal_input("Enter base width: ")
        
        pyramid_sa_h = get_decimal_input("Enter pyramid height: ")
        
        pyramid_sa_unit = input("Enter length unit: ")

        print("Surface area of square-based pyramid is",round(pyramid_sa_base_l*pyramid_sa_base_w+
                                                              pyramid_sa_base_l*((pyramid_sa_base_w/2)**2+pyramid_sa_h**2)**Decimal(1/2)+
                                                              pyramid_sa_base_w*((pyramid_sa_base_l/2)**2+pyramid_sa_h**2)**Decimal(1/2),3),
                                                              pyramid_sa_unit+"^2")
    except InvalidOperation:
        print("Invalid value for square-based pyramid, please enter number.")

def tetrahedron_sa():
    try:
        tetrahedron_sa_side = get_decimal_input("Enter tetrahedrone side length: ")
        
        tetrahedron_sa_unit = input("Enter length unit: ")

        print("Surface area of regular tetrahedron is",round(Decimal(math.sqrt(3))*tetrahedron_sa_side**2,3),tetrahedron_sa_unit+"^2")
    
    except InvalidOperation:
        print("Invalid value for tetrahedron side length, please enter number.")

def cone_sa():
    try:
        cone_sa_r = get_decimal_input("Enter cone base radius: ")
        
        cone_sa_h = get_decimal_input("Enter perpendicular height of cone: ")
        
        cone_sa_unit = input("Enter length unit: ")

        print("Surface area of cone is",round((Decimal(math.pi) * cone_sa_r) * (cone_sa_r + Decimal(math.sqrt(cone_sa_h**2 + cone_sa_r**2))), 3), cone_sa_unit+ "^2")

    except InvalidOperation:
        print("Invalid value for cone property, please enter number.")

# STATISTICS

def get_number_list():
    # Prompts user to enter a list of numbers separated by spaces or commas
    while True:
        try:
            user_input = input("Please enter numbers separated by commas or spaces: ")
            num_list = [Decimal(num) for num in user_input.replace(',',' ').split()]
            if not num_list:
                print("Please enter at least one number.")
                continue
            return num_list
        except InvalidOperation:
            print("Invalid input. Please enter numbers separated by spaces or commas.")

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
    # Handles unit conversion choices

    print("\n--- UNIT CONVERSION ---")
    from_unit = input("Enter the current unit (e.g., mm, cm, m, km): ").lower()
    to_unit = input("Enter the unit to convert to: ").lower()
    value = get_decimal_input("Enter the value to convert: ")

    converted_value = convert_units(value, from_unit, to_unit)
    if converted_value is not None:
        print(f"{value} {from_unit} is {converted_value} {to_unit}")

def shape_calculator_menu():
    # Handles shape calculation
    print("\n--- POLYGON AND SOLID CALCULATOR ---")
    print("1: 2D Object Area")
    print("2: 3D Object Volume")
    print("3: 3D Object Surface Area")
    print("X: Return to Main Menu")

    choice = input("Enter an option: ").upper()

    if choice == "1":
        print("Choose shape:")
        print("A: Parallelogram/Rectangle")
        print("B: Triangle")
        print("C: Circle")
        print("D: Trapezium")
        shapes = {
            "A": parallelogram_rectangle_area,
            "B": triangle_area,
            "C": circle_area,
            "D": trapezium_area
        }
        shape_choice = input("Enter shape: ").upper()
        if shape_choice in shapes:
            shapes[shape_choice]()

    elif choice == "2":
        print("Choose volume calculation:")
        print("A: Cuboid")
        print("B: Cylinder")
        print("C: Triangular Prism")
        print("D: Sphere")
        volumes = {
            "A": cuboid_volume,
            "B": cylinder_volume,
            "C": triangle_prism_volume,
            "D": sphere_volume
        }
        volume_choice = input("Enter shape: ").upper()
        if volume_choice in volumes:
            volumes[volume_choice]()

    elif choice == "3":
        print("Choose surface area calculation:")
        print("A: Cuboid")
        print("B: Cylinder")
        print("C: Sphere")
        surfaces = {
            "A": cuboid_sa,
            "B": cylinder_sa,
            "C": sphere_sa
        }
        surface_choice = input("Enter shape: ").upper()
        if surface_choice in surfaces:
            surfaces[surface_choice]()

    elif choice == "X":
        return
    
    else:
        print("Invalid option.")

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
            "A": math.pi,
            "B": math.e,
            "C": 1.61803398875,  # Golden Ratio
            "D": math.tau
        }
        print("A: π (pi)")
        print("B: e (Euler's Constant)")
        print("C: φ (Golden Ratio)")
        print("D: τ (Circle Constant)")
        math_choice = input("Choose a constant: ").upper()
        if math_choice in math_constants:
            global constant_memory
            constant_memory = Decimal(math_constants[math_choice])
            print(f"Saved {math_constants[math_choice]} to memory.")

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

# Run the main menu
main_menu()