from chat import Chat
from resources import resources

default_language = 0

def run_it(language, subject, search_str):
    this_chat = Chat(resources, subject, language)
    this_chat.flatten()
    return this_chat.match(search_str)


def chat_loop():
    phrase = "What are you looking for? Press q to exit."
    subject = ()
    while True:
        search_str = input(f'{phrase}\n')
        if search_str == 'q':
            break
        match = run_it(default_language, subject, search_str)
        match_value = match['value']
        print(match)
        main_phrase = "I'm not sure what you're asking for. Try entering the problem you're having - like 'rent' or 'sick'."
        # If some certainty
        if (match['certainty'] > 0):
            subject = match_value['subject']
            main_phrase = f"It looks like you're looking for {match_value['phrase'][default_language]}."
            if 'children' in match_value:
                children = ', '.join(str(i) for i in match_value['children'])
                main_phrase += f" Here are some options: {children}. Which do you need?"
            if 'isLeaf' in match_value:
                leaf_info = ''
                for key, val in match_value['info'][default_language].items():
                    leaf_info += f'\n{key.capitalize()}: {val}'
                main_phrase += f"\n{leaf_info}"
        phrase = main_phrase



if __name__ == '__main__':
    chat_loop()
