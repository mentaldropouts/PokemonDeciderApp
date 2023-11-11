from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_bar(df, name, title):
    data = df.sort_values(by=name, ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(6, 6))
    g = sns.barplot(data=data, y='Name', x=name)
    for p in g.patches:
        ax.annotate(
            format(p.get_width(), '.0f'),
            (p.get_height() + p.get_width(), p.get_y()),
            ha='left', va='top'
        )
    plt.title(title)
    plt.show()
    return list(data['Name'].values)

gen1 = pd.read_csv('pokemon.csv').drop('#', axis=1)

mask = gen1['Name'].str.startswith('Mega')

gen1 = gen1[~mask]

gen1 = gen1[gen1['Generation'] == 1].reset_index() #Generation 1

gen1['Total'] = gen1['HP'] + gen1['Attack'] + gen1['Defense'] + gen1['Sp. Atk'] + gen1['Sp. Def'] + gen1['Speed']

gen1['Type 2'].fillna('None', inplace=True)

top_of_tops = []

top_of_tops += plot_bar(gen1, name='Total', title='Top 10 Pokemon with the highest total stats')

top_of_tops += plot_bar(gen1, name='HP', title='Top 10 Pokemon with the highest health')

top_of_tops += plot_bar(gen1, name='Attack', title='Top 10 Pokemon with the highest base attack power')

top_of_tops += plot_bar(gen1, name='Defense', title='Top 10 Pokemon with the highest basic defense')

top_of_tops += plot_bar(gen1, name='Sp. Atk', title='Top 10 Pokemon with the highest special attack power')

top_of_tops += plot_bar(gen1, name='Sp. Def', title='Top 10 Pokemon with the highest special defense')

top_of_tops += plot_bar(gen1, name='Speed', title='Top 10 Pokemon with the highest speed')

top_of_top_df = pd.DataFrame(Counter(top_of_tops).items(), columns=['Name', 'Count']).sort_values(by='Count', ascending=False)

plot_bar(top_of_top_df.head(10), name='Count', title='Pokemon at the top of the top 10 charts')