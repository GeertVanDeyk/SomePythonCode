import spacy
from spacy import displacy



nlp = spacy.load('en_core_web_sm')

introduction_text = "Hi, I'm Johnny Cash."
introduction_text1 = "Call me Ishmael."

introduction_doc = nlp(introduction_text)
displacy.serve(introduction_doc)

  

sentences = list(introduction_doc.sents)




print(len(sentences))
for sentence in sentences:
    print(sentence)
    
for token in introduction_doc:
    print(token.idx, token, token.lemma_, token.doc ,token.dep_)
    
    
         

