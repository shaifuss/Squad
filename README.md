# Squad
Task:
Take a dataset of paragraphs and questions. Find which paragraph is most likely to hold the answer to the first question 

Assumption:
The paragraph that contains the most significant words from the question is the most likely to contain the answer

Algorithm:
create a bag of words vocabulary for the set; words are stemmed, punctuation and stopwords are removed.

for each paragraph (also the question), create a bag of words vector, indicating which vocab words are 
present (and how many times).

compute inner product to compare how many words from the question appear in the paragraph.

print paragraph with highest word overlap
