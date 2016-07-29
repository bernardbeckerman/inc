import numpy as np
from matplotlib import pyplot as plt
def vonmises_KDE(data, kappa, length, plot=None):

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
    x_data = np.linspace(-2*np.pi, 2*np.pi, length, endpoint=False)

    kernels = []

    for d in data:

        # Make the basis function as a von mises PDF
        kernel = vonmises(kappa, loc=d)
        kernel = kernel.pdf(x_data)
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

baz = np.array([179,100,-170])   
kappa = 12
x_data, vonmises_kde, f = vonmises_KDE(baz, kappa, 200, plot=0)
f = open('prd_vm.dat','w')
for i in range(0,200):
    xc = (i-100.0)*np.pi/50.0
    if xc < 0:
        f.write(str(xc)+' '+str(vonmises_kde[i]+vonmises_kde[i+100]) + '\n')
    else:
        f.write(str(xc)+' '+str(vonmises_kde[i]+vonmises_kde[i-100]) + '\n')
f.close()
plt.show()
