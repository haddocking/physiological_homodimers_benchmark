
# Reproduction of results

## PDB structures

Used PDB structures are the ones from the v3 folder (gzipped). Non-supported residues and atoms are filtered according to:

```bash
for i in `cat complex.list`;do echo $i; grep -v 'MN2\|BR1\|CA2\|CD\|CL1\|CO3\|CU2\|FE2\|FUL\|HEC\|K1\|MG2\|NA\|NI2\|GAL\|NDG\|ACE\|CS\|GLC\|FUC\|MAN\|CO\|SEP\|CTN\|CU1\|BGC\|ZN\|CAS\|MSE\TOP' ${i}.pdb | pdb_delhetatm | pdb_selresname -ALA,CYS,ASP,GLU,PHE,GLY,HIS,ILE,LYS,LEU,MET,ASN,PRO,GLN,ARG,SER,THR,VAL,TRP,TYR > ${i}_parsed.pdb; done
```

## Prediction

Calculated by:

```bash
for i in `cat complex.list`;do echo $i; pdb_wc -c ${i}.pdb | tail -1 | cut -c5- | tr ',' ' ' > ${i}.chains; done
for i in `cat complex.list`;do echo $i; ../prodigy_cryst/interface_classifier.py ${i}_parsed.pdb --contact_list --selection `cat ${i}.chains | cut -c1-3` > ${i}.out; done
```

## Sucess Rate

```bash
./success_rate.py complex.list ../../pdbs/v3/physiological.list ../../pdbs/v3/nonphysiological.list
./success_rate.py complex_not_in_many.list ../../pdbs/v3/physiological.list ../../pdbs/v3/nonphysiological.list
```

## CSV results

```bash
./parse_prediction.py complex.list overlap.list > prodigy-crystal.csv
```

