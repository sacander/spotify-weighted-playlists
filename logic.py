# Imports random
from hashlib import new
import random


# Takes a list of numbers and converts them into a relative probabilities, then makes it cumulative
def cumulative_probabilities(prob_values): # prob_values takes a list of numbers

    cumulative_probs = []
    cumulative_probs.append(prob_values[0] / sum(prob_values)) # Adds first relative probability

    for prob in prob_values[1:]: # Takes all probabilities except the first one which has already been added
        cumulative_probs.append(prob / sum(prob_values) + cumulative_probs[-1]) # Finds relative probability then adds it the previous one added to list to make it cumulative

    return cumulative_probs


# Combines multiple lists of uris with different chances based on relative probability values, including each uri at least once
def individual_weightings(uri_lists, prob_values): # uri_lists takes a list of lists of uris, prob_values takes a list of numbers, each corresponding to a list of uris

    final_uris = [] # Final uris for output
    uri_lists_temp = [] # For temporary copy of uri_lists
    looped_lists = [] # Used for logic to see when each uri has been included at least once
    cumulative_probs = cumulative_probabilities(prob_values) # Converts relative probability values to a cumulative probabilities

    for uris in uri_lists: # Copies uri_lists and sets whether each list has been looped to false
        uri_lists_temp.append(list(uris))
        looped_lists.append(False)

    while not all(looped_lists): # When all lists have been looped, the inner statement will be true, making the outer statement false and breaking the loop

        rand = random.random() # Gets a random value

        index = 0 # Used for referencing corresponding items in different lists

        for uris in uri_lists_temp: # For each list of uris provided to function

            if (rand < cumulative_probs[index]): # If passes probability test, moves random uri from temp uri list to final uri list
                random_uri = random.choice(uris)
                final_uris.append(random_uri)
                uris.remove(random_uri)

                if (uris == []): # If list is empty, refills it
                    looped_lists[index] = True
                    uri_lists_temp[index] = list(uri_lists[index])

                break # If passed probability test, break the loop, otherwise incrase index and try next list

            index += 1

    return final_uris