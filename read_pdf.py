from langchain_core.tools import tool
import io
import fitz  # PyMuPDF
import requests 

@tool
def read_pdf(url:str)->str:
    """Read and extract text from a pdf file  given its url
 
    Args:
       url: The url of the pdf file to read_pdf
    
    returns:
       the extracted text content from the PDF
    """
    
    try :
        response = requests.get(url)
        pdf_file = io.BytesIO(response.content)
        doc = fitz.open(stream = pdf_file, filetype = "pdf")
        num_pages = doc.page_count

        text = ""
        for i, page in enumerate(doc.pages , 1):
            print(f"Extracting text from page {i}/{num_pages}")
            text += page.extract_text() + "\n"

        print(f"Successfully extracted {len(text)} characters of text from PDF")

        return text.strip()
    
    except Exception as e:
        print(f"Error reading PDf : {str(e)}")
        raise