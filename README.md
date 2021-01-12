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
Size of complex list: 977
Size of Physiological list: 836
Size of Non Physiological list: 141
Predicted as BIO and Physiological: 636
Predicted as BIO and Non-Physiological: 50
Predicted as CRYSTAL and Physiological: 200
Predicted as CRYSTAL and Non-Physiological: 91

Success rate: 74.41%
```

#### Performance on this data set excluding overlapping with the MANY dataset:

(See `prediction/prodigy-crystal/overlap.list`)

```
Size of complex list: 864
Size of Physiological list: 735
Size of Non Physiological list: 129
Predicted as BIO and Physiological: 541
Predicted as BIO and Non-Physiological: 46
Predicted as CRYSTAL and Physiological: 194
Predicted as CRYSTAL and Non-Physiological: 83

Success rate: 72.22%
```
