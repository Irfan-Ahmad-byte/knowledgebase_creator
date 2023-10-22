# module which builds knowledgebase from the given data
# Author: Irfan Ahmad (github.com/irfan-ahmad-byte)

# this module applies the knowledgebase creating strategy used in a notebook in the
# parent dir of this sub-module

# it uses a text splitter to split the text into sentences and then applies the
# knowledgebase creating strategy to create the knowledgebase
# it stores the vector data into chromadb


from knowledgebase.knowledge_builder.knowledgebase_creator import KnowledgebaseCreator