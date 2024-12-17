def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))