import os
import json
import pandas as pd

biorxiv_dir = './data/CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv/pdf_json/'

def refine_text(json_object):
    # dropping in-text references
    # considering abstract and body_text as of now
    abstract = json_object['abstract']
    body_text = json_object['body_text']

    def get_combined_text(text_dict):
        return " ".join(p['text'] for p in text_dict)
    
    return " ".join([get_combined_text(abstract), get_combined_text(body_text)])

def loadData():
    biorxiv_pdfs = os.listdir(biorxiv_dir)
    print(f'----- Total pdf files in biorxiv {len(biorxiv_pdfs)} -----')

    sample_file_path = os.path.join(biorxiv_dir, biorxiv_pdfs[0])
    sample_json = json.load(open(sample_file_path, 'r'))
    print(f'\n** Keys in pdf file - \n{sample_json.keys()}\n**')

    with open('sample.json', 'w') as f:
        json.dump(sample_json, f)

    refined_pdfs = []
    for pdf in biorxiv_pdfs:
        json_pdf = json.load(open(os.path.join(biorxiv_dir, pdf), 'r'))
        json_pdf['text_'] = refine_text(json_pdf)
        refined_pdfs.append(json_pdf)

    dataframe = pd.DataFrame.from_records(refined_pdfs)
    return dataframe