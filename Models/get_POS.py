from collections import defaultdict
def get_POS(article):

    POS = {}

    word_tags = unigram_tagger.tag(article)
    for word, tag in word_tags:
        if tag not in POS:
            POS[tag] = [word]
        else:
            POS[tag].append(word)
    
    DF = {'Tags':[], 'Words':[], 'Count':[]}


    for k in POS:
        DF['Tags'].append(k)
        DF['Words'].append(" ".join(POS[k]))
        DF['Count'].append(len(POS[k]))
    
    return pd.DataFrame(DF)