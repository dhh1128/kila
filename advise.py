def reorder(tags, i, tag_prefixes, until_tag):
    end = -1
    for j in range(i+1, len(tags)):
        tag = tags[j][1]
        if tag[0] not in tag_prefixes:
            if tag.startswith(until_tag):
                end = j
                break
    if end > i:
        tags[i:end+1] = tags[i:end+1][::-1]
        return end
    return -1

def advise(tags):
    """
    Give advice to a TranslationCoach that is trying to help translate
    English into kila.

    tags are tuples (pairs) in the form (english, part of speech), where
    part of speech is something from the nltk inventory (see pos.py in langkit). 
    """
    revised = []
    reordered_until = -1
    i = 0
    while i < len(tags):

        # Define a function to reorder the tags if necessary.
        def try_to_flip_order(tag_prefixes, until_tag):
            nonlocal revised, reordered_until, i
            n = -1
            if i > reordered_until:
                n = reorder(tags, i, tag_prefixes, until_tag)
                if n > -1:
                    reordered_until = n
                    # Cancel this iteration, so the next time through the loop
                    # we restart analysis on the new word in this position.
                    i -= 1
            if n == -1:
                revised.append((word, pos))

        word, pos = tags[i]
        if pos == 'DT': # determiner
            if word in ['a', 'an', 'the']:
                pass # no need to translate
            elif word in ['this', 'that', 'these', 'those']:
                revised.append((word, 'det'))
            elif word == 'some':
                revised.append((word, 'quant'))
        #elif pos == 'CC', 'coordinating conjunction', 'conj'),
        #elif pos == 'CD', 'cardinal digit', ''),
        elif pos == 'EX': #existential there
            revised.append(('d', '~')) # "there is", "there are": hardcode translation
        #elif pos == 'FW', 'foreign word', ''),
        #elif pos == 'IN', 'preposition/subordinating conjunction', 'prep'),
        elif pos in ['JJ', 'JJR', 'JJS', 'RBR', 'RBS']:
            # If there's an [adverb]adjective...noun sequence and we haven't already reordered it
            try_to_flip_order(['JJ', 'RB'], 'NN')
            #elif pos == 'JJ', 'adjective', 'ad'),
            #elif pos == 'JJR', 'adjective, comparative', 'ad'),
            #elif pos == 'JJS', 'adjective, superlative', 'ad'),
            #elif pos == 'RBR', 'adverb, comparative', 'ad'),
            #elif pos == 'RBS', 'adverb, superlative', 'ad'),
        #elif pos == 'LS', 'list marker', 'punct'),
        #elif pos == 'MD', 'modal (could, will)', 'modal'),
        #elif pos == 'NN', 'noun, singular or mass', 'n'),
        elif pos == 'NNS': #noun plural
            revised.append(('vx-', '~'))
            revised.append((word, pos))
        #elif pos == 'NNP', 'proper noun, singular', 'n'),
        #elif pos == 'NNPS', 'proper noun, plural', 'n'),
        #elif pos == 'PDT', 'predeterminer (all, both)', 'quant'),
        elif pos == 'POS': #possessive ending
            revised.append(('d', '~'))
        #elif pos == 'PRP', 'personal pronoun', 'pronoun'),
        #elif pos == 'PRP$', 'possessive pronoun (my, our)', ''),
        elif pos == 'RB': #adverb
            # If there's an adverb...verb sequence and we haven't already reordered it...
            try_to_flip_order(['RB'], 'V')
        #elif pos == 'RP', 'particle (about)', ''),
        #elif pos == 'TO', 'to', 'prep'),
        #elif pos == 'UH', 'interjection', 'inter'),
        #elif pos == 'VB', 'verb base form', 'v'),
        elif pos == 'VBD': #verb past tense: walked
            revised.append((word, pos))
            revised.append(('-dy', '~'))
        elif pos == 'VBG': #verb gerund/present participle: walking
            revised.append((word, pos))
            revised.append(('-go', '~'))
        #elif pos == 'VBN', 'verb past participle', 'v'),
        #elif pos == 'VBP', 'verb non-3rd person singular present', 'v'),
        #elif pos == 'VBZ', 'verb 3rd person singular present', 'v'),
        #elif pos == 'WDT', 'wh-determiner (which, that)', 'det'),
        #elif pos == 'WP', 'wh-pronoun (who, what)', 'pronoun'),
        elif pos == 'WP$': #possessive wh-pronoun (whose)
            revised.append(('d', '~'))
        #elif pos == 'WRB', 'wh-adverb (where, when)', '')
        else:
            revised.append((word, pos))
        i += 1
    return revised
