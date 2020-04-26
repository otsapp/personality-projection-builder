# Personality Type Projection

Using 5 personality measures, this project aims to find how easy it is to segment users based on movie preference.

To get an idea of separability, UMAP is applied to the personality measures to build a 2D scatter plot of 1820 Unique users , with colour classification denoting their movie watching preference out of serendipity, popularity, diversity or none.

Interestingly, this approach doesn't seem to segment well, so a next step may be too use a different variable for colour classification.

You can see the default output as example.png in the projection folder:
![alt text](https://github.com/otsapp/personality-projection-builder/blob/master/projection/example.png)

## Running 

Output: a single 2D projection chart saved as .png

1. Download and unzip the dataset: https://grouplens.org/datasets/personality-2018/
2. Install dependencies: `pip install -r requirements.txt`
3. With the project as current working directory: `python personality-projection-builder.py --data-dir [path to your dataset] --plot-name [your name for the PNG file]`
4. Core parameters for UMAP can be adjusted with the following additional arguments:
`--n-neighbors (default=15)
--min-dist (default=0.1)
--n-components (default=2)
--metric (default='euclidean')`
## grouplens Dataset

Unfortunately it's not possible to redistribute this dataset, however it can be accessed (as of April 2020) through https://grouplens.org/datasets/personality-2018/

Citing the following paper:
Nguyen, T.T., Maxwell Harper, F., Terveen, L. et al. Inf Syst Front (2018) 20: 1173.
https://doi.org/10.1007/s10796-017-9782-y

PERSONALITY MEASURES

- **Openness**: an assessment score (from 1 to 7) assessing user tendency to prefer new experience. 1 means the user has tendency NOT to prefer new experience, 7 means the user has tendency to prefer new experience.

- **Agreeableness**: an assessment score (from 1 to 7) assessing user tendency to be compassionate and cooperative rather than suspicious and antagonistic towards others. 1 means the user has tendency to NOT be compassionate and cooperative. 7 means the user has tendency to be compassionate and cooperative.

- **Emotional Stability**: an assessment score (from 1 to 7) assessing user tendency to have psychological stress. 1 means the user has tendency to have psychological stress, and 7 means the user has tendency to NOT have psychological stress.

- **Conscientiousness**: an assessment score (from 1 to 7) assessing user tendency to be organized and dependable, and show self-discipline. 1 means the user does not have such a tendency, and 7 means the user has such tendency.

- **Extraversion**: an assessment score (from 1 to 7) assessing user tendency to be outgoing. 1 means the user does not have such a tendency, and 7 means the user has such a tendency.

LABEL

- **Assigned Metric**: one of the follows (serendipity, popularity, diversity, default). Each user, besides being assessed their personality, was evaluated their preferences for a list of 12 movies manipulated with serendipity, popularity, diversity value or none (default option).
