# Physiological protein homodimers Benchmark

## Structure

* `pdbs`: folder containing for a given version (i.e. `v2`) all the PDB structures ready.
* `prediction`: prediction files for each of the methods benchmarked.

### Files

* `pdbs/v2/complex.list`: list of all complexes in the benchmark
* `pdbs/v2/physiological.list`: all complexes classified as physiological
* `pdbs/v2/nonphysiological.list`: all complexes classified as non-physiological
* `pdbs/v2/error.list`: Errors found on PDB structures which have been manually curated.

## Methods

### PRODIGY-CRYSTAL

```
Size of complex list: 977
Size of Physiological list: 836
Size of Non Physiological list: 141
Predicted as BIO and Physiological: 636
Predicted as BIO and Non-Physiological: 50
Predicted as CRYSTAL and Physiological: 200
Predicted as CRYSTAL and Non-Physiological: 91

Success rate: 0.74%
```
