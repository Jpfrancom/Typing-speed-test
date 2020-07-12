import time

# Variables and presentation of "text"
errors = 0
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
input('Press ENTER to continue: ')
print(f'''
{text} 
Enter the text above:''')

# User response and reading of two sentences
t0 = time.time()
input_user = str(input(''))
t1 = time.time()
len_input_user = len(input_user.split()) 
len_text = len(text.split()) 

# Errors detection
if len_input_user == len_text:
    for i in range(0, len_input_user):
        if text.split()[i] == input_user.split()[i]:
            continue
        else:
            errors += 1
else:
    if len_input_user > len_text:
        bigger = input_user
        smaller = text
    elif len_text > len_input_user:
        bigger = text
        smaller = input_user
    for i in range(0, len(smaller)):
        if bigger[i] == smaller[i]:
            continue
        else:
            errors += 1
    errors = errors + (len(bigger.split()) - len(smaller.split()))

# TIME / ACCURACY / WORD PER MINUTE
time = t1 - t0 
word_per_minute = len_input_user / (time / 60)
accuracy = 100 - ((errors / len(text)) * 100)
print(f'''
\033[4mTIME\033[0;0m: {time:.0f} s
\033[4mACCURACY\033[0;0m: {accuracy:.1f}%
\033[4mWORD PER MINUTE\033[0;0m: {word_per_minute:.1f} wpm''')