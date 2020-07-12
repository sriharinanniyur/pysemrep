# representation of SurfaceElement class.
from abc import ABC, abstractmethod

class SurfaceElement(ABC):
	def getIndex(self):
		pass
	def setIndex(self, i):
		pass
	def getSentence(self):
		pass
	def setSentence(self, s):
		pass
	def getDocument(self):
		pass
	def getText(self):
		pass
	def setText(self, t):
		pass
	def getLemma(self):
		pass
	def getPos(self):
		pass
	def setPos(self, p):
		pass
	def getCategory(self):
		pass
	def isVerbal(self):
		pass
	def isNominal(self):
		pass
	def isAdjectival(self):
		pass
	def isCoordConj(self):
		pass
	def isAdverbial(self):
		pass
	def isDeterminer(self):
		pass
	def isPrepositional(self):
		pass
	def isPredicate(self):
		pass
	def isPronomial(self):
		pass
	def isRelativePronoun(self):
		pass
	def isAlphanumeric(self):
		pass
	def getHead(self):
		pass
	def toWordList(self, cat=None): # cat is optional str arg
		pass
	def hasSemantics(self):
		pass
	def writeSemantics(self):
		pass
	def filterSemanticsByClass(self, clazz):
		pass
	def filterByEntities(self):
		pass
	def filterByPredicates(self):
		pass
	def filterByTerms(self):
		pass
	def filterByRelations(self):
		pass
	def getHeadSemantics(self):
		pass
	def containsAnyToken(self, tokens):
		pass
	def containsAnyLemma(self, lemmas):
		pass
	def containsToken(self, token):
		pass
	def containsLemma(self, lemma):
		pass

