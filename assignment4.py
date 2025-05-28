# Step 1: Create and write to a new file
with open("sample.txt", "w") as file:
    file.write("This is the first line in the file.\n")
    file.write("This is the second line.\n")
print("Initial content written to sample.txt")

# Step 2: Append more content to the same file
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("Another appended line.\n")
print("Additional content appended to sample.txt")

# Step 3: Read and display the content of the file
print("\nReading contents of sample.txt:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
