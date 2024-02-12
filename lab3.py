#!/usr/bin/env python3
def write_name_to_file(name):
    try:
        with open('akash_dahal.txt', 'w') as file:
            file.write(name)
        print("File 'akash_dahal.txt' created successfully.")
    except Exception as e:
        print("Error:", e)

write_name_to_file("My name is Akash Dahal.")
