from gtts import gTTS
import PyPDF2
import os

print("Selecciona la opción del tipo de archivo que tienes:")
print("""
TIPO DE ARCHIVOS:
1. .txt
2. .pdf
""")

seleccion = int(input("Coloca la opción deseada: "))
path_documento = input("Coloca el path donde se encuentra tu libro: ")

def generador_audio_libro(seleccion, path_documento):
    if seleccion == 1:
        file = open(path_documento, "r", encoding="utf-8")
        text_book = file.read()
        file.close()
        audio = gTTS(text=text_book, lang="es")
        audio.save("audiolibro.mp3")
        print("Audiolibro generado correctamente")
    elif seleccion == 2:
        with open(path_documento, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_book = ""
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text_book += page.extract_text()
        audio = gTTS(text=text_book, lang="es")
        audio_path = os.path.splitext(path_documento)[0] + "_audiolibro.mp3"
        audio.save(audio_path)
        print("Audiolibro generado correctamente")
    else:
        print("Opción seleccionada no válida")

# Llamar a la función
generador_audio_libro(seleccion, path_documento)

