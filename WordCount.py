def word_count(x):
    word_list = x.split()
    return len(word_list)


# main function
text = input("Provide your input to count words: ")
count = word_count(text)
print(f"Word Count of Given input is {count}.")
