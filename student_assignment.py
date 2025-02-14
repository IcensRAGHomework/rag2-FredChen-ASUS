from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    doc = loader.load()
    return doc[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf, mode="single", extraction_mode="layout")
    splitter = CharacterTextSplitter(
        separator=r"第\s[一二三四五六七八九十百千萬0-9\-]+\s[章條].*\n",
        is_separator_regex=True,
        chunk_size=0,
        chunk_overlap=0,
        keep_separator="start",
    )
    doc = loader.load_and_split(splitter)
    return len(doc)
