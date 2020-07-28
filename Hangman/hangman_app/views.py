from django.shortcuts import render
from .models import Word

import random

def home(request):
    
    if request.method == 'POST':

        # to get count of users wrong choices 
        counter =  int(request.POST.get('counter')) if request.POST.get('counter') else 0  

        # to get the original word 
        original_word = request.POST.get('original_word')

        # to get the dashed word 
        dashed_word = request.POST.get('dashed_word')

        # to get the letter that user choose
        letter = request.POST.get('letter')

        # check if the letter in the dashed word 
        # this will happen if the user input the letter twice 
        if letter in dashed_word:
            context = {
                'original_word': original_word,
                'dashed_word': dashed_word,
                'counter': counter,
                'error': 'you entered this letter before'
            }
            return render(request, 'home.html', context=context)

        # check if the letter in the word 
        if letter in original_word:
            # temp var to assign a new dashed_word variable
            new_dashed_word = ''
            # looping for all letter in original word 
            # to check if the letter exist in the original word
            for char_index in range(len(original_word)):

                if original_word[char_index] == letter:
                    new_dashed_word += letter
                
                else:
                    new_dashed_word += dashed_word[char_index]

            dashed_word = new_dashed_word

            # check if the original word = dashed word 
            if original_word == dashed_word:

                context = {
                    'message': 'you win the game',
                    'word': original_word
                }
                return render(request, 'home.html', context=context)

        # if letter does not exist in word ...
        else:
            counter += 1

            # if counter more than 5, user will lose the game 
            if counter == 5:

                context = {
                    'message': 'you loss the game',
                    'word': original_word
                }
                return render(request, 'home.html', context=context)
        
        context = {
            'counter': counter,
            'original_word': original_word,
            'dashed_word': dashed_word,
        }

        return render(request, 'home.html', context=context)
    
    else:    

        # to get all objects in the database model 
        all_original_words = Word.objects.all()
        
        # to get random object from the all objects list 
        random_item = random.choice(all_original_words)
        
        # dashed random item 
        dashed_random_item_list = ['*' for x in random_item.text]
        dashed_random_item = ''
        dashed_random_item = dashed_random_item.join(dashed_random_item_list)

        # creating the context dictionary
        context = {
            'original_word': random_item.text.lower(),
            'dashed_word': dashed_random_item
        }

        return render(request, 'home.html', context=context)

    
    
