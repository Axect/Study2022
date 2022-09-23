from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Import netCDF file
ncfile = './data/02_float_sub.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
n = var['n'][:]
fl_sub = var['fl_sub'][:]  
true_sub = var['true_sub'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Compare subtractions", fontsize=16)
plt.xlabel(r'$\log_{10} \delta$', fontsize=14)
plt.ylabel(r'Subs', fontsize=14)
plt.yscale('log')

# Plot with Legends
plt.plot(n, fl_sub, 'r--', label=r'$fl(x) - fl(y)$', alpha=0.5)
plt.plot(n, true_sub, 'b', label=r'$x - y$', alpha=0.5)

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("float_sub.png", dpi=300)

error = abs(fl_sub - true_sub) / true_sub * 100

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Compare subtractions", fontsize=16)
plt.xlabel(r'$\log_{10} \delta$', fontsize=14)
plt.ylabel(r'Error (\%)', fontsize=14)
plt.ylim(-1, 101)

# Plot with Legends
plt.plot(n, error, 'k', label=r'$\frac{\Delta_{fl} - \Delta_{\rm true}}{\Delta_{\rm true}}$')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("float_sub_error.png", dpi=300)
