from decimal import Decimal, getcontext, InvalidOperation
import math
import statistics
choice = ""
constant_memory = 1
getcontext().prec = 40

########################
# P R O C E D U R E S  #
########################

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
            adv_surd_1 = input("Enter value to be rooted: ")
            adv_surd_1 = adv_surd_1.upper()
            adv_surd_1 = constant_memory if adv_surd_1 == "MEMORY" else Decimal(adv_surd_1)
            
            adv_root = input("Enter nth root: ")
            adv_root = adv_root.upper()
            adv_root = constant_memory if adv_root == "MEMORY" else Decimal(adv_root)
            
            print(round(adv_surd_1**(1/adv_root),3))
            break
        except InvalidOperation:
            print("Invalid value. Please enter a number.")

def calculate_logarithm():
    while True:
        try:
            adv_logbase = input("Please enter base of log: ")
            adv_logbase = adv_logbase.upper()
            adv_logbase = constant_memory if adv_logbase == "MEMORY" else Decimal(adv_logbase)
            
            adv_logargument = input("Please enter argument of log: ")
            adv_logargument = adv_logargument.upper()
            adv_logargument = constant_memory if adv_logargument == "MEMORY" else Decimal(adv_logargument)
                                                                                  
            print(round(math.log(adv_logargument,adv_logbase),3))
            break
        except InvalidOperation:
            print("Invalid value for logarithm. Please enter a positive real number.")

def calculate_quadratic():
    while True:
        try:
            print("ax^2+bx+c = 0")
            quadratic_a = input("Please enter value for a: ")
            quadratic_a = quadratic_a.upper()
            quadratic_a = constant_memory if quadratic_a == "MEMORY" else Decimal(quadratic_a)

            quadratic_b = input("Please enter value for b: ")
            quadratic_b = quadratic_b.upper()
            quadratic_b = constant_memory if quadratic_b == "MEMORY" else Decimal(quadratic_b)
            
            quadratic_c = input("Please enter value for c: ")
            quadratic_c = quadratic_c.upper()
            quadratic_c = constant_memory if quadratic_c == "MEMORY" else Decimal(quadratic_c)
            
            discriminant = quadratic_b**2-4*quadratic_a*quadratic_c
            
            if discriminant < 0:
                print("Quadratic has no real roots.")
                break
            if discriminant == 0:
                print("Quadratic has one distinct real root.")
                print("x solution:", round((-quadratic_b+Decimal(math.sqrt(discriminant)))/2*quadratic_a,3))
                print("Completed square form: ( x +", quadratic_b/2, ")^2 +", ((quadratic_b/2)**2) + quadratic_c)
                break
            else:
                print("First x solution:", round((-quadratic_b+Decimal(math.sqrt(discriminant)))/2*quadratic_a,3))
                print("Second x solution:", round((-quadratic_b-Decimal(math.sqrt(discriminant)))/2*quadratic_a,3))
                print("Completed square form: ( x +",round(quadratic_b/2,3), ")^2 +", round(((quadratic_b/2)**2) + quadratic_c,3))
                break
        
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
        rectangle_area_base = input("Enter base length: ")
        rectangle_area_base = rectangle_area_base.upper()
        rectangle_area_base = constant_memory if rectangle_area_base == "MEMORY" else Decimal(rectangle_area_base)
        
        rectangle_area_height = input("Enter height: ")
        rectangle_area_height = rectangle_area_height.upper()
        rectangle_area_height = constant_memory if rectangle_area_height == "MEMORY" else Decimal(rectangle_area_height)
        
        rectangle_area_unit = input("Enter unit of length: ")

        print("Parallelogram/rectangle area is",round(rectangle_area_base*rectangle_area_height,3),rectangle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def triangle_area():
    try:
        triangle_area_base = input("Enter base length: ")
        triangle_area_base = triangle_area_base.upper()
        triangle_area_base = constant_memory if triangle_area_base == "MEMORY" else Decimal(triangle_area_base)
        
        triangle_area_height = input("Enter perpendicular height: ")
        triangle_area_height = triangle_area_height.upper()
        triangle_area_height = constant_memory if triangle_area_height == "MEMORY" else Decimal(triangle_area_height)
        
        triangle_area_unit = input("Enter unit of length: ")

        print("Triangle area is",round(Decimal(0.5)*triangle_area_base*triangle_area_height,3),triangle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def circle_area():
    try:
        circle_area_radius = input("Enter radius length: ")
        circle_area_radius = circle_area_radius.upper()
        circle_area_radius = constant_memory if circle_area_radius == "MEMORY" else Decimal(circle_area_radius)
        
        circle_area_unit = input("Enter unit of length: ")

        print("Circle area is",round(Decimal(math.pi)*circle_area_radius**2,3),circle_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def trapezium_area():
    try:
        trapezium_area_length_a = input("Enter first side length: ")
        trapezium_area_length_a = trapezium_area_length_a.upper()
        trapezium_area_length_a = constant_memory if trapezium_area_length_a == "MEMORY" else Decimal(trapezium_area_length_a)
        
        trapezium_area_length_b = input("Enter second side length: ")
        trapezium_area_length_b = trapezium_area_length_b.upper()
        trapezium_area_length_b = constant_memory if trapezium_area_length_b == "MEMORY" else Decimal(trapezium_area_length_b)
        
        trapezium_area_height = input("Enter perpendicular height: ")
        trapezium_area_height = trapezium_area_height.upper()
        trapezium_area_height = constant_memory if trapezium_area_height == "MEMORY" else Decimal(trapezium_area_height)
        
        trapezium_area_unit = input("Enter unit of length: ")

        print("Trapezium (UK definition) area is",round(Decimal(0.5)*(trapezium_area_length_a+trapezium_area_length_b)*
                                                        trapezium_area_height,3),trapezium_area_unit+"^2")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

#VOLUME
def cuboid_volume():
    try:
        cuboid_volume_l = input("Enter length of base: ")
        cuboid_volume_l = cuboid_volume_l.upper()
        cuboid_volume_l = constant_memory if cuboid_volume_l == "MEMORY" else Decimal(cuboid_volume_l)
        
        cuboid_volume_w = input("Enter width of base: ")
        cuboid_volume_w = cuboid_volume_w.upper()
        cuboid_volume_w = constant_memory if cuboid_volume_w == "MEMORY" else Decimal(cuboid_volume_w)
        
        cuboid_volume_h = input("Enter height of cuboid: ")
        cuboid_volume_h = cuboid_volume_h.upper()
        cuboid_volume_h = constant_memory if cuboid_volume_h == "MEMORY" else Decimal(cuboid_volume_h)
        
        cuboid_volume_unit = input("Enter length unit: ")

        print("Volume of cuboid is",round(cuboid_volume_l*cuboid_volume_w*cuboid_volume_h,3),cuboid_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def cylinder_volume():
    try:
        cylinder_volume_r = input("Enter radius of base: ")
        cylinder_volume_r = cylinder_volume_r.upper()
        cylinder_volume_r = constant_memory if cylinder_volume_r == "MEMORY" else Decimal(cylinder_volume_r)
        
        cylinder_volume_h = input("Enter height of cylinder: ")
        cylinder_volume_h = cylinder_volume_h.upper()
        cylinder_volume_h = constant_memory if cylinder_volume_h == "MEMORY" else Decimal(cylinder_volume_h)
        
        cylinder_volume_unit = input("Enter length unit: ")

        print("Volume of cylinder is",round((Decimal(math.pi)*cylinder_volume_r**2)*cylinder_volume_h,3),cylinder_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")
def triangle_prism_volume():
    try:
        triangle_prism_volume_b = input("Enter base length: ")
        triangle_prism_volume_b = triangle_prism_volume_b.upper()
        triangle_prism_volume_b = constant_memory if triangle_prism_volume_b == "MEMORY" else Decimal(triangle_prism_volume_b)
        
        triangle_prism_volume_hb = input("Enter perpendicular height of base: ")
        triangle_prism_volume_hb = triangle_prism_volume_hb.upper()
        triangle_prism_volume_hb = constant_memory if triangle_prism_volume_hb == "MEMORY" else Decimal(triangle_prism_volume_hb)
    
        triangle_prism_volume_hp = input("Enter height of prism: ")
        triangle_prism_volume_hp = triangle_prism_volume_hp.upper()
        triangle_prism_volume_hp = constant_memory if triangle_prism_volume_hp == "MEMORY" else Decimal(triangle_prism_volume_hp)
        
        triangle_prism_volume_unit = input("Enter unit of length: ")

        print("Volume of triangular prism is",round(Decimal(0.5)*triangle_prism_volume_b*
                                                    triangle_prism_volume_hb*triangle_prism_volume_hp,3),
                                                    triangle_prism_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def sphere_volume():
    try:
        sphere_volume_r = input("Enter sphere radius: ")
        sphere_volume_r = sphere_volume_r.upper()
        sphere_volume_r = constant_memory if sphere_volume_r == "MEMORY" else Decimal(sphere_volume_r)
        
        sphere_volume_unit = input("Enter length unit: ")

        print("Volume of sphere is",round(Decimal(4/3)*Decimal(math.pi)*sphere_volume_r**3,3),sphere_volume_unit+"^3")

    except InvalidOperation:
            print("Invalid value. Please enter a number.")

def rectangle_pyramid_volume():
    try:
        rectangle_pyramid_volume_l = input("Enter base length: ")
        rectangle_pyramid_volume_l = rectangle_pyramid_volume_l.upper()
        rectangle_pyramid_volume_l = constant_memory if rectangle_pyramid_volume_l == "MEMORY" else Decimal(rectangle_pyramid_volume_l)
        
        rectangle_pyramid_volume_w = input("Enter base width: ")
        rectangle_pyramid_volume_w = rectangle_pyramid_volume_w.upper()
        rectangle_pyramid_volume_w = constant_memory if rectangle_pyramid_volume_w == "MEMORY" else Decimal(rectangle_pyramid_volume_w)
        
        rectangle_pyramid_volume_h = input("Enter pyramid height: ")
        rectangle_pyramid_volume_h = rectangle_pyramid_volume_h.upper()
        rectangle_pyramid_volume_h = constant_memory if rectangle_pyramid_volume_h == "MEMORY" else Decimal(rectangle_pyramid_volume_h)
        
        rectangle_pyramid_volume_unit = input("Enter length unit: ")

        print("Volume of rectangle-based pyramid is",
              round(Decimal(1/3)*rectangle_pyramid_volume_l*rectangle_pyramid_volume_w*rectangle_pyramid_volume_h,3),
              rectangle_pyramid_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def tetrahedron_volume():
    try:
        tetrahedron_volume_l = input("Enter side length: ")
        tetrahedron_volume_l = tetrahedron_volume_l.upper()
        tetrahedron_volume_l = constant_memory if tetrahedron_volume_l == "MEMORY" else Decimal(tetrahedron_volume_l)
        
        tetrahedron_volume_unit = input("Please enter length unit: ")

        print("Volume of regular tetrahedron is",round((tetrahedron_volume_l**3)/(6*2**Decimal(1/2)),3),tetrahedron_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value. Please enter a number.")

def cone_volume():
    try:
        cone_volume_r = input("Enter base radius: ")
        cone_volume_r = cone_volume_r.upper()
        cone_volume_r = constant_memory if cone_volume_r == "MEMORY" else Decimal(cone_volume_r)
        
        cone_volume_h = input("Enter perpendicular height of cone: ")
        cone_volume_h = cone_volume_h.upper()
        cone_volume_h = constant_memory if cone_volume_h == "MEMORY" else Decimal(cone_volume_h)
        
        cone_volume_unit = input("Enter length unit: ")

        print("Volume of cone is",round(Decimal(1/3)*Decimal(math.pi)*(cone_volume_r**2)*cone_volume_h,3),cone_volume_unit+"^3")

    except InvalidOperation:
        print("Invalid value, please enter number.")

#SURFACE AREA
def cuboid_sa():
    try:
        cuboid_sa_l = input("Enter cuboid length: ")
        cuboid_sa_l = cuboid_sa_l.upper()
        cuboid_sa_l = constant_memory if cuboid_sa_l == "MEMORY" else Decimal(cuboid_sa_l)
        
        cuboid_sa_w = input("Enter cuboid width: ")
        cuboid_sa_w = cuboid_sa_w.upper()
        cuboid_sa_w = constant_memory if cuboid_sa_w == "MEMORY" else Decimal(cuboid_sa_w)
        
        cuboid_sa_h = input("Enter cuboid height: ")
        cuboid_sa_h = cuboid_sa_h.upper()
        cuboid_sa_h = constant_memory if cuboid_sa_h == "MEMORY" else Decimal(cuboid_sa_h)
        
        cuboid_sa_unit = input("Enter length unit: ")

        print("Cuboid surface area is",round(2*cuboid_sa_l*cuboid_sa_w+2*cuboid_sa_l*cuboid_sa_h+2*cuboid_sa_h*cuboid_sa_w,3),cuboid_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def cylinder_sa():
    try:
        cylinder_sa_r = input("Enter base radius: ")
        cylinder_sa_r = cylinder_sa_r.upper()
        cylinder_sa_r = constant_memory if cylinder_sa_r == "MEMORY" else Decimal(cylinder_sa_r)
        
        cylinder_sa_h = input("Enter cylinder height: ")
        cylinder_sa_h = cylinder_sa_h.upper()
        cylinder_sa_h = constant_memory if cylinder_sa_h == "MEMORY" else Decimal(cylinder_sa_h)
        
        cylinder_sa_unit = input("Enter length unit: ")

        print("Cylinder surface area is",round(2*Decimal(math.pi)*cylinder_sa_r*cylinder_sa_h+2*math.pi*cylinder_sa_r**2,3),cylinder_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def triangle_prism_sa():
    try:
        triangle_prism_sa_b = input("Enter base length: ")
        triangle_prism_sa_b = triangle_prism_sa_b.upper()
        triangle_prism_sa_b = constant_memory if triangle_prism_sa_b == "MEMORY" else Decimal(triangle_prism_sa_b)
        
        triangle_prism_sa_s1 = input("Enter second base edge length: ")
        triangle_prism_sa_s1 = triangle_prism_sa_s1.upper()
        triangle_prism_sa_s1 = constant_memory if triangle_prism_sa_s1 == "MEMORY" else Decimal(triangle_prism_sa_s1)
        
        triangle_prism_sa_s2 = input("Enter third base edge length: ")
        triangle_prism_sa_s2 = triangle_prism_sa_s2.upper()
        triangle_prism_sa_s2 = constant_memory if triangle_prism_sa_s2 == "MEMORY" else Decimal(triangle_prism_sa_s2)
        
        triangle_prism_sa_h = input("Enter base perpendicular height: ")
        triangle_prism_sa_h = triangle_prism_sa_h.upper()
        triangle_prism_sa_h = constant_memory if triangle_prism_sa_h == "MEMORY" else Decimal(triangle_prism_sa_h)
        
        triangle_prism_sa_unit = input("Enter unit: ")

        print("Triangular prism surface area is",round(triangle_prism_sa_b*triangle_prism_sa_h+
                                                       (triangle_prism_sa_b+triangle_prism_sa_s1+triangle_prism_sa_s2)*triangle_prism_sa_h,3),
                                                        triangle_prism_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def sphere_sa():
    try:
        sphere_sa_r = input("Enter base radius: ")
        sphere_sa_r = sphere_sa_r.upper()
        sphere_sa_r = constant_memory if sphere_sa_r == "MEMORY" else Decimal(sphere_sa_r)
        
        sphere_sa_unit = input("Enter unit: ")

        print("Sphere surface area is",round(4*Decimal(math.pi)*sphere_sa_r**2,3),sphere_sa_unit+"^2")

    except InvalidOperation:
        print("Invalid value, please enter number.")

def rectangle_pyramid_sa():
    try:
        pyramid_sa_base_l = input("Enter base length: ")
        pyramid_sa_base_l = pyramid_sa_base_l.upper()
        pyramid_sa_base_l = constant_memory if pyramid_sa_base_l == "MEMORY" else Decimal(pyramid_sa_base_l)
        
        pyramid_sa_base_w = input("Enter base width: ")
        pyramid_sa_base_w = pyramid_sa_base_w.upper()
        pyramid_sa_base_w = constant_memory if pyramid_sa_base_w == "MEMORY" else Decimal(pyramid_sa_base_w)
        
        pyramid_sa_h = input("Enter pyramid height: ")
        pyramid_sa_h = pyramid_sa_h.upper()
        pyramid_sa_h = constant_memory if pyramid_sa_h == "MEMORY" else Decimal(pyramid_sa_h)
        
        pyramid_sa_unit = input("Enter length unit: ")

        print("Surface area of square-based pyramid is",round(pyramid_sa_base_l*pyramid_sa_base_w+
                                                              pyramid_sa_base_l*((pyramid_sa_base_w/2)**2+pyramid_sa_h**2)**Decimal(1/2)+
                                                              pyramid_sa_base_w*((pyramid_sa_base_l/2)**2+pyramid_sa_h**2)**Decimal(1/2),3),
                                                              pyramid_sa_unit+"^2")
    except InvalidOperation:
        print("Invalid value for square-based pyramid, please enter number.")

def tetrahedron_sa():
    try:
        tetrahedron_sa_side = input("Enter tetrahedrone side length: ")
        tetrahedron_sa_side = tetrahedron_sa_side.upper()
        tetrahedron_sa_side = constant_memory if tetrahedron_sa_side == "MEMORY" else Decimal(tetrahedron_sa_side)
        
        tetrahedron_sa_unit = input("Enter length unit: ")

        print("Surface area of regular tetrahedron is",round(Decimal(math.sqrt(3))*tetrahedron_sa_side**2,3),tetrahedron_sa_unit+"^2")
    
    except InvalidOperation:
        print("Invalid value for tetrahedron side length, please enter number.")

def cone_sa():
    try:
        cone_sa_r = input("Enter cone base radius: ")
        cone_sa_r = cone_sa_r.upper()
        cone_sa_r = constant_memory if cone_sa_r == "MEMORY" else Decimal(cone_sa_r)
        
        cone_sa_h = input("Enter perpendicular height of cone: ")
        cone_sa_h = cone_sa_h.upper()
        cone_sa_h = constant_memory if cone_sa_h == "MEMORY" else Decimal(cone_sa_h)
        
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
        print("A: Distance")
        print("B: Area")
        print("C: Volume")
        print("D: Mass")

        try:

            unit_choice = input("Please pick an option: ")
            unit_choice = unit_choice.upper()

            if unit_choice == "A":
                print("- DISTANCE -")
                print("A: mm to cm")
                print("B: cm to m")
                print("C: m to km")
                print("D: km to m")
                print("E: m to cm")
                print("F: cm to mm")
                print("G: Metric-Imperial conversion")


                try:
                    
                    dist_value = input("Please enter distance: ")
                    dist_value = dist_value.upper()
                    dist_value = constant_memory if dist_value == "MEMORY" else Decimal(dist_value)
                    
                    dist_choice = input("Please choose a conversion: ")
                    dist_choice = dist_choice.upper()

                    if dist_choice == "A":
                        print(dist_value,"mm is",round(mm_to_cm(dist_value),3),"cm")
                    elif dist_choice == "B":
                        print(dist_value,"cm is",round(cm_to_m(dist_value),3),"m")
                    elif dist_choice == "C":
                        print(dist_value,"m is",round(m_to_km(dist_value),3),"km")
                    elif dist_choice == "D":
                        print(dist_value,"km is",round(km_to_m(dist_value),3),"m")
                    elif dist_choice == "E":
                        print(dist_value,"m is",round(m_to_cm(dist_value),3),"cm")
                    elif dist_choice == "F":
                        print(dist_value,"cm is",round(cm_to_mm(dist_value),3),"mm")

                    elif dist_choice == "G":
                        print("- METRIC-IMPERIAL DISTANCE CONVERSION -")
                        print("A: km to mi")
                        print("B: mi to km")
                        print("C: cm to ft")
                        print("D: ft to cm")
                        print("E: m to yds")
                        print("F: yds to m")
                        
                        d_imp_choice = input("Please enter conversion: ")
                        d_imp_choice = d_imp_choice.upper()

                        if d_imp_choice == "A":
                            print(dist_value,"km is",round(km_to_mi(dist_value),3),"mi")
                        elif d_imp_choice == "B":
                            print(dist_value,"mi is",round(mi_to_km(dist_value),3),"km")
                        elif d_imp_choice == "C":
                            print(dist_value,"cm is",round(cm_to_ft(dist_value),3),"ft")
                        elif d_imp_choice == "D":
                            print(dist_value,"ft is",round(ft_to_cm(dist_value),3),"cm")
                        elif d_imp_choice == "E":
                            print(dist_value, "m is",round(m_to_yds(dist_value),3),"yds")
                        elif d_imp_choice == "F":
                            print(dist_value,"yds is",round(yds_to_m(dist_value),3),"m")

                except InvalidOperation:
                    print("Invalid value, please enter a number.")

            elif unit_choice == "B":
                print("- AREA -")
                print("A: mm^2 to cm^2")
                print("B: cm^2 to m^2")
                print("C: m^2 to km^2")
                print("D: km^2 to m^2")
                print("E: m^2 to cm^2")
                print("F: cm^2 to mm^2")
                print("G: Metric-Imperial conversion")

                try:

                    area_value = input("Please enter area: ")
                    area_value = area_value.upper()
                    area_value = constant_memory if area_value == "MEMORY" else Decimal(area_value)
                    
                    area_choice = input("Please enter conversion: ")
                    area_choice = area_choice.upper()

                    if area_choice == "A":
                        print(area_value,"mm^2 is",round(mm2_to_cm2(area_value),3),"cm^2")
                    elif area_choice == "B":
                        print(area_value,"cm^2 is",round(cm2_to_m2(area_value),3),"m^2")
                    elif area_choice == "C":
                        print(area_value,"m^2 is",round(m2_to_km2(area_value),3),"km^2")
                    elif area_choice == "D":
                        print(area_value,"km^2 is",round(km2_to_m2(area_value),3),"m^2")
                    elif area_choice == "E":
                        print(area_value,"m^2 is",round(m2_to_cm2(area_value),3),"cm^2")
                    elif area_choice == "F":
                        print(area_value,"cm^2 is",round(cm2_to_mm2(area_value),3),"mm^2")
                    elif area_choice == "G":
                        print("- METRIC-IMPERIAL AREA CONVERSION -")
                        print("A: km^2 to ha")
                        print("B: ha to km^2")
                        print("C: m^2 to ac")
                        print("D: ac to m^2")

                        a_imp_choice = input("Please enter conversion: ")
                        a_imp_choice = a_imp_choice.upper()

                        if a_imp_choice == "A":
                            print(area_value,"km^2 is",round(km2_to_ha(area_value),3),"ha")
                        elif a_imp_choice == "B":
                            print(area_value,"ha is", round(ha_to_km2(area_value),3),"ha")
                        elif a_imp_choice == "C":
                            print(area_value,"m^2 is",round(m2_to_ac(area_value),3),"ac")
                        elif a_imp_choice == "D":
                            print(area_value,"ac is",round(ac_to_m2(area_value),3),"m^2")

                except InvalidOperation:
                    print("Invalid value, please enter a number.")

            elif unit_choice == "C":
                print("- VOLUME -")
                print("NOTE - 1 ml = 1 cm^3")
                print("A: mm^3 to l")
                print("B: l to m^3")
                print("C: m^3 to ml")
                print("D: ml to m^3")
                print("E: l to ml")
                print("F: ml to l")
                print("G: Metric-Imperial conversion")

                try:

                    volume_value = input("Please enter volume: ")
                    volume_value = volume_value.upper()
                    volume_value = constant_memory if volume_value == "MEMORY" else Decimal(volume_value)
                    
                    volume_choice = input("Please enter conversion: ")
                    volume_choice = volume_choice.upper()

                    if volume_choice == "A":
                        print(volume_value,"mm^3 is",round(mm3_to_l(volume_value),3),"l")
                    elif volume_choice == "B":
                        print(volume_value,"l is",round(l_to_m3(volume_value),3),"m^3")
                    elif volume_choice == "C":
                        print(volume_value,"m^3 is", round(m3_to_ml(volume_value),3),"ml")
                    elif volume_choice == "D":
                        print(volume_value,"ml is",round(ml_to_m3(volume_value),3),"m^3")
                    elif volume_choice == "E":
                        print(volume_value,"l is", round(l_to_ml(volume_value),3),"ml")
                    elif volume_choice == "F":
                        print(volume_value,"ml is",round(ml_to_l(volume_value),3),"l")
                    elif volume_choice == "G":
                        print("- METRIC-IMPERIAL VOLUME CONVERSION - ")
                        print("A: fl oz to ml")
                        print("B: ml to fl oz")
                        print("C: gal to l")
                        print("D: l to gal")

                        v_imp_choice = input("Please enter conversion: ")
                        v_imp_choice = v_imp_choice.upper()

                        if v_imp_choice == "A":
                            print(volume_value,"fl oz is",round(fl_oz_to_ml(volume_value),3),"ml")
                        elif v_imp_choice == "B":
                            print(volume_value,"ml is",round(ml_to_fl_oz(volume_value),3),"fl oz")
                        elif v_imp_choice == "C":
                            print(volume_value,"gal is",round(gal_to_l(volume_value),3),"l")
                        elif v_imp_choice == "D":
                            print(volume_value,"l is",round(l_to_gal(volume_value),3),"gal")

                except InvalidOperation:
                    print("Invalid value, please enter a number.")

            elif unit_choice == "D":
                print("- MASS -")
                print("A: mg to g")
                print("B: g to kg")
                print("C: kg to t")
                print("D: t to kg")
                print("E: kg to g")
                print("F: g to mg")
                print("G: Metric-Imperial conversion")

                try:

                    mass_value = input("Please enter mass: ")
                    mass_value = mass_value.upper()
                    mass_value = constant_memory if mass_value == "MEMORY" else Decimal(mass_value)
                    
                    mass_choice = input("Please enter conversion: ")
                    mass_choice = mass_choice.upper()

                    if mass_choice == "A":
                        print(mass_value,"mg is",round(mg_to_g(mass_value),3),"g")
                    elif mass_choice == "B":
                        print(mass_value,"g is",round(g_to_kg(mass_value),3),"kg")
                    elif mass_choice == "C":
                        print(mass_value,"kg is",round(kg_to_t(mass_value),3),"t")
                    elif mass_choice == "D":
                        print(mass_value,"t is",round(t_to_kg(mass_value),3),"kg")
                    elif mass_choice == "E":
                        print(mass_value,"kg is",round(kg_to_g(mass_value),3),"g")
                    elif mass_choice == "F":
                        print(mass_value,"g is",round(g_to_mg(mass_value),3),"mg")
                    elif mass_choice == "G":
                        print("- METRIC-IMPERIAL MASS CONVERSION -")
                        print("A: kg to lbs")
                        print("B: lbs to kg")
                        print("C: kg to st")
                        print("D: st to kg")
                        print("E: g to oz")
                        print("F: oz to g")

                        m_imp_choice = input("Please enter conversion: ")
                        m_imp_choice = m_imp_choice.upper()

                        if m_imp_choice == "A":
                            print(mass_value,"kg is",round(kg_to_lbs(mass_value),3),"lbs")
                        elif m_imp_choice == "B":
                            print(mass_value,"lbs is",round(lbs_to_kg(mass_value),3),"kg")
                        elif m_imp_choice == "C":
                            print(mass_value,"kg is",round(kg_to_st(mass_value),3),"st")
                        elif m_imp_choice == "D":
                            print(mass_value,"st is",round(st_to_kg(mass_value),3),"kg")
                        elif m_imp_choice == "E":
                            print(mass_value,"g is",round(g_to_oz(mass_value),3),"oz")
                        elif m_imp_choice == "F":
                            print(mass_value,"oz is",round(oz_to_g(mass_value),3),"g")

                except InvalidOperation:
                    print("Invalid value, please enter number.")

            else:
                print("Invalid option, please try again.")


        except ValueError:
                print("Invalid value. Please enter a number.")
                            
                                 

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


            
                
    
            
            
                        

        
