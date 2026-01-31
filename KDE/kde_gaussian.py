import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def measure(n):
    "Measurement model, return two coupled measurements."
    m1 = np.random.normal(size=n)
    m2 = np.random.normal(scale=0.5, size=n)
    return m1+m2, m1-m2

def main():
    m1, m2 = measure(2000)
    xmin = m1.min()
    xmax = m1.max()
    ymin = m2.min()
    ymax = m2.max()
    # Perform a kernel density estimate on the data:

    # make a 100 x 100 grid
    # smear in x direction and in direction
    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]

    # 2 x 10000
    positions = np.vstack([X.ravel(), Y.ravel()])

    # 2 x 2000 - using original values
    values = np.vstack([m1, m2])

    # form the kernel from the original measurements
    kernel = stats.gaussian_kde(values)

    # reshape to 100 x 100
    # the value of the kerney at the positions
    Z = np.reshape(kernel(positions).T, X.shape)

    # Z is the kernel "Hills"
    # Plot the hills:
    fig, ax = plt.subplots()
    ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,
              extent=[xmin, xmax, ymin, ymax])

    # plot the original points:
    ax.plot(m1, m2, 'k.', markersize=2)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    plt.show()
    #../../_images/scipy-stats-gaussian_kde-1_00_00.png
    # Compare against manual KDE at a point:

    point = [1, 2]
    mean = values.T
    cov = kernel.factor**2 * np.cov(values)
    X = stats.multivariate_normal(cov=cov)
    res = kernel.pdf(point)
    ref = X.pdf(point - mean).sum() / len(mean)
    np.allclose(res, ref)
    True

if __name__ == "__main__":
    main()
