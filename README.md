# code2cap
UCLA CS 269 Final Project

The aim of the project is to  build a tool that can automatically produce a concise natural language summary 
of source code in the form of method name predictions.

## Directories & descriptions

| Directory | Description |
|-----------|-------------|
| notebooks | Contains the notebook artifacts used to run the process the data, train, and translate. The notebooks act as logs of training, showing the moving train acc, periodic validation acc, and runtimes involved for each experiment. |
| data | Contains the processed dataset of function declaration+body, description, and generated ASTs |
| pred | Contains the predictions output from various tests conducted to evaluate the importance of different prep-processing steps |
