
# Reproduction of results

## PDB structures

Used PDB structures are the ones from the HADDOCK prediction folder (gzipped). Non-supported residues and atoms are filtered according to:

```bash
grep -v 'MN2\|BR1\|CA2\|CD\|CL1\|CO3\|CU2\|FE2\|FUL\|HEC\|K1\|MG2\|NA\|NI2\|GAL\|NDG\|ACE\|CS\|GLC\|FUC\|MAN\|CO\|SEP\|CTN\|CU1\|BGC\|ZN'
```

## Prediction

Calculated by:

```bash
for i in `cat complex.list`;do echo $i; interface_classifier.py ${i}.pdb --contact_list --selection A B > ${i}.out; done
```

## Sucess Rate

```bash
./success_rate.py complex.list ../../pdbs/v2/physiological.list ../../pdbs/v2/nonphysiological.list
./success_rate.py complex_not_in_many.list ../../pdbs/v2/physiological.list ../../pdbs/v2/nonphysiological.list
```

## CSV results

```bash
./parse_prediction.py complex.list overlap.list > prodigy-crystal.csv
```

