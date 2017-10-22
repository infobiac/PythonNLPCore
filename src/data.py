import xml.etree.ElementTree as ET
from xml.dom import minidom

class Document:
	def __init__(self):
		self.tree = ET.parse("input.txt.xml").getroot()[0][0]
		self.sentences = []
		for sentence in self.tree:
			self.sentences.append(Sentence(sentence))


	def tree_as_string(self):
		rough_string = ET.tostring(self.tree, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = ""
		for x in self.sentences:
			st += x
		final = "Document containing: [{}]".format(st)
		return final


class Sentence:
	def __init__(self, sentence):
		self.tree = sentence
		self.id = sentence.attrib['id']
		if len(sentence.findall('parse')) != 0:
			self.parse = sentence.findall('parse')[0].text
		else:
			self.parse = None
		self.tokens = []
		self.dependencies = []
		self.entities = []
		self.relations = []
		for x in self.tree:
			if x.tag == 'tokens':
				for y in x:
					self.tokens.append(Token(y))
			if x.tag == 'dependencies':
				for y in x:
					self.dependencies.append(Dependency(y, x.attrib['type']))
		try:
			if self.parse:
				for x in self.tree.findall("MachineReading")[0]:
					if x.tag == 'entities':
						for y in x:
							self.entities.append(Entity(y, self.tokens))
				for x in self.tree.findall("MachineReading")[0]:	
					if x.tag == 'relations':
						for y in x:
							self.relations.append(Relation(y, self.tokens, self.entities))
		except:
			self.relations.append([])


	def tree_as_string(self):
		rough_string = ET.tostring(self.tree.getroo, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = ""
		for x in self.tokens:
			st += str(x)
		for x in self.dependencies:
			st += str(x)
		for x in self.entities:
			st += str(x)
		for x in self.relations:
			st += str(x)
		final = "Sentence containing: [{}]".format(st)
		return final


class Token:
	def __init__(self, token):
		self.id = token.attrib['id']
		self.word = token.findall('word')[0].text
		self.lemma = token.findall('lemma')[0].text
		self.characterOffsetBegin = token.findall("CharacterOffsetBegin")[0].text
		self.characterOffsetEnd = token.findall("CharacterOffsetEnd")[0].text
		self.pos = token.findall("POS")[0].text
		self.ner = token.findall("NER")[0].text

	def tree_as_string(self):
		rough_string = ET.tostring(self.tree.getroo, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = "Token with id: {} representing word: {}. ".format(self.id, self.word)
		return st


class Dependency:
	def __init__(self, dependency, overtype):
		self.overtype = overtype
		self.type = dependency.attrib['type']
		self.governor = dependency.findall("governor")[0].text
		self.govidx = dependency.findall("governor")[0].attrib['idx']
		self.dependent = dependency.findall("dependent")[0].text
		self.depidx = dependency.findall("dependent")[0].attrib['idx']

	def tree_as_string(self):
		rough_string = ET.tostring(self.tree.getroo, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = "Dependency of overarching type {} and type {} with governor: {}, dependent: {}. ".format(self.overtype, self.type, self.governor, self.dependent)
		return st

class Entity:
	def __init__(self, entity, tokens):
		self.id = entity.attrib['id']
		self.type = ' '.join(entity.text.split())
		self.value = None
		for x in tokens:
			if x.id == entity.findall("span")[0].attrib['end']:
				self.value = x.word
				break

	def tree_as_string(self):
		rough_string = ET.tostring(self.tree.getroo, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = "Entity with ID: {}, value: {}, and type: {}. ".format(self.id, self.value, self.type)
		return st

class Relation:
	def __init__(self, relation, tokens, ents):
		self.id = relation.attrib['id']
		self.entities = []
		for x in relation.findall('arguments')[0]:
			for y in ents:
				if x.attrib['id'] == y.id:
					self.entities.append(y)
		self.probabilities = dict()
		for x in relation.findall('probabilities')[0]:
			self.probabilities[x.findall('label')[0].text] = x.findall('value')[0].text

	def tree_as_string(self):
		rough_string = ET.tostring(self.tree.getroo, "utf-8", method="xml")
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(newl='')

	def __str__(self):
		st = ""
		for x in self.entities:
			st = st + str(x)
		final = "Relation with id: {}, made up of the following entities: [{}], and the following probabilities:[{}]. ".format(self.id, st, self.probabilities)
		return final
