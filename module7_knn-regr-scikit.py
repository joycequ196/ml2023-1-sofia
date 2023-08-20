import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Read N and k
N = int(input("Enter the N value (positive integer): "))
k = int(input("Enter the k value (positive integer): "))

if k < 0 :
    print("k should be positive integer")
    k = int(input("Enter the k value (positive integer): "))
if N < 0 :
    print("N should be positive integer")
    N = int(input("Enter the N value (positive integer): "))
if k > N:
    print("k should be less than or equal to N")
    N = int(input("Enter the N value (positive integer): "))
    k = int(input("Enter the k value (positive integer): "))
    
# Read N (x, y) points
x_val= []
y_val = []

for i in range(N):
    x = float(input(f"Enter the x value for point {i + 1}: "))
    y = float(input(f"Enter the y value for point {i + 1}: "))
    x_val.append(x)
    y_val.append(y)
        
class KNN:
    def __init__(self, k, x_val,y_val):
        self.k = k
        self.x_val = np.array(x_val).reshape(-1, 1)
        self.y_val = np.array(y_val)

    def predict(self,X):

        # Create k-NN Regressor
        knn = KNeighborsRegressor(n_neighbors=k)

        # Fit the model
        knn.fit(self.x_val, self.y_val)

        # Call for input X
        X_input = np.array([[X]])

        # Predict Y
        Y_pred = knn.predict(X_input)

        return np.mean(Y_pred)



# Initialize KNN object
knn = KNN(k,x_val,y_val)

# Read value for X and compute Y
X = float(input("Enter the input X: "))

#Print the result
result = knn.predict(X)
print(f"The result of {k}-NN Regression is: {result}")
