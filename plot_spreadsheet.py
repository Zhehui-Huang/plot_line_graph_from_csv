import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Load the data
tips = pd.read_csv("plot.csv")

# set style
sns.set(style='whitegrid',palette='muted',color_codes=True)
# plot
g = sns.relplot(x="Total num envs", y="fps, frameskip=4", hue="Framework",
            kind="line",
            data=tips, legend='brief')

# Set x, y axis
plt.xlim(xmin = 0, xmax = tips.max(axis=0).values[1] * 1.1)
plt.ylim(ymin = 0, ymax = tips.max(axis=0).values[2] * 1.1)

# mute title of legend
leg = g._legend
leg.texts[0].set_text("")

# save file
plt.savefig(os.path.join(os.getcwd(), "result.eps"), format='eps')