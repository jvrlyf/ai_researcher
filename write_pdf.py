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