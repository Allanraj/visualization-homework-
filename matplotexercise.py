import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv',
                      sep=',',
                      header=0)

pretty_print("insurance dataframe", insurance.to_string())
pretty_print("insurance columns", insurance.columns)

os.makedirs("plots", exist_ok=True)

# Plotting line chart
plt.plot(insurance['charges'], color='red')
plt.title('charges by Index')
plt.xlabel('charges')
plt.ylabel('charges')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.clf()


# Plotting histogram
plt.hist(insurance['bmi']) #, bins=3, color='g')
plt.title('bmi')
plt.xlabel('bmi')
plt.ylabel('bmi')
plt.savefig(f'plots/bmi.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age to charge')
plt.xlabel('Age')
plt.ylabel('charge')
plt.savefig(f'plots/age_to_charge_scatter.png', format='png')

plt.close()