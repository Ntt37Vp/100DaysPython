# Error Handling
# Python Error examples:
# KeyError, IndexError, TypeError, ValueError, ZeroDivisionError
# and more!

# TRY
# EXCEPT
# ELSE
# FINALLY

# FileNotFound example
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["keyyy"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("lorem ipsum dolor")
except KeyError as error_message:
    print(error_message)
else:  # "what else do you need?" Only runs if try block is all true with no errors
    content = file.read()
    print(content)
finally:  # not required
    file.close()
    print("File was closed.")


# use RAISE to raise your own error
# example

# use PASS to skip a loop
