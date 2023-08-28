# Python "timeit" module

<p align="center">
  <img src="https://github.com/ArkadiiOlshevskyi/python_timeit/blob/main/img/arkadii_olshevsky_python_developer_timeit.png" alt="Python timeit module" style="max-width:200%;">
</p>


When it comes to measuring the speed of your Python code, the `timeit` module is your go-to tool. This module provides a simple and effective way to gauge how fast or slow your code executes. Inside this repository, you'll find four examples that demonstrate its usage:

1. **Simple Function**: Measure the execution time of a basic function.
2. **Iterating Class Properties**: Evaluate the performance of a function that iterates through class properties.
3. **Random**: See how the `random` function performs.
4. **Randint (Random Module)**: Explore the speed of the `randint` function from the `random` module.

## Usage

The `timeit` module offers several options to fine-tune your timing measurements:

- `stmt`: This is where you provide the code snippet you want to time.
- `setup`: Use this to set up any necessary imports or initializations for your code.
- `number`: Determine how many times you want your code to run for timing.
- `repeat`: Specify how many times you want to repeat the timing process for more accuracy.

Here's an example of how to use the `timeit` module:

```python
import timeit

# Define your code snippet
code_snippet = "your_code_here"

# Set up any necessary imports or initializations
setup_code = "import your_module_here"

# Measure the execution time
time_taken = timeit.timeit(stmt=code_snippet, setup=setup_code, number=10000)

print(f"Time taken: {time_taken:.6f} seconds")
