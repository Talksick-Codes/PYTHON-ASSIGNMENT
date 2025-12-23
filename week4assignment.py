#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename=input(f"Please Enter File name:")
try:
  with open(filename,"r") as file:
    print(file.read())
except FileNotFoundError:
  print(f"File {filename} not found.")
  

