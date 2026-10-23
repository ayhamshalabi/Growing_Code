*This activity has been created as part of the 42 curriculum by ashalabi.*

# Growing Code

An introductory Python module focusing on fundamental programming structures, control flow, functions, recursion, and strict static type hints.

---

## Description

**Growing Code** serves as the initial foundation in Python programming within the 42 curriculum. Through a progressive series of practical exercises centered around a digital garden theme, core software engineering fundamentals are practiced:

- **ex0 (`ft_hello_garden`)**: Basic program entry point and standard console output.
- **ex1 (`ft_garden_name`)**: Interactive user input handling and string display.
- **ex2 (`ft_plot_area`)**: Numeric input processing and arithmetic area calculations.
- **ex3 (`ft_harvest_total`)**: Repetition logic and running totals using `while` loops.
- **ex4 (`ft_plant_age`)**: Conditional decision making and branching (`if`/`else`).
- **ex5 (`ft_water_reminder`)**: State checking with conditional evaluation.
- **ex6 (`ft_count_harvest_iterative` & `ft_count_harvest_recursive`)**: Comparing iterative loops (`for` / `range`) and functional recursion to solve the same problem.
- **ex7 (`ft_seed_inventory`)**: Multi-argument function design, conditional string formatting, and explicit parameter type hinting.

---

## Instructions

### Requirements
- Python 3.10+
- `flake8` (for PEP 8 compliance)
- `mypy` (for static type analysis)

### Running the Exercises

Each exercise function can be executed individually in Python:

```bash
# Example: Running ex0
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"

# Example: Running ex7 with arguments
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

### Running Linters and Static Type Checking

All code in this repository adheres to PEP 8 standards and passes strict typing checks:

```bash
# Verify PEP 8 standards
flake8 ex*/*.py

# Verify static typing
mypy --strict ex*/*.py
```

---

## Resources

- [Official Python Documentation (3.10+)](https://docs.python.org/3/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Mypy Documentation & Type System Reference](https://mypy.readthedocs.io/)

### AI Usage

In compliance with the 42 AI policy:
- **Linting & Verification**: AI was used to check and identify PEP 8 line-length violations and ensure complete `mypy --strict` compliance.
- **Documentation**: AI assisted in formatting and structuring this `README.md` to adhere to the standardized 42 curriculum documentation guidelines.
- **Implementation**: The core logic, algorithms, and exercises were written and reasoned through as part of the foundational learning process.
