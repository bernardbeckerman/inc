import numpy as np
from matplotlib import pyplot as plt
def vonmises_KDE(data, kappa, plot=None):       

    """    
    Create a kernal densisity estimate of circular data using the von mises 
    distribution as the basis function.

    """

    # imports
    from scipy.stats import vonmises
    from scipy.interpolate import interp1d

    # convert to radians
    data = np.radians(data)

    # set limits for von mises
    vonmises.a = -np.pi
    vonmises.b = np.pi
    x_data = np.linspace(-2*np.pi, 2*np.pi, 200)

    kernels = []

    for d in data:

        # Make the basis function as a von mises PDF
        kernel = vonmises(kappa, loc=d)
        kernel = kernel.pdf(x_data)
        kernels.append(kernel)
        kernels.append(kernel)
        kernels.append(kernel)

        if plot:
            # For plotting
            kernel /= kernel.max()
            kernel *= .2
            plt.plot(x_data, kernel, "grey", alpha=.5)


    vonmises_kde = np.sum(kernels, axis=0)
    vonmises_kde = vonmises_kde / np.trapz(vonmises_kde, x=x_data)
    f = interp1d( x_data, vonmises_kde )


    if plot:
        plt.plot(x_data, vonmises_kde, c='red')  

    return x_data, vonmises_kde, f

baz = np.array([-92.29061004, -85.42607874, -85.42607874, -70.01689348,
               -63.43494882, -63.43494882, -70.01689348, -70.01689348,
               -59.93141718, -63.43494882, -59.93141718, -63.43494882,
               -63.43494882, -63.43494882, -57.52880771, -53.61564818,
               -57.52880771, -63.43494882, -63.43494882, -92.29061004,
               -16.92751306, -99.09027692, -99.09027692, -16.92751306,
               -99.09027692, -16.92751306,  -9.86580694,  -8.74616226,
                -9.86580694,  -8.74616226,  -8.74616226,  -2.20259816,
                -2.20259816,  -2.20259816,  -9.86580694,  -2.20259816,
                -2.48955292,  -2.48955292,  -2.48955292,  -2.48955292,
                 4.96974073,   4.96974073,   4.96974073,   4.96974073,
                -2.48955292,  -2.48955292,  -2.48955292,  -2.48955292,
                -2.48955292,  -9.86580694,  -9.86580694,  -9.86580694,
               -16.92751306, -19.29004622, -19.29004622, -26.56505118,
               -19.29004622, -19.29004622, -19.29004622, -19.29004622,179,])   
kappa = 12
x_data, vonmises_kde, f = vonmises_KDE(baz, kappa, plot=1)
plt.show()
