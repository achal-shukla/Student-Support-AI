
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# API KEY
# ==========================

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ==========================
# PROJECT PATHS
# ==========================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

VECTOR_STORE_DIR = BASE_DIR / "vector_store"

# ==========================
# RAG SETTINGS
# ==========================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 4

# Placeholder used to anonymize institution names
COLLEGE_PLACEHOLDER = "<COLLEGE_NAME>"

# Institution names to anonymize
COLLEGE_PATTERNS = [

    # JIIT
    r"\bJIIT(?:\s+[A-Za-z&().,-]+){0,6}",

    # Thapar
    r"\bTHAPAR(?:\s+[A-Za-z&().,-]+){0,10}",

    # JSS
    r"\bJSS(?:\s+[A-Za-z&().,-]+){0,10}",

    # Shiv Nadar
    r"\bShiv\s+Nadar(?:\s+[A-Za-z&().,-]+){0,10}",

    # SHIV NADAR (uppercase documents)
    r"\bSHIV\s+NADAR(?:\s+[A-Z&().,-]+){0,10}",

    # Government College of Engineering & Technology
    r"\bGOVT\.?\s+COLLEGE(?:\s+[A-Za-z&().,-]+){0,10}",

    # Institute of Engineering & Technology
    r"\bInstitute\s+of\s+Engineering\s*&\s*technology(?:\s+[A-Za-z&().,-]+){0,10}",

    # IET Lucknow
    r"\bIET(?:,\s*Lucknow)?",

    # Galgotias
    r"\bGALGOTIAS(?:\s+[A-Za-z&().,-]+){0,10}",

    # Sri Krishna
    r"\bSRI\s+KRISHNA(?:\s+[A-Za-z&().,-]+){0,10}",

    # AKTU
    r"\bDR\.?\s*A\.?P\.?J\.?\s*ABDUL\s*KALAM(?:\s+[A-Za-z&().,-]+){0,15}",

]