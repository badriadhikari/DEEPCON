### DEEPCON using Covariance features as input

#### Predict
```bash
python ../deepcon-covariance.py --aln ./16pkA0.aln --rr ./16pkA0.rr
```

#### Evaluate
```bash
./coneva-lite.pl -pdb ./16pkA.pdb -rr ./16pkA0.rr
```
