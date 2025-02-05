from decimal import Decimal, getcontext, InvalidOperation
import math
import cmath
import statistics
choice = ""
constant_memory = 1
getcontext().prec = 40

########################
# P R O C E D U R E S  #
########################

def get_decimal_input(prompt):
    while True:
        try:
            value = input(prompt).upper()
            return constant_memory if value == "MEMORY" else Decimal(value)
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def convert_units(value, from_unit, to_unit):
        """Converts between units using a base unit system."""
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
    while True:
        try:

            simple_operators = {
                "+":lambda x, y : x + y,
                "-":lambda x, y : x - y,
                "/":lambda x, y : x / y,
                "*":lambda x, y : x * y,
                "**":lambda x,y : x ** y
                }        
                
            simple_calc_1 = input("Enter first value: ")
            simple_calc_1 = simple_calc_1.upper()
            simple_calc_1 = constant_memory if simple_calc_1 == "MEMORY" else Decimal(simple_calc_1)
            simple_calc_2 = input("Enter second value: ")
            simple_calc_2 = simple_calc_2.upper()
            simple_calc_2 = constant_memory if simple_calc_2 == "MEMORY" else Decimal(simple_calc_2)
            
            simple_calc_op = input("Enter operation: ")
            
            if simple_calc_op in simple_operators:
                simple_calc_ans = simple_operators[simple_calc_op](simple_calc_1,simple_calc_2)
                print(round(simple_calc_ans,3))
                break
            else:
                print("Invalid operator, please try again.")

        except InvalidOperation:
            print("Invalid value entered, please try again.")


# ADVANCED ARITHMETIC

def calculate_surd():
    while True: 
        try:
            adv_surd_1 = get_decimal_input("Enter value to be rooted: ")
        
            adv_root = get_decimal_input("Enter nth root: ")
            
            print(round(adv_surd_1**(1/adv_root),3))
            break
        except InvalidOperation:
            print("Invalid value. Please enter a number.")

def calculate_logarithm():
    while True:
        try:
            adv_logbase = get_decimal_input("Please enter base of log: ")
            
            adv_logargument = get_decimal_input("Please enter argument of log: ")
                                                                                  
            print(round(math.log(adv_logargument,adv_logbase),3))
            break
        except InvalidOperation:
            print("Invalid value for logarithm. Please enter a positive real number.")

def calculate_quadratic():
    while True:
        try:
            print("Quadratic Equation: ax^2 + bx + c = 0")
            a = get_decimal_input("Enter value for a: ")
            b = get_decimal_input("Enter value for b: ")
            c = get_decimal_input("Enter value for c: ")

            if a == 0:
                print("This is not a quadratic equation (a cannot be 0).")
                return

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
    try:
        adv_factorial = int(input("Please enter value to be factorial'd: "))
        print(math.factorial(adv_factorial))

    except ValueError:
        print("Invalid value for factorial. Please enter a positive integer.")

def calculate_permutation():
    try:
        print("A permutation can be defined as n!/(n-r)!")
        adv_perm_n = int(input("Please enter n value: "))
        adv_perm_n_fact = math.factorial(adv_perm_n)
        print("n! =",adv_perm_n_fact)
        adv_perm_n_minus_r = adv_perm_n - int(input("Please enter r value: "))
        adv_perm_n_minus_r_fact = math.factorial(adv_perm_n_minus_r)
        print("(n-r)! =",adv_perm_n_minus_r_fact)
        print("n!/(n-r)!=",adv_perm_n_fact/adv_perm_n_minus_r_fact)
    except ValueError:
        print("Invalid value. Please enter a positive integer where n > r.")
    except ZeroDivisionError:
        print("Invalid value. Please make it so that n > r.")



# UNIT CONVERSIONS

#DISTANCE

def mm_to_cm(distance):
    return distance / Decimal(10)
def cm_to_m(distance):
    return distance / Decimal(100)
def m_to_km(distance):
    return distance / Decimal(1000)
def km_to_m(distance):
    return distance * Decimal(1000)
def m_to_cm(distance):
    return distance * Decimal(1000)
def cm_to_mm(distance):
    return distance * Decimal(100)
def km_to_mi(distance):
    return distance / Decimal(1.609)
def mi_to_km(distance):
    return distance * Decimal(1.609)
def cm_to_ft(distance):
    return distance / Decimal(30.48)
def ft_to_cm(distance):
    return distance * Decimal(0.48)
def m_to_yds(distance):
    return distance * Decimal(1.094)
def yds_to_m(distance):
    return distance / Decimal(1.094)

#AREA

def mm2_to_cm2(area):
    return area / Decimal(100)
def cm2_to_m2(area):
    return area / Decimal(10000)
def m2_to_km2(area):
    return area / Decimal(1000000)
def km2_to_m2(area):
    return area * Decimal(1000000)
def m2_to_cm2(area):
    return area * Decimal(10000)
def cm2_to_mm2(area):
    return area * Decimal(100)
def km2_to_ha(area):
    return area * Decimal(100)
def ha_to_km2(area):
    return area / Decimal(100)
def m2_to_ac(area):
    return area / Decimal(4047)
def ac_to_m2(area):
    return area * Decimal(4047)

#VOLUME

def mm3_to_l(volume):
    return volume / Decimal(1000000)
def l_to_m3(volume):
    return volume / Decimal(1000)
def m3_to_ml(volume):
    return volume * Decimal(1000000)
def ml_to_m3(volume):
    return volume / Decimal(1000000)
def l_to_ml(volume):
    return volume * Decimal(1000)
def ml_to_l(volume):
    return volume / Decimal(1000)
def fl_oz_to_ml(volume):
    return volume * Decimal(29.57353)
def ml_to_fl_oz(volume):
    return volume / Decimal(29.57353)
def gal_to_l(volume):
    return volume * Decimal(3.78541)
def l_to_gal(volume):
    return volume / Decimal(3.78541)

#MASS

def mg_to_g(mass):
    return mass / Decimal(1000)
def g_to_kg(mass):
    return mass / Decimal(1000)
def kg_to_t(mass):
    return mass / Decimal(1000)
def t_to_kg(mass):
    return mass * Decimal(1000)
def kg_to_g(mass):
    return mass * Decimal(1000)
def g_to_mg(mass):
    return mass * Decimal(1000)
def kg_to_lbs(mass):
    return mass * Decimal(2.20462)
def lbs_to_kg(mass):
    return mass / Decimal(2.20462)
def kg_to_st(mass):
    return mass * Decimal(0.157473)
def st_to_kg(mass):
    return mass / Decimal(0.157473)
def g_to_oz(mass):
    return mass / Decimal(28.3495)
def oz_to_g(mass):
    return mass * Decimal(28.3495)


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

        print("Surface area of cone is",round((Decimal(math.pi)*cone_sa_r)*(cone_sa_r+Decimal(math.sqrt(cone_sa_h**2+cone_sa_r**2))),3),cone_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value for cone property, please enter number.")

# STATISTICS

def mean():
    mean_list = []
    while True:
        try:
            mean_number = ""
                
            mean_number = input("Please enter number (X to stop): ")
            mean_number = mean_number.upper()

            if mean_number == "X" and len(mean_list) != 0:
                print(f"Mean of {', '.join(str(x) for x in mean_list)} is {sum(mean_list)/len(mean_list)}")
                print(f"There were a total of {len(mean_list)} elements.")
                break

            elif mean_number == "X":
                print("Returning to menu...")
                break
            
            mean_number = constant_memory if mean_number == "MEMORY" else Decimal(mean_number)
            mean_list.append(mean_number)
            
            print([str(x) for x in mean_list])

        except InvalidOperation:
            print("Invalid value, please enter a number.")

def median():
    median_list = []
    while True:
        try:
            median_number = input("Please enter a number (X to stop): ")
            median_number = median_number.upper()
            median_list.sort()

            if median_number == "X" and len(median_list) != 0:
                print(f"Median of {', '.join(str(x) for x in median_list)} is {statistics.median(median_list)}")
                print(f"There were {len(median_list)} elements")
                break
            elif median_number == "X" and len(median_list) == 0:
                print("Returning to menu...")
                break

            median_number = constant_memory if median_number == "MEMORY" else Decimal(median_number)
            median_list.append(median_number)

            print([str(x) for x in median_list])
                

        except InvalidOperation:
            print("Invalid value, please enter a number.")

def mode():
    mode_list = []
    while True:
        try:
            mode_number = input("Please enter a number (X to stop): ")
            mode_number = mode_number.upper()
            
            if mode_number == "X" and len(mode_list) != 0:
                print(f"Mode of {', '.join(str(x) for x in mode_list)} is {statistics.mode(mode_list)}")
                print(f"There were {len(mode_list)} elements")
                break
            elif mode_number == "X" and len(mode_list) == 0:
                print("Returning to menu...")
                break

            mode_number = constant_memory if mode_number == "MEMORY" else Decimal(mode_number)
            mode_list.append(mode_number)

            print([str(x) for x in mode_list])

        except InvalidOperation:
            print("Invalid value, please enter number.")

def iqr():
    iqr_list = []
    while True:
        try:
            iqr_number = input("Please enter number (X to stop): ")
            iqr_number = iqr_number.upper()
            iqr_list.sort()

            if iqr_number == "X" and len(iqr_list) != 0:
                iqr_lower_half = [x for x in iqr_list if x <=
                                      statistics.median(iqr_list)]
                iqr_upper_half = [x for x in iqr_list if x >=
                                  statistics.median(iqr_list)]
                
                iqr_q1 = statistics.median(iqr_lower_half)
                iqr_q3 = statistics.median(iqr_upper_half)

                print(f"Lower Quartile: {iqr_q1}")
                print(f"Upper Quartile: {iqr_q3}")
                print(f"Interquartile range: {iqr_q3-iqr_q1}")
                break

            elif iqr_number == "X" and len(iqr_list) == 0:
                print("Returning to menu...")
                break

            iqr_number = constant_memory if iqr_number == "MEMORY" else Decimal(iqr_number)
            iqr_list.append(iqr_number)

            print([str(x) for x in iqr_list])

        except InvalidOperation:
            print("Invalid value, please enter a number.")

def statistics_range():
    range_list = []
    while True:
        try:
            range_number = input("Please enter number: ")
            range_number = range_number.upper()

            if range_number == "X" and len(range_list) != 0:
                print(f"Range: {max(range_list) - min(range_list)}")
                break
            
            elif range_number == "X" and len(range_list) == 0:
                print("Returning to menu...")
                break

            range_number = constant_memory if range_number == "MEMORY" else Decimal(range_number)
            range_list.append(range_number)

            print([str(x) for x in range_list])

        except InvalidOperation:
            print("Invalid value, please enter a number: ")
            
                

while choice != "X":

    print("\n==== C A L C U L A T O R ===")
    print("Welcome to Arash's calculator. Please pick an option: ")
    
    print("A: Simple Arithmetic")
    print("B: Advanced Arithmetic")
    print("C: Unit Conversion")
    print("D: Polygon and Solid calculator")
    print("E: Common constants")
    print("F: Statistics")
    print("X: exit")

    choice = input("Please enter an option here: ")
    choice = choice.upper()
    if choice == "A":
        print("--- SIMPLE ARITHMETIC ---")
        print("This section covers the simplest, most fundamental mathematical concepts.")
        print("Operators:")
        print("Addition (+)")
        print("Subtraction (-)")
        print("Multiplication (* or x)")
        print("Division (/)")
        print("Exponents/Power (**)")

        simple_arithmetic()

    elif choice == "B":

        adv_arithmetic_operators = {
            "A": calculate_surd,
            "B": calculate_logarithm,
            "C": calculate_quadratic,
            "D": calculate_factorial,
            "E": calculate_permutation,
            }

        
        print("--- ADVANCED ARITHMETIC ---")
        print("This section covers more advanced mathematical concepts.")
        print("Operations: ")
        print("A: Surds (Rooting)")
        print("B: Logarithms")
        print("C: Quadratics")
        print("D: Factorials")
        print("E: Permutations")

        adv_choice = input("Please enter option: ")
        adv_choice = adv_choice.upper()
        if adv_choice in adv_arithmetic_operators:
            adv_arithmetic_operators[adv_choice]()
        else:
            print("Invalid operation, please try again.")
            
            
    elif choice == "C":
        print("--- UNIT CONVERSION ---")
        print("This section allows you to convert values from different units, including Metric to Imperial system units.")
       
        unit_factors = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "mi": 1609.34, "yds": 0.9144, "ft": 0.3048,
        "mm2": 1e-6, "cm2": 1e-4, "m2": 1, "km2": 1e6, "ha": 1e4, "ac": 4046.86,
        "mm3": 1e-9, "cm3": 1e-6, "m3": 1, "l": 1e-3, "ml": 1e-6, "fl_oz": 2.95735e-5, "gal": 3.78541e-3,
        "mg": 1e-6, "g": 1e-3, "kg": 1, "t": 1000, "lbs": 0.453592, "st": 6.35029, "oz": 0.0283495
    }

        while True:
            from_unit = input("Enter the current unit (e.g., mm, cm, m, km): ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            value = get_decimal_input("Enter the value to convert: ")

            converted_value = convert_units(value, from_unit, to_unit)
            if converted_value is not None:
                print(f"{value} {from_unit} is {converted_value} {to_unit}")

            if input("Convert another? (Y/N): ").upper() != "Y":
                break
                                
    elif choice == "D":
        print("--- POLYGON AND SOLID CALCULATOR ---")
        print("This section calculates the areas and volumes of certain 2D and 3D objects.")
        print("Operations:")
        print("A: 2D Object area calculator")
        print("B: Volume calculator")
        print("C: 3D Object area calculator")

        polygon_solid_choice = input("Please enter chosen operation: ")
        polygon_solid_choice = polygon_solid_choice.upper()

        if polygon_solid_choice == "A":

            area_calc_operators = {
                "A": parallelogram_rectangle_area,
                "B": triangle_area,
                "C": circle_area,
                "D": trapezium_area,
                }
            
            print("- AREA CALCULATOR -")
            print("A: Parallelogram/Rectangle")
            print("B: Triangle")
            print("C: Circle")
            print("D: Trapezium (UK)")

            area_calc_choice = input("Please enter shape to be calculated: ")
            area_calc_choice = area_calc_choice.upper()

            if area_calc_choice in area_calc_operators:
                area_calc_operators[area_calc_choice]()
            else:
                print("Invalid operation, please try again.")
                
        elif polygon_solid_choice == "B":
            print("- VOLUME CALCULATOR -")
            print("A: Prism")
            print("B: Sphere")
            print("C: Pyramid")

            volume_choice = input("Please enter shape to be calculated: ")
            volume_choice = volume_choice.upper()

            if volume_choice == "A":

                prism_volume_operators = {
                "A": cuboid_volume,
                "B": cylinder_volume,
                "C": triangle_prism_volume,
                }
                
                print("- PRISM VOLUME CALCULATOR -")
                print("A: Cuboid")
                print("B: Cylinder")
                print("C: Triangular prism")

                prism_volume_choice = input("Please enter shape to be calculated: ")
                prism_volume_choice = prism_volume_choice.upper()

                if prism_volume_choice in prism_volume_operators:
                    prism_volume_operators[prism_volume_choice]()
                else:
                    print("Invalid operation, please try again.")
                    
            elif volume_choice == "B":
            
                    sphere_volume()
                    
            elif volume_choice == "C":

                pyramid_volume_operators = {
                    "A": rectangle_pyramid_volume,
                    "B": tetrahedron_volume,
                    "C": cone_volume,
                    }
                
                print("- PYRAMID VOLUME CALCULATOR -")
                print("A: Rectangle-based pyramid")
                print("B: Regular tetrahedron")
                print("C: Cone")

                pyramid_volume_choice = input("Please enter shape to be calculated: ")
                pyramid_volume_choice = pyramid_volume_choice.upper()

                if pyramid_volume_choice in pyramid_volume_operators:
                    pyramid_volume_operators[pyramid_volume_choice]()
                else:
                    print("Invalid operation, please try again.")
                    
        if polygon_solid_choice == "C":            
            print("- SURFACE AREA CALCULATOR -")
            print("A: Prism")
            print("B: Sphere")
            print("C: Pyramid")

            sa_choice = input("Please enter shape to be calculated: ")
            sa_choice = sa_choice.upper()

            if sa_choice == "A" or sa_choice == "PRISM":

                prism_sa_operators = {
                    "A": cuboid_sa,
                    "B": cylinder_sa,
                    "C": triangle_prism_sa,
                    }
                
                print("- PRISM SURFACE AREA CALCULATOR -")
                print("A: Cuboid")
                print("B: Cylinder")
                print("C: Triangular prism")

                prism_sa_choice = input("Please enter shape to be calculated: ")
                prism_sa_choice = prism_sa_choice.upper()

                if prism_sa_choice in prism_sa_operators:
                    prism_sa_operators[prism_sa_choice]()
                else:
                    print("Invalid operation, please try again.")
                    
            elif sa_choice == "B" or sa_choice == "SPHERE":
                
                sphere_sa()
                
            elif sa_choice == "C" or sa_choice == "PYRAMID":

                pyramid_sa_operators = {
                    "A": rectangle_pyramid_sa,
                    "B": tetrahedron_sa,
                    "C": cone_sa,
                    }
                
                print("- PYRAMID SURFACE AREA CALCULATOR -")
                print("A: Rectangle-based pyramid")
                print("B: Regular tetrahedron")
                print("C: Cone")

                pyramid_sa_choice = input("Please choose shape to be calculated: ")
                pyramid_sa_choice = pyramid_sa_choice.upper()

                if pyramid_sa_choice in pyramid_sa_operators:
                    pyramid_sa_operators[pyramid_sa_choice]()
                else:
                    print("Invalid operator, please try again.")

    elif choice == "E":
        print("- COMMON CONSTANTS -")
        print("This section allows you to use and retrieve common constants to use in your operations.")
        print("Once you have selected a constant, type 'memory' when performing calculation to input stored value.")
        print("A: Mathematical")
        print("B: Scientific")
        print("C: Save your own value.")

        constants_choice = input("Please enter constant option: ")
        constants_choice = constants_choice.upper()

        if constants_choice == "A":

            math_constants = {
                "A":math.pi,
                "B":math.e,
                "C":1.61803398875,
                "D":math.tau
                }
            
            print("- MATHEMATICAL CONSTANTS -")
            print("A: π (pi)")
            print("B: e (Euler's constant)")
            print("C: φ (Golden ratio)")
            print("D: τ (Circle constant)")

            math_constants_choice = input("Please enter constant option: ")
            math_constants_choice = math_constants_choice.upper()

            if math_constants_choice in math_constants:
                constant_memory = Decimal(math_constants[math_constants_choice])
                print("Saved to memory, please access saved value in")
                print("calculation by typing 'memory' into input prompt.")
            else:
                print("Invalid option, please try again.")

        elif constants_choice == "B":
            
            scientific_constants = {
                "A": "6.02e23",
                "B": "2.99792458e8",
                "C": "6.67430e-11",
                "D": "6.62607015e-34"
                }
                
            print("- SCIENTIFIC CONSTANTS -")
            print("A: Nₐ (Avogadro's constant)")
            print("B: c (Speed of light)")
            print("C: G (Gravitational constant)")
            print("D: h (Planck's constant)")

            science_constants_choice = input("Please enter constants option: ")
            science_constants_choice = science_constants_choice.upper()

            if science_constants_choice in scientific_constants:
                constant_memory = Decimal(scientific_constants[science_constants_choice])
                print("Saved to memory, please access saved value in")
                print("calculation by typing 'memory' into input prompt.")
            else:
                print("Invalid option, please try again.")

        elif constants_choice == "C":
            try:
                constant_memory = Decimal(input("Please enter value to store: "))
                print("Saved to memory, please access saved value in")
                print("calculation by typing 'memory' into input prompt.")
            except InvalidOperation:
                print("Invalid! Enter a number")

    elif choice == "F":

        statistics_operators = {
            "A": mean,
            "B": median,
            "C": mode,
            "D": statistics_range,
            "E": iqr
            }


        print("- STATISTICS -")
        print("This section deals with statistical mathematics.")
        print("A: Mean")
        print("B: Median")
        print("C: Mode")
        print("D: Range")
        print("E: IQR")

        statistics_choice = input("Please enter chosen operation: ")
        statistics_choice = statistics_choice.upper()

        if statistics_choice in statistics_operators:
            statistics_operators[statistics_choice]()
        else:
            print("Invalid operator, please try again.")
        
    elif choice == "X":
        print("Exiting...")

    else:
        print("Invalid option. Please try again.")


            
                
    
            
            
                        

        
