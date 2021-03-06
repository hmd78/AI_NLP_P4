# -*- coding: utf-8 -*-
"""clean_text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZBOh581XY-1LkUcq_PFKpEm2rQZvq1U
"""

def clean_text(text):
  # remove numbers
  text_nonum = re.sub(r'\d+', '', text)
  # remove punctuations and convert characters to lower case
  text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
  # substitute multiple whitespacACe with single whitespace
  # Also, removes leading and trailing whitespaces
  return text_nopunct