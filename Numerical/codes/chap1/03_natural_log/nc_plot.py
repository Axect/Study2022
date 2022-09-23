from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Import netCDF file
ncfile = './data/natural_log.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
x = var['x'][:]
y1 = var['y1'][:]
y2 = var['y2'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Compare natural logarithms", fontsize=16)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$\ln(1+x)$', fontsize=14)
plt.xscale('log')
plt.yscale('log')

# Plot with Legends
plt.plot(x, y1, 'r--', label=r'$\ln(1+x)$', alpha=0.5)
plt.plot(x, y2, 'b', label=r'$\frac{x\ln(1+x)}{(1+x) - 1}$', alpha=0.5)

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("natural_log.png", dpi=300)
