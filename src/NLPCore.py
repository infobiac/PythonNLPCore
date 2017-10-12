import subprocess
import os

from data import Document, Sentence, Token, Relation

class NLPCoreClient:
	def __init__(self, path, default_annotators='tokenize,ssplit,pos,lemma,ner,parse,relation'):

		sp = subprocess.Popen(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		t = sp.communicate()
		sp.wait()
		java = False

		for x in t:
			if "Runtime Environment" in str(x):
				java = True
				break

		if not java:
			print("Please make sure you have Java installed")
			raise("Java not installed")

		self.path = path
		self.default_annotators = default_annotators

	def annotate(self, text, properties):
		with open('input.txt', 'w') as t:
			for x in text:
				t.write("{}\n".format(x))

		with open('props.properties', 'w') as props:
			if 'annotators' not in properties:
				props.write("annotators = {}\n".format(self.default_annotators))
			props.write("file = input.txt\n")
			for key, value in properties.items():
				props.write("{} = {}\n".format(key, value))

		path = "{}/*".format(self.path)
		args = []
		try:
			sp = subprocess.Popen(['java', "-cp", path, "-Xmx2g", "edu.stanford.nlp.pipeline.StanfordCoreNLP", "-props", "props.properties"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			sp.wait()
		except java.lang.OutOfMemoryError:
			raise("Out of Memory")

		return Document()
