def generate_alphabetic_triangle(rows):
	# Generate the list of lists containing
	# alphabetic characters for each row
	alphabets = [[chr(65 + j) for j in range(i)] for i in range(1, rows + 1)]
	return alphabets


def print_alphabetic_triangle(alphabets):
	# Print the alphabetic triangle
	# pattern using list comprehension
	for row in alphabets:
		print(' '.join(row))


if __name__ == "__main__":
	num_rows = 5 # Adjust the number of rows as needed

	alphabets_triangle = generate_alphabetic_triangle(num_rows)
	print_alphabetic_triangle(alphabets_triangle)
