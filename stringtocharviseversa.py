def string_to_list(text):
  return [char for char in text]

def list_to_string(characters):
  return str.join("",characters)

text=input("Enter any text: ")
characters=input("Enter characters: ")

string=string_to_list(text)
character_list=list_to_string(characters)

print(text,"to character is:",string)
print(characters,"to string is:",character_list)
