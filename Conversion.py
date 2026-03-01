import os 
import srt        # library used to perform operatons on subtitles.
import pykakasi   # library used for conversion. 


def convert_srt(input_file):
  name = os.path.basename(input_file).split('.')[0] + '_romaji' + ".srt"
  output_file = os.path.join("outputs", name)

  # Read File Using Srt Library : 
  with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()  

  # Parse Subtitles into Objects 
  subtitles = list(srt.parse(content))

  # Setup Pykakasi Converter 
  kks = pykakasi.kakasi()

  for sub in subtitles: 
    # read subtitle content 
    original_text = sub.content 

    # perform conversion: japanese --> romaji: 
    converted = kks.convert(original_text)  
    romaji_text = " ".join(item['hepburn'] for item in converted)
    
    # replace subtitle text 
    sub.content = romaji_text
  
  # write to new file: 
  new_content = srt.compose(subtitles)

  with open(output_file, "w", encoding="utf-8") as f: 
    f.write(new_content)
    
  return output_file