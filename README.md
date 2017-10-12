# PythonNLPCore

## Installation instructions:
Clone: git clone https://github.com/infobiac/PythonNLPCore.git

CD: cd PythonNLPCore

Install: pip install -e .

## Usage
You **must** have [Stanford's NLP Core installed first](https://stanfordnlp.github.io/CoreNLP/index.html). Usage is simple:
~~~~
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
~~~~

For a list of all attributes, see src/data.py. To understand the structure of the tree at any stage, use the tree_as_string() function.
**If the object wrappers are not working as expected, you can manipulate the XML tree that NLPCore returns directly. To do so, just call the tree attribute of the document that is returned**
## Documentation:
### NLPCoreClient:
* Parameters:
	* Takes a path to the location of the unzipped stanford-corenlp folder
* Has following method:
	* Annotate - create a new annotation

### Annotate:
* Parameters:
	* text: text to annotate. List of sentences.
	* properties: a dictionary of properties to pass to NLPCore. Default annotators: "tokenize,ssplit,pos,lemma,ner,parse,relation"
* Returns a Document object, which is the root of the tree returned by the NLP Core client
