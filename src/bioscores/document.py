# Document representation class.

class Document:
    id = 0
    sentences = []
    topics = []
    surfaceElementFactory = None
    semanticItemFactory = None
    # public Document(String id, String text) {
    #     this.id = id;
    #     this.text = text;
    # semanticItems = newHashMap <> ();
    # }
    def __init__(self):
        self.id = id
        self.text = text
        self.semanticItems = []

    def __init__(self, id,  text, sentences):
        self.id = id
        self.text = text
        self.sentences = sentences
"""
Creates a <code>Document</code> object with the full parse tree.
"""
    def __init__(self, id, text, sentences, documentTree):
        self.id = id
        self.text = text
        self.sentences = sentences
        self.documentTree = documentTree

#
# public
# Document(String
# id, String
# text, List < Sentence > sentences, Tree
# documentTree,
# Map < Class <? extends
# SemanticItem >, LinkedHashSet < SemanticItem >> semanticItems) {
#     this(id, text, sentences, documentTree);
# this.semanticItems = semanticItems;
# }
#     def __init__(self, id, text, sentences, documentTree, )

    def getId(self):
        return self.id

    def getDocumentTree(self):
        return self.documentTree

    def getSemanticItems(self):
        return self.semanticItems

    def getSentences(self):
        return self.sentences

    def setSentences(self, sentences):
        self.sentences = sentences

    def addSentence(self, sentences):
        if not self.sentences:
            self.sentences = []
        self.sentences.append(sentences)

    def getText(self):
        return self.text

    def getSections(self):
        return self.sections

    def setSections(self):
        return self.sections = sections

    def addSections(self, section):
        if not self.sections:
            self.sections = []
        self.sections.append(section)

    def getTopics(self):
        return self.topics

    def setTopics(self, topics):
        self.topics = topics

    def addTopic(self, topics):
        if not topics:
            self.topics = []
        self.topics.append(topics)

    def getSurfaceElementFactory(self):
        if not self.surfaceElementFactory:
            self.surfaceElementFactory = SurfaceElementFactory()
        return self.surfaceElementFactory

  






