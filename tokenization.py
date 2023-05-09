from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer
tokenizer  = TreebankWordTokenizer()


class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		#Fill in code here
		
		for sentence in text:
			tokenizedText.append(re.split(",|\s|-|'", sentence.strip()))

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		#Fill in code here
		
		for sentence in text:
			tokenizedText.append(tokenizer.tokenize(sentence.strip()))

		return tokenizedText