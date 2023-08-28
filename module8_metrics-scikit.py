import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask the user for input N
N = int(input("Please enter the number of points (N): "))

# Ensure N is positive
if N <= 0:
    print("N should be positive integer")
    N= int(input("Please enter the number of points (N): "))
    
# Initialization
prediction = np.zeros(N, dtype=int)
ground_truth = np.zeros(N, dtype=int)


# Get input points from the user
for i in range(N):
    x = int(input(f"Please enter ground truth (x value) for point {i+1}, the value should be either 0 or 1: "))
    y = int(input(f"Please enter predicted value (y value) for point {i+1}, the value should be either 0 or 1: "))
    
    # Ensure x and y are either 0 or 1
    if x not in [0, 1] or y not in [0, 1]:
        print("Both x and y should be either 0 or 1.")
        exit()
    
    ground_truth[i] = x
    prediction[i] = y

# Compute Precision and Recall using Scikit-learn
precision = precision_score(ground_truth, prediction)
recall = recall_score(ground_truth, prediction)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
