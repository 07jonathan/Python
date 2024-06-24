import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Data yang diberikan
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# Gabungkan fitur x dan y ke dalam satu list data
data = list(zip(x, y))

# Visualisasi data
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=classes, cmap='coolwarm', edgecolors='k')
plt.title('Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Class', ticks=[0, 1])
plt.show()

# Fungsi untuk memprediksi dan memvisualisasikan hasil
def predict_and_visualize(k):
    # Inisialisasi model KNN dengan jumlah tetangga (K) yang ditentukan
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(data, classes)

    # Titik data baru yang akan diprediksi
    new_x = 8
    new_y = 21
    new_point = [(new_x, new_y)]

    # Prediksi kelas titik data baru
    prediction = knn.predict(new_point)
    print(f'Predicted class for ({new_x}, {new_y}) with K={k}: {prediction[0]}')

    # Visualisasi hasil prediksi
    plt.figure(figsize=(8, 6))
    plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]], cmap='coolwarm', edgecolors='k')
    plt.title(f'KNN Classification (K={k})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar(label='Class', ticks=[0, 1])
    plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f'New point, class: {prediction[0]}', fontsize=12)
    plt.show()

# Uji dengan K = 1
predict_and_visualize(1)

# Uji dengan K = 5
predict_and_visualize(5)
