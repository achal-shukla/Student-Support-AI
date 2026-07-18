import re

from config import (
    COLLEGE_PATTERNS,
    COLLEGE_PLACEHOLDER
)


def sanitize_text(text: str) -> str:

    for pattern in COLLEGE_PATTERNS:
        text = re.sub(
            pattern,
            COLLEGE_PLACEHOLDER,
            text
        )

    # Remove repeated placeholders
    text = re.sub(
        rf"({re.escape(COLLEGE_PLACEHOLDER)}\s*)+",
        COLLEGE_PLACEHOLDER + " ",
        text
    )

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()