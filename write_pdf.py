from langchain_core.tools import tool
from datetime import datetime
from pathlib import Path
import subprocess
import shutil

@tool
def render_latex_pdf(latex_content: str) -> str:
    """Render a LaTeX document to pdf .
    
    Args:
      latex_content : The LaTex document content as a string
    
    returns:
      path to the generated pdf document
    """

    if shutil.which("tectonic") is None:
        raise RuntimeError(
            "tectonic is not installed. Install it first on your system"
        )
    
    try:
        output_dir = Path("output").absolute()
        output_dir.mkdir(exist_ok = True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        tex_filename = f"paper_{timestamp}.tex"
        pdf_filename = f"paper_{timestamp}.pdf"

        tex_file = output_dir/tex_filename
        tex_file.write_text(latex_content)

        result = subprocess.run(
           [ "tectonic" ,tex_filename ,"--outdir" , str(output_dir)],
           cwd = output_dir,
           capture_output= True,
           text = True
        )

        final_pdf = output_dir/pdf_filename
        if not final_pdf.exist():
            raise FileNotFoundError("PDF file was not generated")
        
        print(f"Successfully generated PDF at {final_pdf}")
        return str(final_pdf)
    
    except Exception as e:
        print(f"Error rendering LaTeX:{str(e)}")
        raise
    
    return str(final_pdf)