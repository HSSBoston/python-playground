import markovify

# Get raw text as string.
with open("chord_data_"任意のキー名".txt") as f:
   text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=2) 

# Print three randomly-generated sentences of no more than 100 characters
file = open("chord.txt", 'w')
for i in range(20): 
   chord = text_model.make_short_sentence(100)
   print(chord) 
   file.write(chord)
   file.write("\n")

file.close()
f.close()

