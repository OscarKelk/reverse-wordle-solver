import operator
from datetime import date, datetime


def chunk_string(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))


# Get today's wordle answer
wordle_release_date = date(2021, 6, 19)
today_date = datetime.date(datetime.now())
delta = today_date - wordle_release_date
with open("answers_list.txt", "r") as f:
    answers = f.readlines()
word_today = answers[delta.days]

# Import word list from text file
with open("word_list.txt", "r") as f:
    possible_guesses = f.readlines()
for guess_count, guess in enumerate(possible_guesses):
    possible_guesses[guess_count] = guess.strip()  # Remove trailing newlines
print(f"Imported word list with {len(possible_guesses)} words")

# Get guess order from square matrix
square_matrix = input("Input square matrix:\n")
sm_list = list(chunk_string(square_matrix, 5))

guess_order = []
for sme in sm_list:  # Iterate through each guess
    emoji_string = []
    for emoji in sme:  # Iterate through each character of guess and convert to letters
        if emoji == "⬛" or emoji == "⬜":
            emoji_string.append("i")
        elif emoji == "🟩":
            emoji_string.append("g")
        elif emoji == "🟨":
            emoji_string.append("y")
    guess_order.append(emoji_string)

# Begin search for potential words
final_output = []
for guess_count, guess in enumerate(guess_order):
    print(f"Wordle Guess {guess_count + 1}")
    # Find and list all correct (green) indexes and all misplaced (yellow) indexes
    correct_indexes = []
    misplaced_indexes = []
    for index, letter in enumerate(guess):
        if letter == "g":
            correct_indexes.append(index)
        elif letter == "y":
            misplaced_indexes.append(index)

    word_potential = {}
    # Iterate through the word list
    for pg_count, pg in enumerate(possible_guesses):
        if pg_count % 2000 == 0:
            print(f"Scanned guess count: {pg_count}")

        # Give words points for matching correct indexes
        for ci in correct_indexes:
            if pg[ci] == word_today[ci]:
                try:
                    word_potential[pg] += 1
                except KeyError:
                    word_potential[pg] = 1

        # Give words points for matching misplaced indexes
        for mi in misplaced_indexes:
            if pg[mi] in word_today and mi not in correct_indexes:
                try:
                    word_potential[pg] += 0.5
                except KeyError:
                    word_potential[pg] = 0.5

    max_potential = max(word_potential.items(), key=operator.itemgetter(1))[1]  # Get the highest point count

    # Potential words are all that have the highest point count
    final_output.append([])
    for key in word_potential.keys():
        if word_potential[key] == max_potential:
            if key != word_today:
                final_output[-1].append(key)

# Present results
print("\nResults:\n------------------------")
for output_count, output in enumerate(final_output):
    if len(output) > 12:
        print(f"Guess {output_count + 1}: {len(output)} potential words")
    else:
        print(f"Guess {output_count + 1}: {output}")
print(f"Final word: {word_today}")




# Begin search for potential words
final_output = []
for guess_count, guess in enumerate(guess_order):
    print(f"Wordle Guess {guess_count + 1}")
    # Find and list all correct (green) indexes and all misplaced (yellow) indexes
    correct_indexes = []
    misplaced_indexes = []
    for index, letter in enumerate(guess):
        if letter == "g":
            correct_indexes.append(index)
        elif letter == "y":
            misplaced_indexes.append(index)

    word_potential = {}
    # Iterate through the word list
    for pg_count, pg in enumerate(possible_guesses):
        if pg_count % 2000 == 0:
            print(f"Scanned guess count: {pg_count}")

        # Give words points for matching correct indexes
        for ci in correct_indexes:
            if pg[ci] == word_today[ci]:
                try:
                    word_potential[pg] += 1
                except KeyError:
                    word_potential[pg] = 1

        # Give words points for matching misplaced indexes
        for mi in misplaced_indexes:
            if pg[mi] in word_today and mi not in correct_indexes:
                try:
                    word_potential[pg] += 0.5
                except KeyError:
                    word_potential[pg] = 0.5

    max_potential = max(word_potential.items(), key=operator.itemgetter(1))[1]  # Get the highest point count

    # Potential words are all that have the highest point count
    final_output.append([])
    for key in word_potential.keys():
        if word_potential[key] == max_potential:
            if key != word_today:
                final_output[-1].append(key)

# Present results
print("\nResults:\n------------------------")
for output_count, output in enumerate(final_output):
    if len(output) > 12:
        print(f"Guess {output_count + 1}: {len(output)} potential words")
    else:
        print(f"Guess {output_count + 1}: {output}")
print(f"Final word: {word_today}")
