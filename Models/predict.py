def predict(marathi_text):

  #Removing Punctuations
  punctuations = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
  punctuation_removed_text = marathi_text
  for ele in marathi_text:
      if ele in punctuations:
          punctuation_removed_text = punctuation_removed_text.replace(ele, " ")

  #Tokenization
  tokenized_text = punctuation_removed_text.split(" ")
  #print(len(tokenized_text))

  #Removing Stopwords
  stopwords_collection = stopwords('mr')
  stopwords_removed_text = []
  for i in tokenized_text:
      if i not in stopwords_collection:
          stopwords_removed_text.append(i)

  #Remove Spaces
  final_text = []
  for i in stopwords_removed_text:
      if i != '':
          final_text.append(i)
  

  #Lemmatization
  nlp = stanza.Pipeline('mr') # This sets up a default neural pipeline in Marathi
  #nlp = stanza.Pipeline(lang='mr', processors='tokenize,mwt,pos,lemma')
  doc = nlp(marathi_text)
  #print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
  MainWord = []
  RootWord = []

  # Appending to MainWord
  for sent in doc.sentences:
      for word in sent.words:
          MainWord.append(word.text)

  # Appending to RootWord
  for sent in doc.sentences:
      for word in sent.words:
          RootWord.append(word.lemma)

  #Final Step
  Final_List = final_text
  k = 0
  for i in Final_List:
      m = 0
      if i in MainWord:
          for j in MainWord:
              if j == i:
                  Final_List[k] = RootWord[m]
                  break
              m = m + 1
      k = k + 1

  #Remove Blank Space
  for a in Final_List:
      if a == '':
          Final_List.remove(a)

  print(Final_List)

  df = get_POS(Final_List)
  # df
  # l2 = word_tokenize(list1)
  # #['मला', 'ताप', 'सर्दी', 'आणि', 'खोकला', 'आहे']
  # # print(l2)

  l=[]
  for i in range(len(df.Tags)):
      if 'NN' == df.Tags[i]:
          l.append(df.iloc[1][i])
  print('printing l')
  print(l)
  l3 = word_tokenize(l[0])
  print('printing l3')
  print(l3)
  data = {
    "Cancer": ['त्वचेची', 'लालसरपणा', 'गिळणे', 'त्रास', 'अपचनाचा','त्रास','रक्तस्त्रा','माझ्याकडे','ढेकूळ','थकव','जाणे','वेदना'],
    "Diarrhea" : ['स्टूलमध्ये','रक्त','स्टूलमध्ये','श्लेष्मा','पोटदुख','ताप','मळमळ'],
    "Covid" : ['चव','गमावणे','खोक','ताप','थकव','जाणे','श्वासोच्छवासाचा','त्रास'],
    "Malaria" : ['मळमळ','ताप','पोटदुख','डोक','खोक','उलटा'],
    "Stroke" : ['सुन्नपणा','पहाणे','समसा','चालणे','त्रास','बोलणे','अडचण'],
    "Diabetes" : ['लघवीची','समस्या','तहान','थकव','अंधुक','दृष्टी ','पाय','सुन्न','मुंग्य'],
    "Asthama" : ['धाप','छाती','घट्टपणणा','छाती','वेदना','झोपणे','त्रास'],
    "Depression" : ['अश्रू','दुःख','हताशपणा','न्यूनगंड'],
    "Fever": ['ताप','सर्दी','खोक'],
    "Tuberculosis" : ['थकव','वजन','ताप','खोक'],
    "AIDS" : ['ताप','डोकेदुखी','स्नायू','दुखण','घस','खवखवणे','पुरळ'],
    "Malaria" : ['ताप','डोकेदुखी','मळमळ','उलटी','पोटदुखी'],
    "Chickenpox" : ['ताप','थकव','डोकेदुखी','त्वचेवर','पुरळ'],
    "Piles" : ['रक्तस्त्राव','गुदद्वाराभोवती','वेदना','गुद्द्वार','खाज'],
  }

  score_l = []

  for i in data:
    score = 0
    k = 0
    for j in data[i]:
      while k < len(l3):
        # if get_sentence_similarity(l3[k], j, 'mr') == 1:
        if l3[k] == j:
          print(l3[k])
          score = score + 1
        k = k + 1
        # print(j)
    score_l.append(score)

  print('Score_List:',score_l)
  max_value = max(score_l) 
  print('Max value in score list', max_value)
  # max_index = score_l.index(max_value)
  max_indices=[]
  p = []
  j=0
  for i in score_l:
    if i==max_value:
        max_indices.append(j)
    j+=1
  for mi in max_indices:
    p.append([key for key in data.keys()][mi])
 
   return p