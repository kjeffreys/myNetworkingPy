import PyPDF2

def openExamplePDF():
    pdfFileObj = open('C:/Users/aj282/Downloads/Automate_the_Boring_Stuff_2e_onlinematerials/automate_online-materials/meetingminutes.pdf', 'rb')
    print(r"...pdfFileObj = open('C:/Users/aj282/Downloads/Automate_the_Boring_Stuff_2e_onlinematerials/automate_online-materials/meetingminutes.pdf', 'rb')...")
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("...pdfReader = PyPDF2.PdfFileReader(pdfFileObj)...")
    
    print("pdfReader.numPages: {}".format(pdfReader.numPages))

    pageObj = pdfReader.getPage(0)
    print("...pageObj = pdfReader.getPage(0)...")

    print("pageObj.extractText(): {}".format(pageObj.extractText()))

    pdfFileObj.close()

if __name__ == '__main__':
    openExamplePDF()