# Python Calculator

A command-line calculator built with Python, featuring arithmetic operations, advanced mathematical functions, geometry calculations, unit conversions, statistical tools, and constant storage.

The project began as a personal calculator and has since been progressively refactored to improve code organisation, numerical accuracy, input validation, and maintainability.

## Features

### Basic Arithmetic
- Addition, subtraction, multiplication, and division.
- Exponentiation.

### Advanced Mathematics
- Surds and nth-root calculations.
- Logarithms with user-defined bases.
- Quadratic equation solver, including real and complex roots.
- Factorial calculations.
- Permutations.

### Geometry

**2D Area Calculations**
- Rectangle and parallelogram.
- Triangle.
- Circle.
- Trapezium.

**3D Volume Calculations**
- Cuboid.
- Cylinder.
- Triangular prism.
- Sphere.
- Rectangular pyramid.
- Regular tetrahedron.
- Cone.

**3D Surface Area Calculations**
- Cuboid.
- Cylinder.
- Triangular prism.
- Sphere.
- Rectangular pyramid.
- Regular tetrahedron.
- Cone.

### Unit Conversion
Convert between compatible units across four categories:
- Length.
- Area.
- Volume.
- Mass.

Conversions are performed using base-unit conversion factors to maintain consistency and prevent conversions between incompatible measurement categories.

### Statistics
- Mean.
- Median.
- Mode.
- Range.
- Interquartile range (IQR).

### Constant Storage
- Mathematical constants, including π, e, the golden ratio, and τ.
- Scientific constants, including Avogadro's constant, the speed of light, the gravitational constant, and Planck's constant.
- User-defined constants.
- Stored values can be retrieved during subsequent calculations using `MEMORY`.

## Installation and Setup

### Prerequisites
- Python 3.8 or later.
- Git (if cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/calculator.git
cd calculator
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Run the calculator

```bash
python calculator.py
```

On some systems, you may need to use:

```bash
python3 calculator.py
```

No external packages or installations are required. The calculator uses Python's standard library.

## Built With

- **Python 3.11** – Primary programming language.
- **`decimal`** – Decimal arithmetic with configurable precision.
- **`math`** – Mathematical functions and operations.
- **`cmath`** – Complex-number calculations, including imaginary roots.
- **`statistics`** – Statistical calculations.

## Technical Notes

- Decimal arithmetic is used for many calculations to reduce the floating-point representation issues associated with binary floating-point numbers.
- Numerical precision is configured globally, with a default display precision of three decimal places for selected calculations.
- Unit conversions use category-specific factors and a common base unit.
- Calculation functions are progressively separated from menu and output handling to improve modularity and maintainability.

## Project Status

This project is actively being refactored. Existing functionality is being preserved while individual components are improved, tested, and reorganised.

Planned improvements include more comprehensive input validation, consistent output formatting, expanded testing, and further code-quality improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
