def my_function(x, /):
  print(x)

my_function(3)
# my_function(x = 3) will raise error


# without positional argument
def my_function2(x):
  print(x)

my_function2(x = 3)