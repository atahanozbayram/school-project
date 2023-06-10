import re

# Read the input file
with open("somewhat_done.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Remove line breaks within words
content = content.replace("-\n", "")

# Find words split by "-" at the end of a line
pattern = r"(\w+)-\n(\w+)"
matches = re.findall(pattern, content)

# Concatenate the split words
for match in matches:
    content = content.replace(f"{match[0]}-\n{match[1]}", match[0] + match[1])

# Write the modified content to the output file
with open("words_concatenated.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Concatenation completed. The result is saved in 'words_concatenated.txt'.")
