def count_words(paragraph):
    # Split the paragraph into words based on whitespace and count them
    words = paragraph.split()
    return len(words)

# Example usage
paragraph = "This is an example paragraph to demonstrate word counting."
word_count = count_words(paragraph)
print("Number of words:", word_count)
