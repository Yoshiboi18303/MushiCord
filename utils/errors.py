# This file will hold all the error ways for our bot.
def type_err(client_name, error_method, correct_type, incorrect_type):
  raise TypeError(f"{client_name} raised an error at {error_method}.\nTypeError: {correct_type} should be the right type, not {incorrect_type}.")