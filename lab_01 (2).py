import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def Plot2D():
    def func_y(x):
        return 3 * np.cos(2 * x) ** 2 * np.sin(5 * x)

    def func_z(x):
        if np.any((x >= 0) & (x < 1)):
            return 2 * np.cos(x) * np.exp(-2 * x)
        else:
            return 2 * np.sin(3 * x)

    X = np.arange(-10, 10, 0.01)
    y = func_y(X)
    plt.plot(X, y)
    plt.title(r"$y = 3\cos^2(2x)\sin(5x)$", fontsize=15, y=1.1, pad=-14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    z = func_z(X)
    plt.plot(X, z)
    plt.title(r'$z = 2\cos(x)e^{-2x}, x\in[0, 1], $'
              r"$ 3x^2 + \sqrt{1+x^4}, x<0,  $"
              r"$ 2\sin(3x),  x>1$", fontsize=15, y=1.1, pad=-14)
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.show()


def PlotSurface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(-10, 10, 0.1)
    Y = np.arange(-00, 10, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = X ** 6 - 3 * np.e ** (0.7 * Y) + Y ** 3

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title(r"$z = x^6 - 3e^{0.7y}+y^3$", fontsize=15)
    plt.xlabel("X")
    plt.ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


def PlotPolar():
    ax = plt.subplot(111, projection='polar')

    def paskal_snail(fi):
        l = 0.5
        r = 2
        ro = 2 * r * np.cos(fi) - l
        return ro

    theta = np.linspace(0, 2 * np.pi, 500)
    ro = paskal_snail(theta)
    ax.plot(theta, ro)
    ax.set_rmax(5)
    ax.set_rticks([0, 5])
    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    ax.set_title(r"$ρ = 2r*cos(φ)-l$")
    plt.show()


def PlotSurfaceSecondOrder():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    a, b = 15, 6
    X = np. arange(-10, 10, 0.25)
    Y = np. arange(-10, 10, 0.25)
    X, Y = np. meshgrid(X, Y)

    Z1 = np.sqrt(1 + np.power(X, 2)/np.power(a, 2) + np.power(Y, 2)/np.power(b, 2))
    Z2 = -np.sqrt(1 + np.power(X, 2)/np.power(a, 2) + np.power(Y, 2)/np.power(b, 2))


    ax.plot_surface(X, Y, Z1, cmap='gist_earth',
                           linewidth=0, antialiased=False)
    ax.plot_surface(X, Y, Z2, cmap='gist_earth',
                           linewidth=0, antialiased=False)

    ax.set_title(r"$ \frac{x^2}{a^2} -\frac{y^2}{b^2}=1 $", fontsize=25)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    ax.view_init(elev=30, azim=-45)

    plt.show()


def PlotBarCart():
    germany = [29, 51, 59, 478, 93, 244, 420, 510, 575, 625]
    france = [28, 46, 57, 52, 63, 93, 190, 275, 310, 355]
    uk = [53, 73, 84, 105, 130, 180, 245, 265, 300, 335]
    ussr = [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    fig, ax1 = plt.subplots(figsize=(12, 6))
    bar_width = 0.15
    index = range(len(years))
    ax1.bar(index, germany, bar_width, label='Германія', color="red")
    ax1.bar([i + bar_width for i in index], france, bar_width, label='Франція')
    ax1.bar([i + 2 * bar_width for i in index], uk, bar_width, label='Великобританія')
    ax1.bar([i + 3 * bar_width for i in index], ussr, bar_width, label='СРСР')

    ax1.set_xlabel('Рік', fontsize=15)
    ax1.set_ylabel('млрд. дол', fontsize=15)
    ax1.set_xticks([i + 1.5 * bar_width for i in index])
    ax1.set_xticklabels(years, rotation=45, ha='right')
    ax1.set_title("Промислове виробництво, додана вартість (млрд. дол)")
    ax1.legend()

    plt.tight_layout()
    plt.show()


def Plot3DChart():
    fig = plt.figure()
    ax1 = plt.axes(projection="3d")

    countries = [" ", " ","Германія", " ", "Франція", " ", "Великобританія", " ", "СРСР"]
    data = np.array([[29, 51, 59, 478, 93, 244, 420, 510, 575, 625],
                     [28, 46, 57, 52, 63, 93, 190, 275, 310, 355],
                     [53, 73, 84, 105, 130, 180, 245, 265, 300, 335],
                     [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]])
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970,  1980, 1990, 2000]
    cols = 10
    rows = 4

    xpos = np.arange(0, 10, 1)
    ypos = np.arange(0, 4, 1)
    xpos, ypos = np.meshgrid(xpos + 0.5, ypos + 0.5)

    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(cols * rows)

    dx = np.ones(rows * cols) * 0.5
    dy = np.ones(cols * rows) * 0.5
    dz = data.flatten()

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color="green")

    index = np.arange(10)
    ax1.set_xticks(index + 8 / 9)
    ax1.set_xticklabels(years, fontsize=7)
    ax1.set_yticklabels(countries)
    ax1.set_xlabel('Роки')
    ax1.set_zlabel('млрд. дол')
    plt.show()


def main():
    Plot2D()
    PlotSurface()
    PlotPolar()
    PlotSurfaceSecondOrder()
    PlotBarCart()
    Plot3DChart()


if __name__ == "__main__":
    main()
