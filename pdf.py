from pypdf import PdfReader
def extractpdf(pdf_doc):
  try:
    pdf=PdfReader(pdf_doc)
    rawtext=''
    for index,page in enumerate(pdf.pages):# iterate through each page in the PDF document
      text=page.extract_text()
      if text:
        rawtext+=text # concatenate the text from each page to the rawtext variable
    return rawtext
  except Exception as e:
    return f"error in reading the pdf file: {str(e)}"
      