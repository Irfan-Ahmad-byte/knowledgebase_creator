"""
Module for creating a knowledgebase from the given data
Author: Irfan Ahmad (github.com/irfan-ahmad-byte)
"""


class KnowledgebaseCreator:
    """
    Class for creating a knowledgebase from the given data
    """

    def __init__(self, text_splitter, knowledgebase_builder):
        """
        Constructor for KnowledgebaseCreator
        :param text_splitter: TextSplitter object
        :param knowledgebase_builder: KnowledgebaseBuilder object
        """
        self.text_splitter = text_splitter
        self.knowledgebase_builder = knowledgebase_builder

    def create_knowledgebase(self, data):
        """
        Creates a knowledgebase from the given data
        :param data: list of strings
        :return: Knowledgebase object
        """
        sentences = self.text_splitter.split_text(data)
        knowledgebase = self.knowledgebase_builder.build_knowledgebase(sentences)
        return knowledgebase