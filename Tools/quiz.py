# a) Outer ZeroDivisionError exception caught
# b) Error: You divided by zero!
# c) Error: You divided by zero!
#          Finally executed
# d) Finally executed
# e) None of the above

try:
    for i in range(3):
        try:
            1 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("Error: You divided by zero!")
        finally:
            print("Finally executed.")
            break
except ZeroDivisionError:
    print("Outer ZeroDivisionError exception caught")
