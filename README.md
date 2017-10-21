# PythonNLPCore

## Installation instructions:
Clone: git clone https://github.com/infobiac/PythonNLPCore.git

Copy the NLPCore.py and data.py files out of src into the directory you'd like to use. Due to the nature of the read/writes of the command line tool, pip does not work in this instance.

## Usage
You **must** have [Stanford's NLP Core installed first](https://stanfordnlp.github.io/CoreNLP/index.html). 
**NOTE: because we're utilizing the underlying annotator rather than the RelationExtractor annotator, you must include the 'relation' annotator as a property for both pipelines, as in the example below.**
Usage is simple:
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
**If the object wrappers are not working as expected, you can manipulate the XML tree that NLPCore returns directly. To do so, just call the tree attribute of the document that is returned by the annotate function.**
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

### Data: 
These are the objects that the xml tree are represented as. They are nested as follows:
* Document:
	* Sentence:
		* Token
		* Dependency
		* Entity
		* Relation

All have the tree_as_string method, which will print the xml tree associated with the object. 
#### Data attributes:
* Document:
	* tree: associated xml tree
	* sentences: list of associated sentences
* Sentence:
	* tree: associated xml tree
	* id
	* parse: the Sentence's parse
	* tokens: list of associated tokens
	* dependencies: list of associated dependencies
	* entitites: list of associated entities
	* relations: list of associated relations
* Token:
	* id
	* word
	* lemma
	* characterOffsetBegin
	* characterOffsetEnd
	* pos
	* ner

* Dependency:
	* overtype: the type of the overarching dependency
	* type: the actual type of the dependency
	* governor
	* dependent
	* govidx
	* depidx

* Entity:
	* id
	* type
	* value
	
* Relation:
	* id
	* entities: a list of the entities involved in the relation (usually two)
	* **probabilities**: a list of the potential relations with they're associated weights.
		
