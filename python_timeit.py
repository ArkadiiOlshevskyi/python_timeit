import timeit
import random
import time
# import profile    # for advanced code examples


# Example 1 - small function
code_snippet = "[x**10 for x in range (100)]"
time_taken = timeit.timeit(code_snippet, number=100)
print(f"Time for small function: {time_taken:.6f} seconds")


# Example 2 - function
code_snippet_2 = """
def show_products(data):
    filtered_products = []

    for product in data:
        # Execute products with empty cost or description values:
        if product.cost is not None and product.description:
            product_view_model = ProductViewModel(product.id, product.name, product.cost)
            filtered_products.append(product_view_model)

    # Sort the list of ProductViewModel objects based on cost
    sorted_products = sorted(filtered_products, key=lambda product: product.cost)   # here you can change for product.id | cost | name ...
    for product in sorted_products:
        print(f"ID: {product.id}, Name: {product.name}, Cost: ${product.cost}")
"""
time_taken_2 = timeit.timeit(code_snippet_2, number=1)
print(f"Time for function: {time_taken_2:.5f} seconds")

# Example 3 - Testing random function
randit_time: float = timeit.timeit(stmt='random.randint(0, 1)',
                                   setup='import random',
                                   timer=time.perf_counter,
                                   number=1)

print(f"Time for randit: {randit_time}.6f seconds")

random_time_2 = timeit.repeat(stmt='random.random()',
                              setup='import random',
                              repeat=2,
                              number=1)

print(f"Time for random: {random_time_2}.6f seconds")


# Example with two text iterators:

code_snippet_3 = '''
def alphabet_position(text):
    alphabet_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }

    position_list = []

    for char in text.lower():
        if char in alphabet_dict:
            position_list.append(str(alphabet_dict[char]))

    return ' '.join(position_list)

'''
code_snippet_4 = '''
def alphabet_position_2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
'''

setup = "text = 'The quick brown fox jumps over the lazy dog.'"

time_measure_1 = timeit.timeit(stmt='alphabet_position(text)', setup=code_snippet_3 + setup, number=1)
time_measure_2 = timeit.timeit(stmt='alphabet_position_2(text)', setup=code_snippet_4 + setup, number=1)

print(f"Time for random: {time_measure_1}.6f seconds")
print(f"Time for random: {time_measure_2}.6f seconds")
