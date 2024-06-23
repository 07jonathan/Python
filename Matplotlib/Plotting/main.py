import matplotlib.pyplot as plt
import numpy as np

# Data points
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Plotting
plt.plot(xpoints, ypoints)
plt.title('Contoh 1: Menggambar garis dari (1, 3) ke (8, 10)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data points
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Plotting with markers only
plt.plot(xpoints, ypoints, 'o')
plt.title('Contoh 2: Menggambar titik-titik pada posisi (1, 3) dan (8, 10)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# Plotting
plt.plot(xpoints, ypoints)
plt.title('Contoh 3: Menggambar garis melalui (1, 3), (2, 8), (6, 1), dan (8, 10)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Data points
ypoints = np.array([3, 8, 1, 10, 5, 7])

# Plotting
plt.plot(ypoints)
plt.title('Contoh 4: Menggambar titik-titik dengan sumbu x default')
plt.xlabel('Index')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
