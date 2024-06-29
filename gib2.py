import random

# Story template
story = "Once upon a time, there was a [noun] who loved to [verb] in the [adjective] forest."

# Word lists
nouns = ["cat", "dog", "unicorn", "dragon", "wizard"]
verbs = ["dance", "sing", "explore", "fly", "laugh"]
adjectives = ["magical", "enchanted", "mysterious", "vibrant", "whimsical"]

# Randomly select words
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)

# Fill in the blanks
filled_story = story.replace("[noun]", noun).replace("[verb]", verb).replace("[adjective]", adjective)

# Display the result
print(filled_story)
