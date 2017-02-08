# Benzol modul

def benzol(filename):
    import numpy as np
    import matplotlib.pyplot as plt
    #%matplotlib inline
    #with open("benzene.yah.HAM", "r", encoding='int64', errors="ignore") as fid:
    #    fid.seek()
    #    H = fid.read()
    #H.decode()
    #    fid.close()
    #paraméterek
    H = np.zeros((8,8)) #Hemiltoni
    for i in range(6):
        H[i,i+1]=1
    for i in range(7):
        H[i,i-1]=1
    H[1,6] = 1
    H[6,1] = 1
    H[4,7] = 1
    H[7,4] = 1   
    t = int(input("Mennyi idegi?")) #idő
    N = int(input("Mekkora felbontásban?")) #felbontás
    dt = t/N 
    h_vonas = 1
    c = 1
    k_b = 1
    T = 1
    g = c*k_b*T
    p = 0
    kappa = 1
    a = int(input("Mekkora mátrix?"))
    z = np.linspace(0,T,N)
    ro = 0*H
    #c = int(input("Honnan indul az elektron?"))
    #m = int(input("Hol nézük a valószinüséget?"))
    c= 0
    m = 7
    ro[c,c] = 1
    f_e = ((-1j/h_vonas)*H)*dt
    f_e = np.exp(f_e)
    h = np.conj(H)
    f_h = (1j/h_vonas)*h*dt
    f_h = np.exp(f_h)
    for n in range(N):   
        ro = np.mat(f_e) * np.mat(ro)
        ro = np.mat(ro) * np.mat(f_h)
        for i in range(7):
            for k in range(7):
                if i != k: 
                    ro[i,k] = ro[i,k]*(-np.exp(-(g/h_vonas)*dt))
                    p = np.abs(ro[m,m])
                    l = np.zeros(N)
                    l[range(N)] = p
    plt.plot(l,z)