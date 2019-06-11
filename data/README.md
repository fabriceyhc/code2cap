# Data

## Method Name Prediction Data

### Java
Due to the rather large size of the datasets and the 100MB limitation Github enforces, we've provided a [link](https://drive.google.com/open?id=1mJRuS_Z0MMYmwWO09LrSXC5idqdgCVCJ) to the preprocessed Java datasets. Files prefixes (eg. src and tgt) indicate the OpenNMT flags to use with each. 

NOTE: preprocessed here means:
- The methods are split between method name and method body AND both have been tokenized and subtokenized
- The method name has been stripped of parameters
- The methody body has been converted to an AST with several paths sampled between terminal nodes

#### Inputs (X)
- src.train.txt
- src.val.txt
- src.test.txt

#### Targets (Y)
- tgt.train.txt
- tgt.val.txt
- tgt.test.txt

Source: [code2seq](https://github.com/tech-srl/code2seq#datasets)

### Python
The dataset for Python was preprocessed to obtain a training dataset with sources consisting of cleaned ASTs and targets being the respective function names. The training, test and validation sets can be found [here](https://drive.google.com/drive/folders/1xzJUoq8nnCYjWnbXQnS7bzmuaFuYi0h4?usp=sharing).

#### Inputs (X)
- in_train.txt
- in_val.txt
- in_test.txt

#### Targets (Y)
- decl_train.txt
- decl_val.txt
- decl_test.txt

#### AST
`
Module(body=[FunctionDef(name='_load_file', args=arguments(args=[Name(id='filename', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='fp', ctx=Store())], value=Call(func=Name(id='open', ctx=Load()), args=[Name(id='filename', ctx=Load()), Str(s='rb')], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='source', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='read', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None), op=Add(), right=Str(s='\n'))), TryExcept(body=[Assign(targets=[Name(id='co', ctx=Store())], value=Call(func=Name(id='compile', ctx=Load()), args=[Name(id='source', ctx=Load()), Name(id='filename', ctx=Load()), Str(s='exec')], keywords=[], starargs=None, kwargs=None))], handlers=[ExceptHandler(type=Name(id='SyntaxError', ctx=Load()), name=None, body=[Print(dest=Attribute(value=Name(id='sys', ctx=Load()), attr='stderr', ctx=Load()), values=[Str(s='>>Syntax \terror \tin'), Name(id='filename', ctx=Load())], nl=True), Raise(type=None, inst=None, tback=None)])], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Return(value=Name(id='co', ctx=Load()))], decorator_list=[])])
`
#### AST Cleaned
`
module body functiondef name load file args arguments args name id filename ctx param vararg none kwarg none defaults body assign targets name id fp ctx store value call func name id open ctx load args name id filename ctx load str s rb keywords starargs none kwargs none assign targets name id source ctx store value binop left call func attribute value name id fp ctx load attr read ctx load args keywords starargs none kwargs none op add right str s n tryexcept body assign targets name id co ctx store value call func name id compile ctx load args name id source ctx load name id filename ctx load str s exec keywords starargs none kwargs none handlers excepthandler type name id syntaxerror ctx load name none body print dest attribute value name id sys ctx load attr stderr ctx load values str s syntax terror tin name id filename ctx load nl true raise type none inst none tback none orelse expr value call func attribute value name id fp ctx load attr close ctx load args keywords starargs none kwargs none return value name id co ctx load decorator list
`
