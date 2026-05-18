import os

# Specify the directory path
path = "/Fortune cloud"

# Get and print directory contents
contents = os.listdir(path)

print("Directory contents:")
for item in contents:
    print(item)