import os
import json

def delete_file_if_exists(file_path):
    """Deletes a file if it exists."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error: {e}")

def create_file_if_not_exists(file_path):
    """Creates a file if it does not exist."""
    with open(file_path, 'a'):
        os.utime(file_path, None)  # Update the access and modification times
    print(f"File '{file_path}' ensured to exist.")


def append_to_json_file(file_path, new_data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Ensure the file contains a list to append to
    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list to append data to.")

    # Step 3: Append the new data
    data.append(new_data)

    # Step 4: Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)