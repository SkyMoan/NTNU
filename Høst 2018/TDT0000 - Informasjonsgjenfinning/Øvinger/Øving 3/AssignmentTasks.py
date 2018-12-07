import random;
import codecs;

#Gensim and ntlk related imports
import nltk;x
import string;
import gensim;
from nltk.stem.porter import PorterStemmer


# -- FUNCTIONS --
#These are all the functions needed to use the steps in the 4 Tasks below.


# Takes in a file and divides it into paragraphs.
def makeParagraphs(file):
    paragraph = '';
    paragraphs = [];

    for line in f.readlines():
        if not line.strip():
            if (paragraph != ""):
                paragraphs.append(paragraph);
                paragraph = "";
        else:
            paragraph += line
    return paragraphs;

#Removes a paragraph from the array if it contains a given word.
def removeWord(word, array):
    tempArray = [];
    for item in array:
        if word not in item:
            tempArray.append(item);
    return tempArray;


#Tokensizes an array, seprates every word in a given sentence to a separate element
def tokenize(array):
    tempArray = [];
    for item in array:
        tempArray.append(nltk.word_tokenize(item))
    return tempArray;

#Removes punctation and whitespaces
def removePunctuationAndLower(array):
    remove = string.punctuation + "\n\r\t";
    tempArray = [];
    temp_Paragraph = [];
    if isinstance(array[0], list):
        for i in range(len(array)):
            for j in range(len(array[i])):
                word = array[i][j];
                new_word = ''
                for char in word:
                    if char not in remove:
                        new_word += char;
                if new_word != '':
                    temp_Paragraph.append(new_word.lower());
            tempArray.append(temp_Paragraph);
            temp_Paragraph = [];
    else:
        for i in range(len(array)):
            word = array[i]
            new_word = ''
            for char in word:
                if char not in remove:
                    new_word += char;
            if new_word != '':
                tempArray.append(new_word.lower());
    return tempArray;

#Stemming function for arrays, uses the PortStemmer function
def stem(array):
    stem = PorterStemmer();
    if isinstance(array[0], list):
        for i in range(len(array)):
            for j in range(len(array[i])):
                array[i][j] = stem.stem(array[i][j]);
    else:
        for i in range(len(array)):
            array[i] = stem.stem(array[i]);

    return array;

#Returns the ID of the stopWords given
def getStopWordIDs(stopwords, dictionary):
    stopWordIDs = [];
    for word in stopwords:
        try:
            stopWordIDs.append(dictionary.token2id[word])
        except:
            pass
    return stopWordIDs;

#Converts an array of stemmed words into a "Bag of Words"
def convertToBagOfWords(array, dictionary):
    vctr = [];
    for p in array:
        vctr.append(dictionary.doc2bow(p))
    return vctr;



#Formats a query by splitting it, stemming it, and remove punctations and makes it lower case.
def makeQuery(query):
    query = query.split(" ");
    query = removePunctuationAndLower(query);
    query = stem(query);
    return query


# --------- TASKS ---------


# -- TASK 1 --

#1.0
random.seed(123)

#1.1
f = codecs.open("pg3300.txt", "r", "utf-8")

# 1.2 Dividing the file into paragraphs
paragraphs = makeParagraphs(f);

# 1.3 Remove paragraphs with the word 'Gutenberg'
GutenbergRemoved = removeWord("Gutenberg", paragraphs);

# 1.4 Tokenizing the paragrapsh
tokenized = tokenize(GutenbergRemoved);

# 1.5 Removing punctuation and white characters ("\n\r\t"). Then convert everything to lowercase
noWhiteSpaceAndPunctations = removePunctuationAndLower(tokenized);

# 1.6 Creating a stemmed array
stemmedArray = stem(noWhiteSpaceAndPunctations);





# -- TASK 2 --


# 2.1 Create dictionary from our stemmed list
dictionary = gensim.corpora.Dictionary(noWhiteSpaceAndPunctations);

# 2.1 Get the IDs for the stop words
stopFile = codecs.open("stopWords.txt", "r", "utf-8").read().split(",");

# Removing punctuation and whitespaces
stopFile = removePunctuationAndLower(stopFile);

# Getting the IDs for the stopwords
stopWordID = getStopWordIDs(stopFile, dictionary);

# Filtering out the stopwords
dictionary.filter_tokens(stopWordID);

# 2.2 Converting our list to a bag of words (corpus).
Corpus = convertToBagOfWords(noWhiteSpaceAndPunctations, dictionary);





# -- TASK 3 --


# 3.1 Building a TD-IDF model using corpus
TFIDFmodel = gensim.models.TfidfModel(Corpus);

# 3.2 Mapping corpus in to TF-IDF weights
tfidf_corpus = TFIDFmodel[Corpus];

# 3.3 MatrixSimilarity object that lets us calculate similarities between paragraphs and queries:
matrixSimimlarity = gensim.similarities.MatrixSimilarity(tfidf_corpus);

# 3.4 Repeat the above procedure for LSI model with TF-IDF weights.
lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100);

lsi_corpus = lsi_model[tfidf_corpus];

lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus);

# 3.5 Report and try to interpret first 3 LSI topics
print("The first three LSI topics:\n" + str(lsi_model.show_topics(3,3)) + "\n");






# -- TASK 4 --


# 4.1 For the following query: "What is the function of money?"
# apply all necessary transformations: remove punctuations, tokenize, stem and convert to BOW representation in a way similar as in Part 1

query = "What is the function of money?";
query = makeQuery(query);
query = dictionary.doc2bow(query);

# 4.2 Convert BOW to TF-IDF representation, then Report TF-IDF weights.

query_tfidf = TFIDFmodel[query];
print("For the query: 'How much taxes influence Economics?' The TFIDF weights are:");
print(str(dictionary.get(query_tfidf[0][0])) + ": " + str(query_tfidf[0][1]) + ", " + str(dictionary.get(query_tfidf[1][0])) + ": " + str(query_tfidf[1][1]));

# 4.3 Report top three the most relevant paragraphs for the query "What is the function of money?"according to TF-IDF model.
# displayed paragraphs should be in the original form; before processing, but truncated up to first 5 lines).

print("\nThe top three paragraphs based on the weights are:");

docSim = enumerate(matrixSimimlarity[query_tfidf]);
docs = sorted(docSim, key=lambda kv: -kv[1])[:3];

for doc in docs:
    text = "\n[Paragraph {0}]\n {1}".format(doc[0], paragraphs[doc[0]]);
    print(text);

# 4.4  Convert query TF-IDF representation for the query "What is the function of money?",
# into LSI-topics representation (weights). Report the top three topics with the most significant
# weights and top three the most relevant paragraphs according to LSI model.
# Compareretrieved paragraphs with the paragraphs found for TF-IDF model.
print("\nFor the query: 'How much taxes influence Economics?' The top three topics are:");


lsi_query = lsi_model[query_tfidf];
topics = sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3];

for i in range(len(topics)):
    text = "\n[Topic {0}]\n {1}".format(topics[i][0], lsi_model.print_topic(topics[i][0]));
    print(text);


print("\nAnd the top three paragraphs according to the LSI model are:");
docSim = enumerate(lsi_matrix[lsi_query])
docs = sorted(docSim, key=lambda kv: -kv[1])[:3];

for doc in docs:
    text = "\n[Paragraph {0}]\n {1}".format(doc[0], paragraphs[doc[0]]);
    print(text);