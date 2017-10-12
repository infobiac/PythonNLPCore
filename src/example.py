from NLPCore import NLPCoreClient

text = ["Bill Gates works at Microsoft.", "Sergei works at Google."]

#path to corenlp
client = NLPCoreClient('/Users/christopherimann/Downloads/stanford-corenlp-full-2017-06-09')
properties = {
	"annotators": "tokenize,ssplit,pos,lemma,ner,parse,relation",
	"parse.model": "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
	"ner.useSUTime": "0"
	}
doc = client.annotate(text=text, properties=properties)
print(doc.sentences[0].relations[0])
print(doc.tree_as_string())