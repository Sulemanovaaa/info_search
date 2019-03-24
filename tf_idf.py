from typing import Dict
from document import Document

"""
str means Word
"""

Tf = Dict[str, Dict[Document, float]]
Idf = Dict[str, float]
TfIdf = Dict[str, Dict[Document, float]]
