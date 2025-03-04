s = "this is a sentence"
words = s.split()
letter_count_per_word = {w:len(w) for w in words}
print(letter_count_per_word)