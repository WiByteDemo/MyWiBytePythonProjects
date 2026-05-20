print('You are here to meet the Prof')
print('First you have to pass my quiz')

print()

answer = input('ok, tell me what action words are called?\n')

if answer.lower() == 'verbs':
  print('Correct ... but that was only a warm up')
else: 
  print('Grrr ... your chances of meeting the prof are very low')


answer = input('Give me an 8 letter word with at least 3 vowels\n')

if len(answer) == 8:
  print('Your word has 8 letters')

  count_a = answer.count('a')
  count_e = answer.count('e')
  count_i = answer.count('i')
  count_o = answer.count('o')
  count_u = answer.count('u')

  count_vowels = count_a + count_e + count_i + count_o + count_u

  if count_vowels > 3:
    print('Ooff ... giving more than 3 vowels')
    print('u are wasting my time')
  elif count_vowels < 3:
    print('Ooff ... giving less than 3 vowels')
    print('u acted smart, I caught u')
  else: 
    print('Ooff ... Exactly 3 vowels')
    print('u are not motivated')
    


else: 
  print('You seem to be a disaster')
  print('That word does not even have 8 letters')


sentence = input('ok, tell me a sentence ending in wise assistant, no question \n')

if sentence.endswith('wise assistant'): 
  print('have you not learnt about punctutions')
elif sentence.endswith('wise assistant.'):
  print('your sentence looks ok ... but ...')
  len_first = sentence.find(' ')
  if len_first < 7:
    print('the first word is too short')
else: 
  print('I think you will make the prof. furious.')