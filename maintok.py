from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
ex_text = "Hello Mr.smith, How are you doing today ? The weather is great and python is awesome... "
print(word_tokenize(ex_text))
print(sent_tokenize(ex_text))
for i in word_tokenize(ex_text):
    print (i)
