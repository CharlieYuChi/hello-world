#practice string

text = "X-DSPAM-Confidence:    0.8475";

atpos = text.find(':')
a = float(text[atpos+1:].lstrip())
print(a)