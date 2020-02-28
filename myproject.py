#!/usr/bin/env python3
#homework5 - Reach
import matplotlib.pyplot as plt
import pandas as pd


def printme(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

iris = pd.read_csv('data/iris.data',
                  names=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

printme ("My Projectdataset", iris[:])
#printme ("My Projectdataset", iris.columns)
printme("correlation between fields", iris.corr().to_string())

# Plotting histogram
plt.hist(iris['sepal length in cm'])
plt.title('sepal length in cm')
plt.xlabel('sepal length in cm')
plt.ylabel('sepal length in cm')
plt.savefig(f'plots/sepal length in cm.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(iris['sepal length in cm'], iris['petal length in cm'], color='b')
plt.title('sepal to petal')
plt.xlabel('sepal length in cm')
plt.ylabel('petal length in cm')
plt.savefig(f'plots/sepal_to_petal_scatter.png', format='png')
plt.clf()

# Plotting line chart
plt.plot(iris['petal width in cm'], color='red')
plt.title('petal width in cm')
plt.xlabel('Petal width')
plt.ylabel('Petal Width')
plt.savefig(f'plots/petal width in cm.png', format='png')
plt.close()