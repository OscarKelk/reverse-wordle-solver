list_file = "word_list.txt"

word_list = ["hello", "goodbye"]

for word in word_list:
    with open(list_file, "a") as f:
        f.write(word + "\n")
        f.close()
