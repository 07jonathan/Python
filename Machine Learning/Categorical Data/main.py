import pandas as pd
from sklearn.linear_model import LinearRegression

# Membaca data dari file CSV
cars = pd.read_csv('data.csv')

# Melakukan One Hot Encoding pada kolom 'Car'
ohe_cars = pd.get_dummies(cars[['Car']])

# Menggabungkan variabel independen (X) dan variabel dependen (y)
X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

# Inisialisasi model regresi linear
regr = LinearRegression()

# Melatih model dengan data X dan y
regr.fit(X, y)

# Membuat prediksi CO2 untuk mobil Volvo dengan Volume 1300 dan Weight 2300
predictedCO2 = regr.predict([[1300, 2300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
print("Predicted CO2 emission:", predictedCO2)
