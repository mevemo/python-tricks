# format_examples.py

# Old-style string formatting (% operator)

# String substitution
name = "Alice"
print("Hello, %s!" % name)

# Multiple substitutions
age = 25
print("%s is %d years old." % (name, age))

# Dictionary substitutions
data = {'name': 'Bob', 'age': 30}
print("%(name)s is %(age)d years old." % data)

# Formatting numbers
num = 42

# As decimal
print("Number as decimal: %d" % num)

# As float
print("Number as float: %f" % num)

# As octal
print("Number as octal: %o" % num)

# As hexadecimal
print("Number as hexadecimal: %x" % num)

# With padding
print("Number with padding: %4d" % num)

# With precision for float
print("Number with precision: %.2f" % num)

# With thousands separator
print("Number with thousands separator: %,d" % 1234567)

# Formatting dates
from datetime import datetime

now = datetime.now()

print("Current date and time: %s" % now.strftime("%Y-%m-%d %H:%M"))
