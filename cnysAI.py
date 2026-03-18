print("Hello World!")

import os
import PyPDF2


merge = PyPDF2.PdfMerger()   
lista_arquivos = os.listdir("arquivos")   
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merge.append(f"arquivos/{arquivo}")
        merge.write("pdf_organizado.pdf")