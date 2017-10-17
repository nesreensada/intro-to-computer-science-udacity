# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    
    i=0
    added=False
    while(i<len(index)):
        if keyword in index[i]:
             index[i][1].append(url)
             added=True
        i+=1
    if not added:
        index.append([keyword,[url]])
        



add_to_index(index,'udacity','http://udacity.com')
#print index
add_to_index(index,'computing','http://acm.org')
#print index
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


