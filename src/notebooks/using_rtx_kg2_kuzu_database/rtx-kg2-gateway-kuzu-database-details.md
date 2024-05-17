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
  "node.id": "UMLS:C2459634",
  "node.name": "Oral Peripheral Mechanism Assessment using Other Equipment",
  "node.all_categories": [
    "biolink:Procedure"
  ],
  "node.category": "biolink:Procedure"
}
```

</td>
<td>

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "node.id": {
      "type": "string"
    },
    "node.name": {
      "type": "string"
    },
    "node.all_categories": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "node.category": {
      "type": "string"
    }
  },
  "required": [
    "node.all_categories",
    "node.category",
    "node.id",
    "node.name"
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
| CellLine                        | NODE   |
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
| Event                           | NODE   |
| Exon                            | NODE   |
| Food                            | NODE   |
| GenomicEntity                   | NODE   |
| GeographicLocation              | NODE   |
| IndividualOrganism              | NODE   |
| LifeStage                       | NODE   |
| MolecularActivity               | NODE   |
| MolecularEntity                 | NODE   |
| MolecularMixture                | NODE   |
| NoncodingRNAProduct             | NODE   |
| NucleicAcidEntity               | NODE   |
| OrganismAttribute               | NODE   |
| PathologicalProcess             | NODE   |
| Protein                         | NODE   |
| ProteinDomain                   | NODE   |
| Transcript                      | NODE   |
| EnvironmentalProcess            | NODE   |
| Gene                            | NODE   |
| GrossAnatomicalStructure        | NODE   |
| MaterialSample                  | NODE   |
| Pathway                         | NODE   |
| PhenotypicFeature               | NODE   |
| SmallMolecule                   | NODE   |
| GeneFamily                      | NODE   |
| GeneticInheritance              | NODE   |
| InformationContentEntity        | NODE   |
| MicroRNA                        | NODE   |
| Phenomenon                      | NODE   |
| PhysicalEntity                  | NODE   |
| PhysiologicalProcess            | NODE   |
| Polypeptide                     | NODE   |
| Publication                     | NODE   |
| NamedThing                      | NODE   |
| OrganismTaxon                   | NODE   |
| OrganismalEntity                | NODE   |
| PopulationOfIndividualOrganisms | NODE   |
| ProteinFamily                   | NODE   |
| RNAProduct                      | NODE   |
| Procedure                       | NODE   |
| RetrievalSource                 | NODE   |
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
  "r.qualified_object_aspect": "",
  "r.predicate": "biolink:treats",
  "r.domain_range_exclusion": "True",
  "r.qualified_object_direction": "",
  "r.id": 19799062,
  "r.primary_knowledge_source": "infores:semmeddb",
  "r.qualified_predicate": ""
}
```

</td>
<td>

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "r.qualified_object_aspect": {
      "type": "string"
    },
    "r.predicate": {
      "type": "string"
    },
    "r.domain_range_exclusion": {
      "type": "string"
    },
    "r.qualified_object_direction": {
      "type": "string"
    },
    "r.id": {
      "type": "integer"
    },
    "r.primary_knowledge_source": {
      "type": "string"
    },
    "r.qualified_predicate": {
      "type": "string"
    }
  },
  "required": [
    "r.domain_range_exclusion",
    "r.id",
    "r.predicate",
    "r.primary_knowledge_source",
    "r.qualified_object_aspect",
    "r.qualified_object_direction",
    "r.qualified_predicate"
  ]
}
```

</td>
</tr>
</table>

#### REL_GROUP Names

| name                                 | type      |
|:-------------------------------------|:----------|
| biomarker_for                        | REL_GROUP |
| chemically_similar_to                | REL_GROUP |
| close_match                          | REL_GROUP |
| associated_with                      | REL_GROUP |
| actively_involved_in                 | REL_GROUP |
| catalyzes                            | REL_GROUP |
| composed_primarily_of                | REL_GROUP |
| affects                              | REL_GROUP |
| capable_of                           | REL_GROUP |
| causes                               | REL_GROUP |
| coexists_with                        | REL_GROUP |
| colocalizes_with                     | REL_GROUP |
| contraindicated_for                  | REL_GROUP |
| contributes_to                       | REL_GROUP |
| disease_has_basis_in                 | REL_GROUP |
| correlated_with                      | REL_GROUP |
| directly_physically_interacts_with   | REL_GROUP |
| derives_from                         | REL_GROUP |
| develops_from                        | REL_GROUP |
| diagnoses                            | REL_GROUP |
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
| has_participant                      | REL_GROUP |
| has_metabolite                       | REL_GROUP |
| has_output                           | REL_GROUP |
| has_part                             | REL_GROUP |
| has_phenotype                        | REL_GROUP |
| has_plasma_membrane_part             | REL_GROUP |
| homologous_to                        | REL_GROUP |
| overlaps                             | REL_GROUP |
| in_taxon                             | REL_GROUP |
| indirectly_physically_interacts_with | REL_GROUP |
| is_sequence_variant_of               | REL_GROUP |
| lacks_part                           | REL_GROUP |
| manifestation_of                     | REL_GROUP |
| located_in                           | REL_GROUP |
| occurs_in                            | REL_GROUP |
| physically_interacts_with            | REL_GROUP |
| precedes                             | REL_GROUP |
| predisposes                          | REL_GROUP |
| prevents                             | REL_GROUP |
| produces                             | REL_GROUP |
| regulates                            | REL_GROUP |
| related_to                           | REL_GROUP |
| same_as                              | REL_GROUP |
| subclass_of                          | REL_GROUP |
| superclass_of                        | REL_GROUP |
| temporally_related_to                | REL_GROUP |
| transcribed_from                     | REL_GROUP |
| translates_to                        | REL_GROUP |
| treats                               | REL_GROUP |
