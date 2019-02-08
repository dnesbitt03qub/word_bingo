import pysrt
from typing import List

def get_words_from_subtitle_file(path: str) -> List[str]:
    
    # Read from file
    subtitles = pysrt.open(path)
    
    # Put content into List of str
    subtitle_content = [subtitle.text for subtitle in subtitles]
    
    return subtitle_content