
text = open("test.txt", "r")
d = dict()

for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    str1=key+":"+str(d[key])
    print(str1)
    text1 =open("test.txt", "a")
    text1.write('\n')
    text1.write(str1)

#f.write(str1)


#print(f.read())