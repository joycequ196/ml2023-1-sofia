import numpy as np

# Read N and k
N = int(input("Enter the N value (positive integer): "))
if N < 0 :
    print("N should be positive integer")
    N = int(input("Enter the N value (positive integer): "))
  
k = int(input("Enter the k value (positive integer): "))
if k < 0 :
    print("k should be positive integer")
    k = int(input("Enter the k value (positive integer): "))

if k > N:
    print("k should be less than or equal to N")
    N = int(input("Enter the N value (positive integer): "))
    k = int(input("Enter the k value (positive integer): "))
        
class KNN:
    def __init__(self, k, points):
        self.k = k
        self.points = points

    def predict(self, x):
    
        # Compute the Euclidean distance for each point
        distances = np.sqrt(np.sum((self.points[:, :1] - x) ** 2, axis=1))

        # Get the indices of the k smallest distances
        indices = np.argsort(distances)[:k]

        # Include all points that distances equal to the k-th smallest distance
        kth_distance = distances[indices[-1]]
        all_indices_with_kth_distance = np.where(distances == kth_distance)[0]

        # Gather non duplicate indices for all filtered points
        final_indices = np.unique(np.concatenate((indices, all_indices_with_kth_distance)))
        
        # Compute the mean of the corresponding y-values
        yvalues = self.points[final_indices, 1]

        return np.mean(yvalues)


# Read N (x, y) points
points = []
for i in range(N):
    x = float(input(f"Enter the x value for point {i + 1}: "))
    y = float(input(f"Enter the y value for point {i + 1}: "))
    points.append((x, y))

points = np.array(points)

# Initialize KNN object
knn = KNN(k, points)

# Read value for X and compute Y
X = float(input("Enter the input X: "))

#Print the result
result = knn.predict(X)
print(f"The result of {k}-NN Regression is: {result}")
