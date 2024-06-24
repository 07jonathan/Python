# Import library yang diperlukan
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset (pastikan file data.csv berada di direktori yang sama dengan script ini)
df = pd.read_csv("data.csv")

# Definisikan independent variables (X) dan dependent variable (y)
X = df[['Weight', 'Volume']]  # Weight dan Volume sebagai independent variables
y = df['CO2']  # CO2 sebagai dependent variable

# Buat objek LinearRegression
regr = LinearRegression()

# Training model menggunakan data
regr.fit(X, y)

# Lakukan prediksi untuk kasus baru
# Misalnya, prediksi CO2 untuk mobil dengan weight 2300 kg dan volume 1300 cm^3
predictedCO2 = regr.predict([[2300, 1300]])

# Print hasil prediksi
print("Predicted CO2 emission:", predictedCO2)
