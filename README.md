# What is UniLanguage?
[[PAPER](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CITATION](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CODE](github)]&nbsp;&nbsp;&nbsp;&nbsp;[[DATASET DOWNLOAD](dtu)]

# Abstract
## Motivation
Language modelling (LM) on biological sequences is an emergent topic in the field of bioinformatics.
Current research has shown that language modelling of proteins can create context-dependent representations that can be applied to improve performance on different protein prediction tasks.
However, little effort has been directed towards analyzing the properties of the datasets used to train language models.
Additionally, only the performance of cherry-picked downstream tasks are used to assess the capacity of LMs.
## Results
We analyze the entire UniProt database and investigate the different properties that can bias or hinder the performance of LMs such as homology, domain of origin, quality of the data, and completeness of the sequence.
We evaluate n-gram and Recurrent Neural Network (RNN) LMs to assess the impact of these properties on performance.
To our knowledge, this is the first protein dataset with an emphasis on language modelling.
Our inclusion of properties specific to proteins gives a detailed analysis of how well natural language processing methods work on biological sequences.
We find that organism domain and quality of  data have an impact on the performance, while the completeness of the proteins has little influence.
%How does it perform?
The RNN based LM can learn to model Bacteria, Eukarya, and Archaea; but struggles with Viruses.
By using the LM we can also generate novel proteins that are shown to be similar to real proteins.

# Process of creating UniLanguage
We scrape all of UniProt - **250M proteins as of 2019-10-01**.
The proteins with experimental evidence (high quality, 1% of UniProt) are homology partitioned, with 20% homology, into train-, validation-, and test set with 60% train, 10% validation and 30% test for each domain on both full proteins and fragments.

Predicted proteins (low quality, 99% of UniProt) are homology compared against the validation and testset with 20% homology.
If predicted proteins do not overlap they are kept as a predicted training set, split into domains and fragments.
This removes about 50% of the predicted proteins (approx. 85 million!), which truly indicates the homogenousness in UniProt proteins.

# Dataset and results
We provide train, validation and testsets for all domains. Notice that fragments are also included for validation and testing, but we do not use them in our work.

| Link         | Partitions | Domain   | Quality | Samples | Mean Length | Fragments |
|--------------|------------|----------|---------|---------|-------------|-----------|
| [Download]() | Train      | Eukarya  | High    |         |             | No        |
| [Download]() | Train      | Eukarya  | High    |         |             | Yes       |
| [Download]() | Train      | Eukarya  | Low     |         |             | No        |
| [Download]() | Train      | Eukarya  | Low     |         |             | Yes       |
| [Download]() | Valid      | Eukarya  | High    |         |             | No        |
| [Download]() | Valid      | Eukarya  | High    |         |             | Yes       |
| [Download]() | Test       | Eukarya  | High    |         |             | No        |
| [Download]() | Test       | Eukarya  | High    |         |             | Yes       |
| [Download]() | Train      | Bacteria | High    |         |             | No        |
| [Download]() | Train      | Bacteria | High    |         |             | Yes       |
| [Download]() | Train      | Bacteria | Low     |         |             | No        |
| [Download]() | Train      | Bacteria | Low     |         |             | Yes       |
| [Download]() | Valid      | Bacteria | High    |         |             | No        |
| [Download]() | Test       | Bacteria | High    |         |             | No        |
| [Download]() | Train      | Archaea  | High    |         |             | No        |
| [Download]() | Train      | Archaea  | High    |         |             | Yes       |
| [Download]() | Train      | Archaea  | Low     |         |             | No        |
| [Download]() | Train      | Archaea  | Low     |         |             | Yes       |
| [Download]() | Valid      | Archaea  | High    |         |             | No        |
| [Download]() | Test       | Archaea  | High    |         |             | No        |
| [Download]() | Train      | Virus    | High    |         |             | No        |
| [Download]() | Train      | Virus    | High    |         |             | Yes       |
| [Download]() | Train      | Virus    | Low     |         |             | No        |
| [Download]() | Train      | Virus    | Low     |         |             | Yes       |
| [Download]() | Valid      | Virus    | High    |         |             | No        |
| [Download]() | Test       | Virus    | High    |         |             | No        |

# Citation
[[PAPER](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CITATION](bioxiv)]&nbsp;&nbsp;&nbsp;&nbsp;[[CODE](github)]&nbsp;&nbsp;&nbsp;&nbsp;[[DATASET DOWNLOAD](dtu)]

PUT IN CITATION
