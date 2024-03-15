# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Example Cypher Read of RTX-KG2 with Kuzu
#
# Use pip install found below for standalone use through external environments (such as Google Colab).

# for installation in external runtime environments
# !pip install "git+https://github.com/CU-DBMI/rtx-kg2-gateway"

# +
import json
import os
import pathlib
import tarfile

import kuzu
from genson import SchemaBuilder

from notebooks import (
    download_file,
    extract_tar_gz,
    infer_generic_json_schema_from_object,
)
# -

# set some variables for the work below
source_data_url = "https://github.com/CU-DBMI/rtx-kg2-gateway/releases/download/v0.0.1/kg2c_lite_2.8.4.full.with-metanames.dataset.kuzu.tar.gz"
target_dir = "../data"
target_database_path = f"{target_dir}/kg2c_lite_2.8.4.full.with-metanames.dataset.kuzu"

# create a target download path
pathlib.Path(target_dir).mkdir(exist_ok=True)

# niave check for existing database to avoid redownloading / extracting if possible
if not pathlib.Path(target_database_path).is_dir():
    downloaded_file = download_file(url=source_data_url, download_dir=target_dir)
    extract_dir = extract_tar_gz(
        tar_gz_path=f"{target_dir}/{downloaded_file}", output_dir=target_dir
    )

# init a Kuzu database and connection
db = kuzu.Database(target_database_path)
kz_conn = kuzu.Connection(db)

# gather table details from Kuzu database
df_table_names_by_type = kz_conn.execute(
    """
    /* SHOW_TABLES() is a special Kuzu function for
    sharing database table details. */
    CALL SHOW_TABLES()

    /* filter to REL_GROUP's and NODE table types */
    WHERE type IN ['REL_GROUP', 'NODE']

    RETURN name, type
    ORDER BY type, name ASC;
    """
).get_as_df()
df_table_names_by_type


def filter_entity_metadata(entity_json: dict) -> dict:
    """
    Filters the metadata from Kuzu cypher entity.
    """
    return {
        key: value
        for key, value in entity_json.items()
        # exclude offset and node label
        if not key.startswith("_")
    }


# +
# gather node entity example from Kuzu database
example_node = kz_conn.execute(
    """
    /* match on arbitrary node */
    MATCH (node)
    WHERE node.id = 'UMLS:C2459634'
    RETURN 
        node.id,
        node.name,
        node.category,
        node.all_categories
    LIMIT 1;
    """
).get_as_df()

example_node.head()

# +
# gather rel entity example from Kuzu database
example_rel = kz_conn.execute(
    """
    /* match on arbitrary relationship */
    MATCH ()-[relationship:treats]-()
    WHERE relationship.id = 19799062
    RETURN 
        relationship.domain_range_exclusion,
        relationship.id,
        relationship.predicate,
        relationship.primary_knowledge_source,
        relationship.qualified_object_aspect,
        relationship.qualified_object_direction,
        relationship.qualified_predicate
    LIMIT 1;
    """
).get_as_df()

example_rel.head()
# -

# run an example query for down syndrome disease
kz_conn.execute(
    """
    MATCH (d:Disease)
    WHERE d.name = "Down syndrome"
    RETURN 
        d.id,
        d.name,
        d.category,
        d.all_categories;
    """
).get_as_df()

# run an example query for down syndrome disease
# showing one relationship to a gene
kz_conn.execute(
    """
    MATCH (d:Disease)-[r]-(g:Gene)
    WHERE d.name = "Down syndrome"
    RETURN 
        d.id,
        d.name,
        d.category,
        d.all_categories,
        r.predicate,
        g.id,
        g.name,
        g.category,
        g.all_categories
    LIMIT 1;
    """
).get_as_df()
