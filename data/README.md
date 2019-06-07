# Data

## Java Method Name Prediction Data
Due to the rather large size of the datasets and the 100MB limitation Github enforces, we've provided a [link](https://drive.google.com/open?id=1mJRuS_Z0MMYmwWO09LrSXC5idqdgCVCJ) to the preprocessed Java datasets. Files prefixes (eg. src and tgt) indicate the OpenNMT flags to use with each. 

NOTE: preprocessed here means:
- The methods are split between method name and method body AND both have been tokenized and subtokenized
- The method name has been stripped of parameters
- The methody body has been converted to an AST with several paths sampled between terminal nodes

### Inputs (X)
- src.train.txt
- src.val.txt
- src.test.txt

### Targets (Y)
- tgt.train.txt
- tgt.val.txt
- tgt.test.txt

Source: [code2seq](https://github.com/tech-srl/code2seq#datasets)
