# PythonNLPCore

## Installation instructions:
Clone: git clone https://github.com/infobiac/PythonNLPCore.git
CD: cd PythonNLPCore
Install: pip install -e .

## Usage
You must have Stanford's NLP Core installed first. Usage is simple:
'''
from NLPCore import NLPCoreClient

text = ["Bill Gates works at Microsoft.", "Sergei works at Google."]

#path to corenlp
client = NLPCoreClient('/path/to/stanford-corenlp-full-2017-06-09')
properties = {
	"annotators": "tokenize,ssplit,pos,lemma,ner,parse,relation",
	"parse.model": "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
	"ner.useSUTime": "0"
	}
doc = client.annotate(text=text, properties=properties)
print(doc.sentences[0].relations[0])
print(doc.tree_as_string())
'''

For a list of all attributes, see src/data.py. To understand the structure of the tree at any stage, use the tree_as_string() function.