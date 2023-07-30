def user_input()
     user_input = input("Please enter a positive integer N: ")

     # Initialize an empty list to store the N numbers
     input_list = []

     # Ask the user to provide N numbers (one by one) and read all of them
     for i in range(user_input):
          num = input(f"Please enter number {i+1}: ")
          input_list.append(num)

     # Ask the user for input X (integer)
     X = input("Please enter an integer X: ")

     # Check if X is in the list of numbers and output the appropriate response
     if X in input_list:
           print("Index of X in the input list: ", input_list.index(X) + 1)
     else:
           print("-1")
