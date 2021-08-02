import re


def remove_source(text):
    cln_text = text
    if '(Source' in cln_text:
        cln_text,_,_ = cln_text.partition('(Source')
    elif '[Written ' in cln_text:
        cln_text,_,_ = cln_text.partition('[Written')
        
    return cln_text

def clean_synopsis(data):
    synopsis = data.synopsis
    
    # removing very small synopsis
    synopsis = synopsis.apply(lambda x: x if ((len(str(x).strip().split())<=300) and len(str(x).strip().split())>30  ) else -1)
    synopsis = synopsis[synopsis!=-1]
    
    # removing source text
    synopsis = synopsis.apply(lambda x: remove_source(x))
    
    # removing japanese characters
    synopsis = synopsis.apply(lambda x: re.sub("([^\x00-\x7F])+"," ",x))
    
    # remove symbols
    rx = re.compile('[&#/@`)(;<=\'"$%>]')
    synopsis = synopsis.apply(lambda x: rx.sub('',x))
    synopsis = synopsis.apply(lambda x: x.replace('>',""))
    synopsis = synopsis.apply(lambda x: x.replace('`',""))
    synopsis = synopsis.apply(lambda x: x.replace(')',""))
    synopsis = synopsis.apply(lambda x: x.replace('(',""))
    

    # removing adaptations
    synopsis = synopsis[synopsis.apply(lambda x: 'adaptation' not in str(x).lower())]    
    synopsis = synopsis[synopsis.apply(lambda x: 'music video' not in str(x).lower())]
    synopsis = synopsis[synopsis.apply(lambda x: 'based on' not in str(x).lower())]
    synopsis = synopsis[synopsis.apply(lambda x: 'spin-off' not in str(x).lower())]
    return synopsis.reset_index(drop=True)
