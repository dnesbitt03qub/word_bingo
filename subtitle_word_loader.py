import srt
from typing import List

def get_words_from_subtitle_file(path: str) -> List[str]:
    
    # Read from file
    with open(path, 'r') as file:
        subtitle_file = file.read()
    
    # Get content from file
    subtitle_generator = srt.parse(subtitle_file)
    subtitles = list(subtitle_generator)        
    
    # Put content into List of str
    subtitle_content = [subtitle.content for subtitle in subtitles]
    
    return subtitle_content