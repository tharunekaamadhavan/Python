import matplotlib.pyplot as plt
x=[1,2,3,5]
y=[9,15,20,25]
plt.errorbar(x,y,xerr=0.9,fmt='o',color='orange',ecolor='lightgreen',elinewidth=5, capsize=10)
plt.show()
