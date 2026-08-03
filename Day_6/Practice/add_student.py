def add():

  print("=== Welcome to the add student function! ===\n")
  name = input("Please enter the student's name: ".strip())
  
  while True:
    try:
      # age parameter is converted to int to ensure it's a valid integer
      age = int(input("Please enter the student's age: "))
      return {"name": name, "age": age}
    except ValueError:
      print("\nInvalid input for age. Please enter a valid integer.\n")
