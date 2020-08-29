import numpy as np
from pylab import *
from matplotlib import pyplot as plt
from matplotlib import animation, rc
import time

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
plt.style.use('classic')

"""
-----------------------------------------------------------
Defining varibles for now, want to change these...
-----------------------------------------------------------
"""
"""
N = 10
a = 0.235e-9                   #Interatomc distance
#L = N*a                       #sample length

m = 4.6637066e-26              #Mass silicon
C =  10e2                      #Force constant
w_0 = sqrt(4*C/m)              #Constant.

#constant defining u_0
hbar = 1.0545718e10-34         #planck constant
rho  = 1                       #mas density
V    = sqrt(C/m)*a             #volume m^3
"""

N = 10
a = 1                         #Interatomc distance
#L = N*a                      #sample length

m = 1                         #Mass silicon
C =  1                        #Force constant
w_0 = 1                       #Constant.

#constant defining u_0
hbar = 1                     #planck constant
rho  = 1                     #mas density
V    = 1                     #volume m^3

"""
-----------------------------------------------------------
Creating class Phonons_Oscillations
-----------------------------------------------------------
"""

class Phonons_Oscillations:

    """
    -----------------------------------------------------------
    """
    #Serve the class function which is used.

    def K_values(self):
        K_list = []

        for i in range(-N, N+1):
            K_list.append(2*np.pi/(N*a) * i/2) #Creating discrete modes.

        K = np.array(K_list)

        return K

    def dispersion_relation(self,K):
        return w_0 * abs(np.sin(1./2. * K *a))

    def u(self, N, K,w,i):
        #Amplitude of displacement - apply when working.
        #u_0  = np.sqrt(4*(1 + n)*hbar/(rho*V*w))
        return np.cos(K*N)*np.cos(w*i)

    """
    -----------------------------------------------------------
    """

"""
Starting to create an animation of atomic displacement.
"""

#Animation goes here. append information from class regarding the animation.
def Visulation_animation(N, fig, K, w):

    #Establishing the inter-atomic separation.
    Noa = np.zeros(N)
    for i in range(N):
        Noa[i:] += N*a

    fig = plt.figure(fig)

    """
    Need to find a way to generalize the x-lim and ylim
    """
    ax = plt.axes(
    xlim =(min(Noa) - 20, max(Noa) + 20),
    ylim =(-1,1))
    yticks([])
    xticks([])

    particles, = ax.plot([],[],'bo')

    lines = []
    for index in range(1,N+1):
        particles =ax.plot([],[],'bo',color='black', markersize=12)
        lines.append(particles[0])

    def animate(i):

        for j, particles in enumerate(lines):
            # set data for each line separately.
            particles.set_data(Noa[j] + Solution.u(j+1, K, w,i), 0)
            #count += 1
        #print (count )
        return lines

    anim = animation.FuncAnimation(fig, animate, frames=200,
                              interval=50, blit=True)


    anim, Noa

Solution = Phonons_Oscillations()

K = Solution.K_values()
w = Solution.dispersion_relation(K)




#Saving figures here:
for i in range(1, 2*N+1):
    anim = Visulation_animation(N, i, K[i], w[i])
    filename = "/Users/kristoffervarslott/Documents/Website/pages/static/Phonons_%i.mp4"%i
    plt.show()
    #anim.save(filename)
