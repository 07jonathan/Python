import matplotlib.pyplot as plt
import numpy as np

def main():
    # Definisikan titik-titik
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    # Plot titik-titik
    plt.plot(xpoints, ypoints)

    # Tampilkan plot
    plt.show()

if __name__ == "__main__":
    main()
