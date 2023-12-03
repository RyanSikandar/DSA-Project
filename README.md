# DSA-Project
End Semester Project for DSA:
A search engine that takes inspiration from Google.

Currenlty, all the articles of the dataset have been added to a single json file and the ids of the articles have been changed from the original 'source-date-title' ids to integral numbers ranging from 1 to the total number of articles. This would help in making indexing simpler.

Moreover, preprocessing has been done to a significant extent as well. 


The inverted index in this branch is a nested dictionary with word ids as the keys of the outer dictionary and document ids as the key of the inner dictionary, and the values of the inner keys are the hitlists corresponding to that particular in that particular document.
