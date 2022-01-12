def reverse(text):
   text = text[::-1]
   char = [str(x) for x in text.split(" ")]
   char = char[::-1]
   return " ".join(char)
        
