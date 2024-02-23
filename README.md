# RTX-KG2 Gateway

Enabling [RTX-KG2](https://github.com/RTXteam/RTX-KG2) data access through various means.

## Overview

[RTX-KG2](https://github.com/RTXteam/RTX-KG2) provides a knowledge graph composed of many different data sources.
The output data from the RTX-KG2 project can benefit from the use of additional specialized graph database tools for analysis purposes.
Please find a brief overview of these technologies below for a better understanding of how they're used in context with the RTX-KG2 data.

### Graph Database Technologies

- [Kuzu](https://github.com/kuzudb/kuzu): Kuzu is an embeddable property graph database system which provides  querying capabilities through [Cypher](<https://en.wikipedia.org/wiki/Cypher_(query_language)>). Kuzu includes a [Python package](https://pypi.org/project/kuzu/) and related API which enables local queries.

## Installation

### Python

Usage of the contents found within this repository depend on Python being available on the system.
One suggested way to use and manage Python is through [`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) (there are many other ways too!).
Please reference the `pyproject.toml` file for more information on Python versions which are compatible with this project.

### Poetry environment

Please use Python [`poetry`](https://python-poetry.org/) to run and install a Python environment related to this project.
The Poetry environment for this project includes dependencies which help run IDE environments, manage the data, and run workflows.
See here for more information about [installing Poetry](https://python-poetry.org/docs/#installation) within your environment.

```bash
# context: within the root of the repository
# after installing poetry, create the environment
poetry install
```

## Development

### Running and updating Jupyter notebooks

Please follow installation steps above and then use a related Jupyter environment to open and explore the notebooks under the `notebooks` directory.
These notebooks leverage [Jupyter Lab extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html) (such as [`jupytext`](https://jupytext.readthedocs.io/en/latest/)) through the related Poetry environment for this repository.
Usage of the notebooks outside of Jupyter Lab as an IDE may have varied experiences.

```bash
# context: within the root of the repository
# after creating poetry environment, run jupyter
poetry run jupyter lab
```

### Executing sequences of Python modules as tasks

We use [Poe the Poet](https://poethepoet.natn.io/index.html) to define and run tasks defined within `pyproject.toml` under the section `[tool.poe.tasks*]`.
This allows for the definition and use of a task workflow when implementing multiple procedures in sequence.

For example, use the following to run the `notebook_sample_data_generation` task:

```bash
# context: within the root of the repository
# run data_prep task using poethepoet defined within `pyproject.toml`
poetry run poe notebook_sample_data_generation
```

Existing tasks:

- `notebook_sample_data_generation`: generates a sample parquet dataset and adds to a kuzu database.
- `notebook_full_data_generation`: generates full dataset and adds to a kuzu database.
- `notebook_full_data_generation_with_metanames`: generates full dataset with metanames specificity and adds to a kuzu database in similar fashion.

> ⚠ Suggested hardware resources:
> Kuzu data ingest may require memory and storage beyond that of common laptop constraint.
> A recent run `notebook_full_data_generation_with_metanames` involved the use of the following resources:
>
> - Storage: ~40 GB (JSON, Parquet, Kuzu, and compressed files)
> - Memory: ~32 GB (GCP VM [`e2-standard-16`](https://cloud.google.com/compute/docs/general-purpose-machines#e2-standard) was used for this purpose).
> - CPU: 4 vCPU (see VM note above).
>
> Further investigation is needed in order to validate computer resources necessary for these tasks.

## Citation and Acknowledgements

Data used by this repo includes [RTX-KG2](https://github.com/RTXteam/RTX-KG2) which was published at the [NCATS Biomedical Data Translator repository](https://github.com/ncats/translator-lfs-artifacts). Special thanks goes to those mentioned in the [RTX-KG2 credits](https://github.com/RTXteam/RTX-KG2?tab=readme-ov-file#credits). Further data acknowledgments may be found within the [data sources documentation](https://github.com/RTXteam/RTX-KG2?tab=readme-ov-file#what-data-sources-are-used-in-kg2).
