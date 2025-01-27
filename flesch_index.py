file = open("description.txt.txt","r")
paragraph = file.read()
word = paragraph.split()
sentences = []
sentence = ""
stripped_sentences = []

for char in paragraph:
    if char in [".", "?", "!", ";", ":"]:
        sentences.append(sentence + char)
        sentence = ""
    else:
        sentence += char

if sentence:
    sentences.append(sentence)

for s in sentences:
    stripped_sentences.append(s.strip())

syallable1 = paragraph.lower()

# Remove non-alphabetic characters
syallable1 =''.join(filter(str.isalpha, word))

# Remove final -es, -ed, or -e (except -le)
if syallable1.endswith('es'):
    syallable1 = syallable1[:-2]
elif syallable1.endswith('ed'):
    syallable1 = syallable1[:-2]
elif syallable1.endswith('e') and not syallable1.endswith('le'):
    syallable1 = syallable1[:-1]

# Count vowels or pairs of consecutive vowels
vowels = 'aeiouy'
syllable_count = 0
prev_char = ''
for char in syallable1:
    if char in vowels and prev_char not in vowels:
        syllable_count += 1
    prev_char = char

# If the word has 3 characters or less, it's a single syllable
if len(syallable1) <= 3:
    syllable_count = 1


avgSyllable = syllable_count/len(word)
avgWord = len(word)/len(stripped_sentences)
grade = 206.835 - 1.015 * (avgWord) - 84.6 * (avgSyllable)

if(grade>=0 and grade<=30):
    print("college")

elif(grade<=60 and grade>=50):
    print("high school")

else:
    print("lower school")
