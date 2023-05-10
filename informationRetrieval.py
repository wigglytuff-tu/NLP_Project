# Add your import statements here
import operator
import numpy as np
from numpy import dot
from numpy.linalg import norm
from sklearn.decomposition import TruncatedSVD
from tqdm import tqdm

class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None

		#Fill in code here
		self.index = index
		list_of_words = []

		for doc in docs:
			for sentence in doc:
				for word in sentence:
					list_of_words.append(word)   #Can have repetition of words 

		self.terms = list(set(list_of_words))

		df = np.zeros(len(self.terms)) # df(i): number of docs containing term i, used for calculating IDF 
		TDf = np.zeros([len(self.terms),len(docs)]) #term-document matrix
		
		for j, doc in tqdm(enumerate(docs)):       # iterate over documents
			for k, sentence in enumerate(doc):  # iterate over sentences for a document
				for word in sentence:
					try:
						TDf[self.terms.index(word),j] += 1
					except:
						x_skip = 0
        
		df = np.sum(TDf > 0, axis=1)
		self.IDF = np.log(len(docs)/df)            
		self.doc_weights = np.zeros([len(self.terms),len(docs)])
        
		for i in range(len(self.terms)):
			self.doc_weights[i,:] = self.IDF[i]*TDf[i,:]   # vector weights for each document 
		
		print(self.doc_weights.shape)
		self.tsvd = TruncatedSVD(n_components=250)
		self.tsvd.fit(self.doc_weights.T)
		tsvd_mat = self.tsvd.transform(self.doc_weights.T)              
        
		index = {key: None for key in docIDs}  # initialize dictionary with keys as doc_IDs
       
		for j in range(len(docs)): 
			index[docIDs[j]] = tsvd_mat[j,:]   # update dict-values with weight vector for corresponding docIDs  

		self.index = index

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		TQ_matrix = np.zeros([len(self.terms),len(queries)]) # term frequency matrix (for each query in list queries)
        
		for i, unique_word in enumerate(self.terms):
			for j, query in enumerate(queries):       # iterate over all queries
				for k, sentence in enumerate(query):  # iterate over sentences for a query
					for word in sentence:
						if unique_word == word:
							TQ_matrix[i,j] += 1 

		self.query_weights = np.zeros([len(self.terms),len(queries)])
        
		for i, unique_word in enumerate(self.terms):
			self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]  # vector weights for each query  
        
		id_docs = list(self.index.keys())
                
		doc_IDs_ordered  = list(range(len(queries)))

		tsvd_queries = self.tsvd.transform(self.query_weights.T)

		for j in range(len(queries)):
			dict_cosine = {key: None for key in id_docs} # given ONE query, stores cosine measures for between query and all docs
			for doc_id, doc_vector in self.index.items():
				a = doc_vector
				b = tsvd_queries[j,:]
				dict_cosine[doc_id] = dot(a,b)/(norm(a)*norm(b))
                 
			dc_sort = sorted(dict_cosine.items(),key = operator.itemgetter(1),reverse = True)
			doc_IDs_ordered[j] = [x for x, _ in dc_sort]
	
		return doc_IDs_ordered
