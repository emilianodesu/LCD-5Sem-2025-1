import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# Generando nuestros datos
X, y = make_moons( n_samples = 1000 , noise = 0.3 , random_state=100)

#print(X)
#print(y)

# Hacioendo la division de nuestros datois entre los de entrenamiento y prueba :o
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Vamos a graficar para ver si es cierto o es puro choro
plt.figure(figsize=(10,5))
plt.scatter(X_train[y_train == 0][:,0], X_train[y_train == 0][:,1],
            color='skyblue', label='Clase 0 - Entrenamiento ', alpha = 0.4)
plt.scatter(X_train[y_train == 1][:,0], X_train[y_train == 1][:,1],
            color='salmon', label='Clase 1 - Entrenamiento ' , alpha = 0.4)
plt.scatter(X_test[y_test == 0][:,0], X_test[y_test == 0][:,1],
            color='skyblue', label='Clase 0 - Testing ' , marker='x')
plt.scatter(X_test[y_test == 1][:,0], X_test[y_test == 1][:,1],
            color='salmon', label='Clase 1 - Testing ',  marker='x')
plt.xlabel(' Característica 1 ')
plt.xlabel(' Característica 2 ')
plt.title('Tamaulipas')
plt.legend()
plt.show()

# ===================== Definiendo nuestro modelito ================
model = Sequential()
model.add(Dense( 10, input_shape=(2,) , activation='relu')) # Esta es la primer capa >:D
model.add(Dense( 8, activation='relu')) # Segunda capa
model.add(Dense( 1, activation='sigmoid')) # Output layer

# ==================== Compilando nuestro modelitop ===============
model.compile( optimizer=Adam(learning_rate=0.01) , loss='binary_crossentropy')


# ====================== Entrenando la mamastrosa =================
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# ====================== Evaluando nuestro modelillo :o ========================
y_pred = (model.predict(X_test > 0.5)).astype("int32")
accuracy = accuracy_score(y_test, y_pred)

print(f"La exactitud en nuestro conjunto de prueba es: {accuracy:.2f}")
