import olefile
f = olefile.OleFileIO('test02.hwp')
encoded_text = f.openstream('PrvText').read()
decoded_text = encoded_text.decode('UTF-16')
print(decoded_text)
print(len('decoded_text'))
#