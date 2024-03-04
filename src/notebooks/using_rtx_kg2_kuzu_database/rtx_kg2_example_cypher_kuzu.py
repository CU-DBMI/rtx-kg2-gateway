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


# gather node entity example from Kuzu database
example_node = filter_entity_metadata(
    entity_json=kz_conn.execute(
        """
        /* match on arbitrary node */
        MATCH (node)
        WHERE node.id = 'UMLS:C2459634'
        RETURN *
        LIMIT 1;
        """
    ).get_next()[0]
)
example_node

# gather rel entity example from Kuzu database
example_rel = filter_entity_metadata(
    entity_json=kz_conn.execute(
        """
        /* match on arbitrary relationship */
        MATCH ()-[r:treats]-()
        WHERE r.id = 19799062
        RETURN r
        LIMIT 1;
        """
    ).get_next()[0]
)
example_rel


def generate_entity_example_html_table(entity_json: dict) -> str:
    """
    Generates an HTML table for showing
    an example of entity data and schema.
    """
    return f"""<table>
<tr>
<th>Example data</th>
<th>Example data JSON schema</th>
</tr>
<td>

```json
{json.dumps(entity_json, indent=2)}
```

</td>
<td>

```json
{infer_generic_json_schema_from_object(entity_json)}
```

</td>
</tr>
</table>
"""


with open(
    "rtx-kg2-gateway-kuzu-database-details.md", mode="w", encoding="utf-8"
) as markdown_file:

    markdown_file.write(
        """# RTX-KG2-gateway Kuzu Database Schema Details

Please see below for details on the Kuzu database associated with RTX-KG2 created as part of this project.

## Table types

Tables below are provided as either NODE or REL_GROUP tables.
[REL_GROUPS](https://kuzudb.com/docusaurus/cypher/data-definition/create-table#create-rel-table-group) are specialized tables within Kuzu databases that are collections of NODE type pairs.
REL_GROUPS are shown by name below which can be referenced as part of Cypher queries (instead of the more verbose and many NODE type pairs).

"""
    )

    markdown_file.write(
        "\n\n".join(
            [
                f"""### {table_type} Tables

#### Example {table_type} Data and JSON Schema

{generate_entity_example_html_table(example_node) if table_type == "NODE" else generate_entity_example_html_table(example_rel)}

#### {table_type} Names

{table_md_content}
"""
                for table_type, table_md_content in {
                    table_type: df_table_names_by_type[
                        df_table_names_by_type["type"] == table_type
                    ][["name", "type"]].to_markdown(index=False)
                    for table_type in df_table_names_by_type["type"].unique().tolist()
                }.items()
            ]
        )
    )

# run an example query
kz_conn.execute(
    """
    MATCH (d:Disease)
    WHERE d.name = "Down syndrome"
    RETURN d.id, d.name, d.all_categories;
    """
).get_as_df()
