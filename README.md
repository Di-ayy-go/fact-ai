# Replication Study of "Fairness and Bias in Online Selection"


This repository is a  reproduction of [Fairness and Bias in Online Selection](http://proceedings.mlr.press/v139/correa21a/correa21a.pdf). This readme contains a high-level explanation of the repository. Inside the files, all functions have docstrings that explain their functionality.


## Requirements

To install requirements: 

```setup

pip install -r requirements.txt

```

It is advisible to run this command in a new environment to avoid package conflicts ([python venv](https://towardsdatascience.com/virtual-environments-104c62d48c54#:~:text=A%20virtual%20environment%20is%20a,a%20system%2Dwide%20Python) or a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)).  

>📋 The datasets required to run the code are included in the repository.


## How run the reproduction

By running the main.ipynb notebook, all algorithms will be called. The plots and values from the reproduction will run and the results will be printed.

### Training code
 This paper does not contain any trainable or pre-trained models.

The selection algorithms are stored in files prefixed with `fair` and `unfair`. `synthetic_data.py` contains the code to generate the data used for the _Equal  P_, _Unequal P_ and Prophet experiment results. All code used to preprocess the datasets is contained in `secretary_data.py`. Lastly, `random_handler.py`, `distributions.py` and `utils.py` contain helper functions and classes.

### Evaluation code
`secretary_eval.py` contains the code that generates evaluation metrics for the algorithms. `prophet_experiments.py`, `secretary_experiments.py`, serve as files that aggregate all previous code and run it to generate the results.

## Remarks
The content of files that have names present in the [original C++ repository](https://github.com/google-research/google-research/blob/master/fairness_and_bias_in_online_selection/) have the same functionality, but the implementation might differ.

📋 The synthetic data generation can be changed by altering the RNG seed in `random_handler.py`.

The images in the _plots_ folder with the \_\_ suffix are the plots used in our reproduction paper.
Similarly, the _distributions_ folder contains distributions for the datasets.