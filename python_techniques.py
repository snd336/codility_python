from itertools import count
from random import sample


# Find an item in list fast
# Memory efficient (optimization) iterations via generators
def list_comprehension():
    # Must go through entire collection
    return [item for item in range(1, 10000) if (item % 42 == 0) and (item % 43 == 0)][0]


# Count() is a memory efficient infinite sequence generator
def generator_combined_with_next():
    # Generator via the count function
    # Stops after each next call and then resumes where left off
    return next(item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))


def generator_3_items():
    # Suspend and resume action of next()
    # Similar efficiency as a for_loop
    # Use for loop for added complexity
    # Use generator for simple filtering
    gen = (item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))
    return [next(gen), next(gen), next(gen)]


def yield_usage():
    # Use yield in a generator function
    # Saves state and sends back the yield value
    # When called again, code after yield executes and then loop begins again until next yield
    # Return leaves the function and doesnt come back
    pass

# sorting
# List of 1 000 000 integers randomly shuffled
MILLION_RANDOM_NUMBERS = sample(range(1_000_000), 1_000_000)


def test_sort():
    random_list = MILLION_RANDOM_NUMBERS[:]
    # Only works lists
    # Modifies list in place
    return random_list.sort()


def test_sorted():
    random_list = MILLION_RANDOM_NUMBERS[:]
    # Creates a new list - takes longer than sort due to creating new list time
    # Can be used with any iterable
    return sorted(random_list)

# company_dicts = (dict(zip(cols, data)) for data in list_line)