def convert_ascii_to_char(filename):
    try:
        with open(filename, 'r') as file:
            ascii_numbers = file.readlines()
            characters = [chr(int(num.strip())) for num in ascii_numbers]
            print(''.join(characters))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid number in file. Each line should contain a valid ASCII number.")

# Example usage: replace 'input.txt' with your file name
convert_ascii_to_char('input.txt')
