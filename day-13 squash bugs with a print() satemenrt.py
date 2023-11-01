# bug getting  code
pages = 0
word_per_page = 0
pages = int(input("number of pages:"))
word_per_page == int(input("number of words per pages"))
# bug here

total_words = pages*word_per_page
print(total_words)

# ---------------------------------------------------------------------
# fixed code
pages = 0
word_per_page = 0
pages += int(input("number of pages:"))  # fixed bug
word_per_page += int(input("number of words per pages"))  # fixed bug

total_words = pages*word_per_page
print(total_words)
