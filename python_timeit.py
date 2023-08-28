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
