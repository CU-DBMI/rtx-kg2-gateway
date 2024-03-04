# RTX-KG2-gateway Kuzu Database Schema Details

Please see below for details on the Kuzu database associated with RTX-KG2 created as part of this project.

## Table types

Tables below are provided as either NODE or REL_GROUP tables.
[REL_GROUPS](https://kuzudb.com/docusaurus/cypher/data-definition/create-table#create-rel-table-group) are specialized tables within Kuzu databases that are collections of NODE type pairs.
REL_GROUPS are shown by name below which can be referenced as part of Cypher queries (instead of the more verbose and many NODE type pairs).

### NODE Tables 

#### Example NODE Data and JSON Schema

<table>
<tr>
<th>Example data</th>
<th>Example data JSON schema</th>
</tr>
<td>

```json
{
  "id": "UMLS:C2459634",
  "name": "Oral Peripheral Mechanism Assessment using Other Equipment",
  "all_categories": [
    "biolink:Procedure"
  ],
  "category": "biolink:Procedure"
}
```

</td>
<td>

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "all_categories": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "category": {
      "type": "string"
    }
  },
  "required": [
    "all_categories",
    "category",
    "id",
    "name"
  ]
}
```

</td>
</tr>
</table>


#### NODE Names

| name                            | type   |
|:--------------------------------|:-------|
| Activity                        | NODE   |
| Agent                           | NODE   |
| AnatomicalEntity                | NODE   |
| Behavior                        | NODE   |
| BehavioralFeature               | NODE   |
| BiologicalEntity                | NODE   |
| BiologicalProcess               | NODE   |
| Cell                            | NODE   |
| CellularComponent               | NODE   |
| ChemicalEntity                  | NODE   |
| ChemicalMixture                 | NODE   |
| ClinicalAttribute               | NODE   |
| ClinicalIntervention            | NODE   |
| Cohort                          | NODE   |
| ComplexMolecularMixture         | NODE   |
| Device                          | NODE   |
| Disease                         | NODE   |
| DiseaseOrPhenotypicFeature      | NODE   |
| Drug                            | NODE   |
| EnvironmentalFeature            | NODE   |
| EnvironmentalProcess            | NODE   |
| Event                           | NODE   |
| Exon                            | NODE   |
| Food                            | NODE   |
| Gene                            | NODE   |
| GeneFamily                      | NODE   |
| GeneticInheritance              | NODE   |
| GenomicEntity                   | NODE   |
| MolecularActivity               | NODE   |
| MolecularEntity                 | NODE   |
| MolecularMixture                | NODE   |
| NamedThing                      | NODE   |
| NucleicAcidEntity               | NODE   |
| PathologicalProcess             | NODE   |
| Phenomenon                      | NODE   |
| Polypeptide                     | NODE   |
| PopulationOfIndividualOrganisms | NODE   |
| CellLine                        | NODE   |
| GeographicLocation              | NODE   |
| GrossAnatomicalStructure        | NODE   |
| IndividualOrganism              | NODE   |
| InformationContentEntity        | NODE   |
| LifeStage                       | NODE   |
| MaterialSample                  | NODE   |
| MicroRNA                        | NODE   |
| NoncodingRNAProduct             | NODE   |
| OrganismAttribute               | NODE   |
| OrganismTaxon                   | NODE   |
| OrganismalEntity                | NODE   |
| Pathway                         | NODE   |
| PhenotypicFeature               | NODE   |
| PhysicalEntity                  | NODE   |
| PhysiologicalProcess            | NODE   |
| Procedure                       | NODE   |
| Protein                         | NODE   |
| ProteinDomain                   | NODE   |
| ProteinFamily                   | NODE   |
| RNAProduct                      | NODE   |
| RetrievalSource                 | NODE   |
| SmallMolecule                   | NODE   |
| Transcript                      | NODE   |
| Publication                     | NODE   |
| Treatment                       | NODE   |


### REL_GROUP Tables 

#### Example REL_GROUP Data and JSON Schema

<table>
<tr>
<th>Example data</th>
<th>Example data JSON schema</th>
</tr>
<td>

```json
{
  "qualified_object_aspect": "",
  "predicate": "biolink:treats",
  "domain_range_exclusion": "True",
  "qualified_object_direction": "",
  "id": 19799062,
  "primary_knowledge_source": "infores:semmeddb",
  "qualified_predicate": ""
}
```

</td>
<td>

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "qualified_object_aspect": {
      "type": "string"
    },
    "predicate": {
      "type": "string"
    },
    "domain_range_exclusion": {
      "type": "string"
    },
    "qualified_object_direction": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "primary_knowledge_source": {
      "type": "string"
    },
    "qualified_predicate": {
      "type": "string"
    }
  },
  "required": [
    "domain_range_exclusion",
    "id",
    "predicate",
    "primary_knowledge_source",
    "qualified_object_aspect",
    "qualified_object_direction",
    "qualified_predicate"
  ]
}
```

</td>
</tr>
</table>


#### REL_GROUP Names

| name                                 | type      |
|:-------------------------------------|:----------|
| associated_with                      | REL_GROUP |
| affects                              | REL_GROUP |
| actively_involved_in                 | REL_GROUP |
| biomarker_for                        | REL_GROUP |
| capable_of                           | REL_GROUP |
| catalyzes                            | REL_GROUP |
| causes                               | REL_GROUP |
| chemically_similar_to                | REL_GROUP |
| close_match                          | REL_GROUP |
| coexists_with                        | REL_GROUP |
| colocalizes_with                     | REL_GROUP |
| composed_primarily_of                | REL_GROUP |
| contraindicated_for                  | REL_GROUP |
| contributes_to                       | REL_GROUP |
| correlated_with                      | REL_GROUP |
| derives_from                         | REL_GROUP |
| develops_from                        | REL_GROUP |
| diagnoses                            | REL_GROUP |
| directly_physically_interacts_with   | REL_GROUP |
| disease_has_basis_in                 | REL_GROUP |
| disease_has_location                 | REL_GROUP |
| disrupts                             | REL_GROUP |
| enables                              | REL_GROUP |
| exacerbates                          | REL_GROUP |
| expressed_in                         | REL_GROUP |
| gene_associated_with_condition       | REL_GROUP |
| gene_product_of                      | REL_GROUP |
| has_decreased_amount                 | REL_GROUP |
| has_increased_amount                 | REL_GROUP |
| has_input                            | REL_GROUP |
| has_member                           | REL_GROUP |
| has_metabolite                       | REL_GROUP |
| has_output                           | REL_GROUP |
| has_part                             | REL_GROUP |
| has_participant                      | REL_GROUP |
| has_phenotype                        | REL_GROUP |
| has_plasma_membrane_part             | REL_GROUP |
| homologous_to                        | REL_GROUP |
| in_taxon                             | REL_GROUP |
| indirectly_physically_interacts_with | REL_GROUP |
| is_sequence_variant_of               | REL_GROUP |
| lacks_part                           | REL_GROUP |
| located_in                           | REL_GROUP |
| manifestation_of                     | REL_GROUP |
| occurs_in                            | REL_GROUP |
| overlaps                             | REL_GROUP |
| physically_interacts_with            | REL_GROUP |
| precedes                             | REL_GROUP |
| regulates                            | REL_GROUP |
| predisposes                          | REL_GROUP |
| prevents                             | REL_GROUP |
| produces                             | REL_GROUP |
| related_to                           | REL_GROUP |
| same_as                              | REL_GROUP |
| subclass_of                          | REL_GROUP |
| superclass_of                        | REL_GROUP |
| temporally_related_to                | REL_GROUP |
| transcribed_from                     | REL_GROUP |
| treats                               | REL_GROUP |
| translates_to                        | REL_GROUP |
