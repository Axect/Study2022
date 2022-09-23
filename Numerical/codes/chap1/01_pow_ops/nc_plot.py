from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Import netCDF file
ncfile = './data/01_pow.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
x = var['x'][:]
p = var['p'][:]  
q = var['q'][:]
r = var['r'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Various pows", fontsize=16)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y$', fontsize=14)

# Plot with Legends
plt.plot(x, p, label=r'$p(x)$', alpha=0.8)
plt.plot(x, q, label=r'$q(x)$', alpha=0.8)
plt.plot(x, r, label=r'$r(x)$', alpha=0.8)

#plt.ylim([-2e-16, 2e-16])

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/01_pow_plot.png", dpi=300)
