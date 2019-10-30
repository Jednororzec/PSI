class FileManager:
    def __init__(self,file_name):
        self.file_name=file_name

    def read_file(self):
        uchwyt = open(self.file_name,'r',encoding='utf-8')
        dane1 = uchwyt.read()
        print(dane1)
        uchwyt.close()
        return dane1

    def update_file(self,dane):
        text_data=input('Podaj tekst do dodania')
        text_data =str(text_data)
        uchwyt = open(self.file_name, 'a', encoding='utf-8')
        uchwyt.write(dane + ' '+text_data)
        uchwyt.close()
        return text_data



file=FileManager('plik.txt')
dane=file.read_file()
file.update_file(dane)
file.read_file()