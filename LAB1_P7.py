import nltk
#nltk.download ()
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
#a. Read the data from a file
file = open("nlp_input.txt",'r')
loaded=file.read()

#b. Tokenize the text into words and apply lemmatization technique on each word
 # Tokenization
token = nltk.word_tokenize(loaded)
# Lemmatization
lemmatizer=WordNetLemmatizer()
modified=lemmatizer.lemmatize(loaded)
#Find all the trigrams for the words 
n=3
ngrams = zip(*[token[i:] for i in range(n)])
Trigrams=[" ".join(ngram) for ngram in ngrams]
#d. Extract the top 10 of the most repeated trigrams based on their count
mostrepeatednum=10
mostrepeated=FreqDist(Trigrams).most_common(mostrepeatednum)
print(mostrepeated)
#f. Find all the sentences with the most repeated tri-grams
#convert the repeated words into dictionary
reformalize=dict(mostrepeated)
#tokanize in sentences
token2 = nltk.sent_tokenize(loaded)
#g. Extract those sentences and concatenate
sent=[]
for i in range (mostrepeatednum):
    for key, value in reformalize.items(): 
            sent.append([sentence + '.' for sentence in token2 if key in sentence])
#to faltten the list to remove the duplicant sentences 
flat_list = [item for sublist in sent for item in sublist]
#remove the duplication
final_list = [] 
for num in flat_list: 
    if num not in final_list: 
        final_list.append(num) 
#h. Print the concatenated result
print(len(final_list))   
print(final_list)