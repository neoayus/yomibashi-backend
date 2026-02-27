import sys        # library: for commandline input 
import srt        # library used to perform operatons on subtitles.
import pykakasi   # library used for conversion. 

# Input file from user using cmd argument: 
inputFile = sys.argv[1]; 
output_file = inputFile.split('.')[0] + '_romaji' + ".srt"

# Read File Using Srt Library : 
with open(inputFile, "r", encoding="utf-8") as subtitle_file:
  content = subtitle_file.read()  
  
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

with open(output_file, "x", encoding="utf-8") as output_file: 
  output_file.write(new_content)
