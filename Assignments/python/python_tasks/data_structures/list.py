# Accept user input to create a list of integers and compute the sum
int_list = input("Enter integers separated by spaces: ").split()
int_list = [int(x) for x in int_list]
print(f"Sum of the integers: {sum(int_list)}")
