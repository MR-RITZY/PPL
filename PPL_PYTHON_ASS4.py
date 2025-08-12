def modify_content(content):
    """
    Modify the file content.
    For this example, we'll convert all text to uppercase.
    """
    return content.upper()


# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Read the original file
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Create new filename
    new_filename = "modified_" + filename

    # Write the modified content to the new file
    with open(new_filename, "w", encoding="utf-8") as file:
        file.write(modified_content)

    print(f"Modified content written to '{new_filename}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
