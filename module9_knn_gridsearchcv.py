# Read N and initialize training set
N = int(input("Enter the number of training samples (N): "))
X_train = []
Y_train = []

# Ensure N is positive
if N <= 0:
    print("N should be a positive integer.")
    N = int(input("Please enter the number of points (N): "))

# Read training samples
for i in range(N):
    x = float(input(f"Enter x value for training sample {i+1}: "))
    y = int(input(f"Enter y value for training sample {i+1}: "))
    X_train.append(x)
    Y_train.append(y)

# Convert lists to Numpy arrays and reshape X_train
X_train = np.array(X_train).reshape(-1, 1)
Y_train = np.array(Y_train)

# Read M and initialize test set
M = int(input("Enter the number of test samples (M): "))
X_test = []
Y_test = []

# Read test samples
for i in range(M):
    x = float(input(f"Enter x value for test sample {i+1}: "))
    y = int(input(f"Enter y value for test sample {i+1}: "))
    X_test.append(x)
    Y_test.append(y)

# Convert lists to Numpy arrays and reshape X_test
X_test = np.array(X_test).reshape(-1, 1)
Y_test = np.array(Y_test)

# Initialize variables to keep track of the best k and corresponding accuracy
best_k = 0
best_accuracy = 0.0

# Loop through k values from 1 to 10
# N + 1 because range is exclusive at the upper limit
for k in range(1, min(11, N + 1)):  
    print(f"Training for k = {k}")
    
    # Initialize kNN classifier
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Train the classifier
    knn.fit(X_train, Y_train)
    
    # Make predictions on the test set
    Y_pred = knn.predict(X_test)
    
    # Calculate accuracy
    acc = accuracy_score(Y_test, Y_pred)
    
    print(f"Accuracy for k={k}: {acc}")
    
    # Update best k and corresponding accuracy
    if acc > best_accuracy:
        best_k = k
        best_accuracy = acc

# Output the best k and corresponding accuracy
print(f"The best k for the kNN Classification method is {best_k} with an accuracy of {best_accuracy}")
