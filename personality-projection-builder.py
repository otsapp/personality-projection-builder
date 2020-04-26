import numpy as np
import pandas as pd
from umap import UMAP
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os


def read_data(path_to_dir, file_name):
    path = os.path.join(path_to_dir, file_name)
    data = pd.read_csv(path)
    return data

def fit_model(data, params):
    personality_measures = data.iloc[:, 1:6]
    u = UMAP(n_neighbors=params['n_neighbors'], min_dist=params['min_dist'], metric=params['metric'])
    embedding = u.fit_transform(personality_measures)
    return embedding

def join_labels(data, embedding):
    df_full = pd.concat([data, pd.DataFrame(embedding)], axis=1)
    df_to_plot = df_full.loc[:, ['userid', 0, 1, ' assigned metric', ' assigned condition']]
    df_to_plot.columns = ['userid', '0_dim', '1_dim', 'assigned metric', 'assigned condition']
    return df_to_plot

def build_plot(df_to_plot, plot_name, plot_path):
    fig = plt.figure(figsize=(10,8))
    plt.title(f"{plot_name}")
    sns.scatterplot(df_to_plot['0_dim'], df_to_plot['1_dim'], hue=df_to_plot['assigned metric'])
    plt.axis('off')
    full_path = os.path.join(plot_path,f"{plot_name}.png")
    fig.savefig(full_path)
    print(f"Plot saved successfully with path: {full_path}")

def build_projection(data, params, plot_name, plot_path):
    embedding = fit_model(data, params)
    df_to_plot = join_labels(data, embedding)
    build_plot(df_to_plot, plot_name, plot_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, help='path to data', default='data/')
    parser.add_argument('--projection-dir', type=str, help='path your plot should be saved', default='projection/')
    parser.add_argument('--plot-name', type=str, help='plot title and file name', default='projection')

    parser.add_argument('--n-neighbors', type=int, default=15)
    parser.add_argument('--min-dist', type=int, default=0.1)
    parser.add_argument('--n-components', type=int, default=2)
    parser.add_argument('--metric', type=str, default='euclidean')
    args = parser.parse_args()

    DEFAULT_PARAMS = {'n_neighbors': args.n_neighbors, 'min_dist': args.min_dist,
                      'n_components': args.n_components, 'metric': args.metric}

    print("Loading data.")
    data = read_data(args.data_dir, 'personality-data.csv')

    print("Building projection.")
    build_projection(data=data, plot_name=args.plot_name,
                    plot_path=args.projection_dir, params=DEFAULT_PARAMS)

