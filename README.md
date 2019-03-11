# Squad
finds the paragraph most likely to contain the answer to the first question in the set, based on word overlap
creates a bag of words vocabulary for the set; words are stemmed, punctuation and stopwords are removed
for each paragraph (also the question), creates a bag of words vector, indicating which vocab words are 
present in the paragraph
uses inner product to compare how many words from the question appear in the paragraph
prints paragraph with highest word overlap