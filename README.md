## DEEPCON: Protein Contact Prediction using Dilated Convolutional Neural Networks with Dropout  


#### Contact:
Email: adhikarib@umsl.edu  
Homepage: https://badriadhikari.github.io/  
Paper: https://www.biorxiv.org/content/10.1101/590455v1 

### DEEPCON using Covariance features as input

Trained and validated using the 3456 proteins in the DeepCov dataset with the covariance features (441 channels) as input.


#### Installation Instructions:
    

You need a deep learing backend that is Keras compatible:

    pip3 install -U tensorflow
    pip3 install pyyaml
	
Install DEEPCON-Covariance package
	
    pip3 install DEEPCON


#### Intstructions for User:

Inside Python:

	import DEEPCON
	

#### Predict
```bash
python ../deepcon-covariance.py --aln ./16pkA0.aln --rr ./16pkA0.rr
```

#### Evaluate
```bash
./coneva-lite.pl -pdb ./16pkA.pdb -rr ./16pkA0.rr
```

