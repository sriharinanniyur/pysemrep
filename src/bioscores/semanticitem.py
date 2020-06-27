# representation of SemanticItem interface.
from abc import ABC, abstractmethod

class SemanticItem(ABC):
    def getID(self):
        pass
    def setID(self, s):
        pass
    def getAllSemTypes(self):
        pass
    def getType(self):
        pass
    def setType(self, sem):
        pass
    def getSpan(self):
        pass
    def getDocument(self):
        pass
    def toShortString(self):
        pass
    def toStandoffAnnotation(self):
        pass
    def toXml(self):
        pass
    def getOntology(self):
        pass
    def ontologyEquals(self, obj):
        pass
    def getFeatures(self):
        pass
    def setFeatures(self, features):
        pass
    def addFeature(self, name, feature):
        pass
