"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""
import matplotlib.pyplot as plt
import seaborn as sns

# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

def visualization_KDN(input_vars, labels, shades, colors, xlabel, ylabel, title, output_image_name):
    """
    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    fig = plt.figure(figsize=(16, 10), dpi=80)
    #plotting KDN
    for i, var in enumerate(input_vars):
        sns.kdeplot(data=var, label=labels[i], shade=shades[i], color=colors[i])

    # Starter code for labeling the image
    plt.xlabel(xlabel, figure = fig)
    plt.ylabel(ylabel, figure = fig)
    plt.title(title, figure= fig)
    plt.legend()
    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
    return fig

def visualization_BOX(x_var, y_var, data, hue, xlabel, ylabel, title, output_image_name):
    """
    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    fig = plt.figure(figsize=(16, 10), dpi=80)
    #plotting KDN
    sns.boxplot(x=x_var, y=y_var, data=data, hue=hue, showfliers=False)
    # Starter code for labeling the image
    plt.xlabel(xlabel, figure = fig)
    plt.ylabel(ylabel, figure = fig)
    plt.title(title, figure= fig)
    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
    return fig

