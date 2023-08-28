#Here, we have tried to get Data from a very complex PDF
import fitz
import pandas as pd
import os
list_session_title = []
list_article_title = []
list_disclosure = []
list_text = []
list_authors = []
list_category = []
list_type = []
list_sub_category = []
li_affiliations = []
li1 = ['1.pdf']
for pdf_name in li1:
    print('PDF COUNT - ',pdf_name)
    pdf_name = str(pdf_name)
    pdf_name = pdf_name
 #   pdf_name = repr(pdf_name)
    doc = fitz.open(pdf_name)
    count = 0
    actual = ''
    while True:
        try:
            the_page = doc[count]
            words = the_page.get_text("words")
            line_dict = {}
            words.sort(key=lambda w: w[0])
            for w in words:
                y1 = round(w[3], 1)
                word = w[4]
                line = line_dict.get(y1, [])
                line.append(word)
                line_dict[y1] = line
            lines = list(line_dict.items())
            lines.sort()
            lat = "\n".join([" ".join(line[1]) for line in lines])
            actual += str(lat)
        except:
            break
        count+=1

    txt1 = actual.strip()
    txt1 = txt1.replace('2023 Congress of the Schizophrenia International Research Society\n', '')
    txt1 = txt1.replace('2023 Congress of the Schizophrenia International Research Society','')

    session_title = txt1.split('\nSubmission ID',1)
    session_title = session_title[0]
    if 'Submission Type' in txt1:
        type1 = txt1.split('\nSubmission Type',1)
        type1 = type1[1]
        if '\nTopic' in type1:
            type1 = type1.split('\nTopic',1)
            type1 = type1[0]
        else:
            type1 = type1.split('\nSubmitter',1)
            type1 = type1[0]
    else:
        type1 = ''

    category = txt1.split('\nTopic',1)
    category = category[1]
    category = category.split('\nSubmitter',1)
    category = category[0]
    auth = txt1.split('\nSubmitter',1)
    auth = auth[1]
    auth = auth.split('\nAffiliation',1)
    auth = auth[0]
    aff = txt1.split('\nAffiliation',1)
    aff = aff[1]
    aff = aff.split('\nParticipant')
    aff = aff[0]
    if 'Secondary Category' in txt1:
        sub_category = txt1.split('\nSecondary Category',1)
        sub_category = sub_category[1]
        sub_category = sub_category.split('\n',1)
        sub_category = sub_category[0]
    else:
        sub_category = ''
    abs_text = txt1.split('\nSUBMISSION DETAILS',1)
    abs_text = abs_text[1]
    abs_text = abs_text.split('\nDISCLOSURE',1)
    abs_text = abs_text[0]
    abs_text = abs_text.replace(str(sub_category),'')
    abs_text = abs_text.replace('Secondary Category','')
    disclosure = txt1.split('\nDISCLOSURE',1)
    disclosure = disclosure[1]
    disclosure = disclosure.split(str(session_title),1)
    disclosure = disclosure[0]
    list_session_title.append(session_title)
    list_article_title.append(session_title)
    list_disclosure.append(disclosure[:len(disclosure)-1])
    list_text.append(abs_text)
    list_authors.append(auth)
    list_category.append(category)
    list_type.append(type1)
    list_sub_category.append(sub_category)
    li_affiliations.append(aff)
    txt2 = txt1.split(session_title)
    artcile_count = 2
    while artcile_count<len(txt2):
        print('Article Count - ',artcile_count)
        try:
            txt3 = txt2[artcile_count]
            article_title = txt3.split('\nSubmission ID',1)
            article_title = article_title[0].strip()
            if article_title=='':
                article_title = session_title
            auth = txt3.split('\nSubmitter',1)
            auth = auth[1]
            auth = auth.split('\nAffiliation',1)
            auth = auth[0]
            aff = txt3.split('\nAffiliation',1)
            aff = aff[1]
            aff = aff.split('Participant',1)
            aff = aff[0]
            abs_text = txt3.split('\nSUBMISSION DETAILS',1)
            abs_text = abs_text[1]
            abs_text = abs_text.split('\nDISCLOSURE',1)
            abs_text = abs_text[0]
            disclosure = txt3.split('DISCLOSURE',1)
            disclosure = disclosure[1]
            list_article_title.append(article_title)
            list_authors.append(auth)
            li_affiliations.append(aff)
            list_text.append(abs_text)
            list_disclosure.append(disclosure[:len(disclosure)-1])
            list_session_title.append(session_title)
            list_type.append(type1)
            list_category.append(category)
            list_sub_category.append(sub_category)
        except:
            pass
        artcile_count+=1

list_session_title = [x.strip() for x in list_session_title]
list_article_title = [x.strip() for x in list_article_title]
list_authors = [x.strip() for x in list_authors]
li_affiliations = [x.strip() for x in li_affiliations]
list_type = [x.strip() for x in list_type]
list_category = [x.strip() for x in list_category]
list_sub_category = [x.strip() for x in list_sub_category]
list_text = [x.strip() for x in list_text]
list_disclosure = [x.strip() for x in list_disclosure]
data = pd.DataFrame()
data['Session'] = list_session_title
data['Article']  = list_article_title
data['Auth'] = list_authors
data['Aff'] = li_affiliations
data['Type'] = list_type
data['Category'] = list_category
data['Subcategory'] = list_sub_category
data['Text'] = list_text
data['Disclosure'] = list_disclosure
data.to_excel('PDF1.xlsx',index = False)