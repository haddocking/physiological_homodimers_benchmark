# Physiological protein homodimers Benchmark

## Structure

* `pdbs`: folder containing for a given version (i.e. `v2`) all the PDB structures ready.
* `prediction`: prediction files for each of the methods benchmarked.

### Files

* `pdbs/v2/complex.list`: list of all complexes in the benchmark
* `pdbs/v2/physiological.list`: all complexes classified as physiological
* `pdbs/v2/nonphysiological.list`: all complexes classified as non-physiological
* `pdbs/v2/error.list`: Errors found on PDB structures which have been manually curated.
* `pdbs/v2/pdb_chains.list`: PDB IDs and chains IDs for each complex.

## Methods

### PRODIGY-CRYSTAL


The classification into physiological assemblies and crystal contacts is based on the contact-based PRODIGY-CRYSTAL method, described online [here](https://bianca.science.uu.nl/prodigy/method#heading_c_three) and published in:

* K. Elez, A.M.J.J. Bonvin* and A. Vangone. 
[Distinguishing crystallographic from biological interfaces in protein complexes: Role of intermolecular contacts and energetics for classification](https://doi.org/10.1186/s12859-018-2414-9). BMC Bioinformatics, 19 (Suppl 15), 438 (2018).

PRODIGY-CRYSTAL is available as a [web server](https://bianca.science.uu.nl/prodigy/):

* B. Jiménez-García, K. Elez, P.I. Koukos, A.M.J.J. Bonvin and A. Vangone. 
[PRODIGY-crystal: a web-tool for classification of biological interfaces in protein complexes](https://doi.org/10.1093/bioinformatics/btz437). Bioinformatics, 35, 4821–4823 (2019).

and the code is available from our [GitHub repository](https://github.com/haddocking/prodigy-cryst).


#### Performance on this data set:

```
Size of complex list: 1677
Size of Physiological list: 836
Size of Non Physiological list: 841
Predicted as BIO and Physiological: 539
Predicted as BIO and Non-Physiological: 409
Predicted as CRYSTAL and Physiological: 297
Predicted as CRYSTAL and Non-Physiological: 432

Success rate: 57.9%
```

#### Performance on this data set excluding overlapping with the MANY dataset:

(See `prediction/prodigy-crystal/overlap.list`)

```
Size of complex list: 1546
Size of Physiological list: 836
Size of Non Physiological list: 841
Predicted as BIO and Physiological: 457
Predicted as BIO and Non-Physiological: 401
Predicted as CRYSTAL and Physiological: 278
Predicted as CRYSTAL and Non-Physiological: 410

Success rate: 56.08%
```

### Deeprank 

The [Deeprank](https://github.com/DeepRank/deeprank) classification is based on a 3D Convolution Neural Network (CNN) that has been pre-trained on the [MANY dataset](https://pubmed.ncbi.nlm.nih.gov/25326082/), which consists of 2828 biological interfaces and 2911 crystal ones, only using PSSM features. The MANY dataset was devided into a training (80%) and a validation set (20%), while maintaining the balance between positive and negative data. The training dataset was augmented by randomly rotating each complex 30 times.

29 complexes have been discarded from the dataset classification due to :
- the lack of pssm matrix 40 complexes)
- Others - See prediction/deeprank/data/README_*_dataset (15 complexes)

#### Performance on this data set:

```
Size of complex list: 1677
Size of complex list processed : 1622
Size of Physiological list: 836
Size of Non Physiological list: 841
Predicted as BIO and Physiological: 642
Predicted as BIO and Non-Physiological: 222
Predicted as CRYSTAL and Physiological: 187
Predicted as CRYSTAL and Non-Physiological: 571

Success rate (considering unprocessed data): 72.332%
Success rate (omitting unprocessed data): 74.784%
```

#### Performance on this data set excluding overlapping with the MANY dataset:

```
Size of complex list: 1551
Size of complex list processed : 1497
Size of Physiological list: 735
Size of Non Physiological list: 816
Predicted as BIO and Physiological: 551
Predicted as BIO and Non-Physiological: 220
Predicted as CRYSTAL and Physiological: 178
Predicted as CRYSTAL and Non-Physiological: 548

Success rate (considering unprocessed data): 70.858%
Success rate (omitting unprocessed data): 73.413%
```

(See `prediction/deeprank/deeprank_prediction_v2.list`)
