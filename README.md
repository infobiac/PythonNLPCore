# PythonNLPCore

## Installation instructions:
Clone: git clone https://github.com/infobiac/PythonNLPCore.git

Copy the NLPCore.py and data.py files out of src into the directory you'd like to use. Due to the nature of the read/writes of the command line tool, pip does not work in this instance.

**Note:** This is an optional way to interact with the underlying library. All it does is write options to a file, call the command line tool with that file, and then read in the resulting file. If you would like to modify it or not use it at all, or just take the command that runs the underlying program, please do so; this is meant to just be a starting point.

## How it works:
This is a very lightweight wrapper file for calling the underlying CoreNLP command line tool (as per the usage here: https://stanfordnlp.github.io/CoreNLP/cmdline.html). All it does is create a properties file and an input file based on what is passed too it, then it runs the command line tool with these as arguments. After the command line tool has finished running, it will try read the outputed xml file into objects for easier manipulation. You can (and should if you want) modify any aspect of this to suit your needs. After running the tool for the first time please read through the outputed xml file (by default it is named input.txt.xml) in order to understand what CoreNLP outputs, and read the cmdline documentation if you have any issues.

## Usage
You **must** have [Stanford's NLP Core installed first](https://stanfordnlp.github.io/CoreNLP/index.html). 

**NOTE: We have two pipelines.**

Pipeline 1: tokenize,ssplit,pos,lemma,ner

Pipeline 2: tokenize,ssplit,pos,lemma,ner,parse,relation

Usage is simple:
~~~~
from NLPCore import NLPCoreClient

text = ["Bill Gates works at Microsoft.", "Sergei works at Google."] # In actuality, you will want to input the cleaned webpage for the first pipeline, and a list of candidate sentences for the second.

#path to corenlp
client = NLPCoreClient('/path/to/stanford-corenlp-full-2017-06-09')
properties = {
	"annotators": "tokenize,ssplit,pos,lemma,ner,parse,relation", #Second pipeline; leave out parse,relation for first
	"parse.model": "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", #Must be present for the second pipeline!
	"ner.useSUTime": "0"
	}
doc = client.annotate(text=text, properties=properties)
print(doc.sentences[0].relations[0])
print(doc.tree_as_string())
~~~~

For a list of all attributes, see src/data.py. To understand the structure of the tree at any stage, use the tree_as_string() function.
**If the object wrappers are not working as expected, you can manipulate the XML tree that NLPCore returns directly. To do so, just call the tree attribute of the document that is returned by the annotate function, or if that isn't working read input.txt.xml.**

You may need to pass sentences to the second pipeline by reconstructing them out of tokens, depending on how you decide to interact with the command line. In order to do so, isolate your candidate sentences from the first pipeline and look over them to reconstruct them by accessing each token's word:
~~~
newsentence = ""
for x in doc.sentences[0].tokens:
	newsentence += " " + x.word
print(newsentence)
~~~
## Rough Documentation:
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
		
