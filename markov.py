import markovify

# Get raw text as string.
with open("kek.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print three randomly-generated sentences of no more than 280 characters
for i in range(4):
    print(text_model.make_sentence())