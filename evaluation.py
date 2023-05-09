from sklearn.metrics import PrecisionRecallDisplay
from util import *

# Add your import statements here

from math import log2

class Evaluation():

	zero_recall_doc_ids = []

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here

		relevant_docs = 0

		for i in range(k):
			if(int(query_doc_IDs_ordered[i]) in true_doc_IDs):
				relevant_docs+=1

		precision = relevant_docs/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here

		num_queries = len(query_ids)
		total_precision = 0

		for i in range(num_queries):	
			true_doc_ids = []
			for qrel_dict in qrels:
				if(int(qrel_dict["query_num"])==int(query_ids[i])):
					true_doc_ids.append(int(qrel_dict["id"]))

			total_precision+=self.queryPrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_ids, k)

		meanPrecision = total_precision/num_queries
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		relevant_docs = 0

		for i in range(k):
			if(int(query_doc_IDs_ordered[i]) in true_doc_IDs):
				relevant_docs+=1

		recall = relevant_docs/len(true_doc_IDs)
		
		'''
		if(recall==0 and k==8):
			self.zero_recall_doc_ids.append(query_id)
		'''

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		self.zero_recall_doc_ids = []

		num_queries = len(query_ids)
		total_recall = 0

		for i in range(num_queries):	
			true_doc_ids = []
			for qrel_dict in qrels:
				if(int(qrel_dict["query_num"])==int(query_ids[i])):
					true_doc_ids.append(int(qrel_dict["id"]))

			total_recall+=self.queryRecall(doc_IDs_ordered[i], int(query_ids[i]), true_doc_ids, k)

		meanRecall = total_recall/num_queries

		'''
		print("Num of docs is : ",len(self.zero_recall_doc_ids))
		if(k==8):
			print("For k=8")
			print(self.zero_recall_doc_ids[:15])
		'''

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = 0

		#Fill in code here

		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

		if(precision>0 and recall>0):
			fscore = (2*precision*recall)/(precision+recall)
			
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here

		num_queries = len(query_ids)
		total_fscore = 0

		for i in range(num_queries):	
			true_doc_ids = []
			for qrel_dict in qrels:
				if(int(qrel_dict["query_num"])==int(query_ids[i])):
					true_doc_ids.append(int(qrel_dict["id"]))

			total_fscore+=self.queryFscore(doc_IDs_ordered[i], int(query_ids[i]), true_doc_ids, k)

		meanFscore = total_fscore/num_queries



		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, q_rels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here

		rel_value_dict = {}
		rel_docs_id = []
		DCGk = 0
		IDCGk = 0

		for qrel_dict in q_rels:
			if int(qrel_dict["query_num"]) == int(query_id):
				relevant_doc_id = int(qrel_dict["id"])
				rel_docs_id.append(int(relevant_doc_id))
				rel_value = 5-qrel_dict["position"]
				rel_value_dict[int(relevant_doc_id)] = rel_value

		for i in range(1, k+1):
			doc_id = int(query_doc_IDs_ordered[i-1])
			if doc_id in rel_docs_id:
				rel_value = rel_value_dict[doc_id]
				DCGk+=(rel_value)/log2(i+1)

		ideal_ordering = sorted(rel_value_dict.values(), reverse=True)
		num_rel_docs = len(ideal_ordering)
		for i in range(1, min(num_rel_docs,k)+1):
			IDCGk += (ideal_ordering[i-1])/log2(i+1)

		nDCG = DCGk/IDCGk
		
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here

		num_queries = len(query_ids)
		nDCG = 0

		for i in range(num_queries):	
			nDCG+=self.queryNDCG(doc_IDs_ordered[i], int(query_ids[i]), q_rels, k)

		meanNDCG = nDCG/num_queries

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here

		total_precision = 0
		num_rel_docs_ret = 0

		for i in range(k):
			if(query_doc_IDs_ordered[i] in true_doc_IDs):
				num_rel_docs_ret+=1
				precision = num_rel_docs_ret/(i+1)
				total_precision+=precision

		avgPrecision = total_precision/len(true_doc_IDs)

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here

		num_queries = len(query_ids)
		total_avg_precision = 0

		for i in range(num_queries):	
			true_doc_ids = []
			for qrel_dict in q_rels:
				if(int(qrel_dict["query_num"])==int(query_ids[i])):
					true_doc_ids.append(int(qrel_dict["id"]))

			total_avg_precision+=self.queryAveragePrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_ids, k)

		meanAveragePrecision = total_avg_precision/num_queries



		return meanAveragePrecision

