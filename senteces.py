import random

# Function to get a determiner
def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

# Function to get a noun
def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

# Function to get a verb
def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

# Function to get a preposition
def get_preposition():
    """Return a randomly chosen preposition."""
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "during", "except", "for", "from", "in", "into", "near", "of", "off", "on", "over", "through", "to", "under", "with", "without"]
    return random.choice(words)

# Function to get a prepositional phrase
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

# Function to generate a sentence
def make_sentence(quantity, tense):
    """Build and return a sentence with determiner, noun, verb, and prepositional phrase."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

# Main function
def main():
    # Generate six sentences with different combinations of quantity and tense
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

# Call the main function to run the program
if __name__ == "__main__":
    main()