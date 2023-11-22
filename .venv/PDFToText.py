import pdfplumber
import argparse

class PDFConverter:
    def __init__(self,pdf_path,output_path):
        self.pdf_path = pdf_path
        self.output_path = output_path
        

    def pdf_to_text(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        return text

    def save_to_text_file(self,text):
        with open(self.output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print(f"Done. the result name is {self.output_path}")

def main():
    parser = argparse.ArgumentParser(description='PDF TO TEXT')
    parser.add_argument('-i', '--input', help='Input PDF file path', required=True)
    parser.add_argument('-o', '--output', help='Output Text file path', required=True)

    args = parser.parse_args()
    PDFCon = PDFConverter(args.input,args.output)
    text_from_pdf = PDFCon.pdf_to_text()
    PDFCon.save_to_text_file(text_from_pdf)

main()