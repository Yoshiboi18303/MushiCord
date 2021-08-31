# This file will hold all the error ways for our bot.
def refer_err(bad_reference):
  raise ReferenceError(f"You didn't define {str(bad_reference)}!")
def type_err(client_name, correct_type, incorrect_type):
  raise TypeError(f"{client_name} raised an error.\nTypeError: {correct_type} should be the right type, not {incorrect_type}.")