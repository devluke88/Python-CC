# MY assignment for Google IT Automation with Python Coursera

magic_words = {} #word, word_frequency
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
calculate_frequencies = 0

filename = "name.txt"
with open(filename, encoding='utf-8') as f:
    contents = f.read()
    new_uw = " ".join(uninteresting_words)
    words = contents.split()
    words = [x.lower() for x in words]
    words = [x for x in words if x.isalpha()]
    words = [x for x in words if x not in new_uw]

    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

print(word_dictionary)



