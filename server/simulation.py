import random
from chatbot import *

def simulate(bot, num_trials):

    correct = []
    response = "The quick brown fox jumps over the lazy dog."
    responder = random.choice(bot.characters)

#    print 'responder', responder
    for n in range(num_trials):

        tokens = tokenize(response)
        words = filter(lambda word: all([char not in string.punctuation.replace('-', '') for char in word]), tokens)
        response = bot.generate_response(responder, words)
#        print 'response', response

        classified_character = None
        if len(tokens) >= 8:
            classified_character = bot.classify_input(tokens)
#        print 'classified_character', classified_character

        correct.append(classified_character == responder)

        if classified_character:
            responder = bot.pick_responder(classified_character)
#        print 'responder', responder

    return correct

def simulate_char(bot, char, num_trials):

#    correct = []
    response = "The quick brown fox jumps over the lazy dog."
#    responder = random.choice(bot.characters)

    results = {c: 0 for c in bot.characters}
#    print 'responder', responder
    for n in range(num_trials):

        tokens = tokenize(response)
        words = filter(lambda word: all([char not in string.punctuation.replace('-', '') for char in word]), tokens)
        response = bot.generate_response(char, words)
#        print 'response', response

#        classified_character = None
#        if len(tokens) >= 8:
        classified_character = bot.classify_input(tokens)
#        print 'classified_character', classified_character

        results[classified_character] += 1
#        correct.append(classified_character == char)

#        if classified_character:
#            responder = bot.pick_responder(classified_character)
#        print 'responder', responder

    norm_results = {c: float(v) / sum(results.values()) for c, v in results.iteritems()}
    return norm_results

means = []
chars = ['Aguilera', 'Rand', 'Whitman', 'Grande', 'Shakespeare', 'Nixon']
bot = initialize_bot(chars, None)
for char in chars:
    result = simulate_char(bot, char, 1000)
    means.append(max(result.values()))
#    print char, float(sum(correct)) / len(correct)
print sum(means) / len(means)