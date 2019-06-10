### DEEPCON with sequence features as input

#### Generate feature file
```bash
./deepcon-seq-step1.pl 5ptpA.aln 5ptpA
```
#### Predict RR
```bash
python ./deepcon-seq-step2.py --feat 5ptpA/5ptpA.input.features --rr 5ptpA.rr
```
