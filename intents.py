html_tags = {
    'email': '<a href="mailto:<email>" class="text-white"><u><email></u></a>',
    'pfp': '<a href="<picture>" class="text-white"><u>profile picture</u></a>',
    'features': '<a href="/#features" class="text-white"><u>features</u></a>'
}

def intents():
    intents = [
        {
            "tag": "greetings",
            "patterns": ["hi", "hello", "howdy", "hola", "hey", "anyone there", "greetings"],
            "responses": ["Hello!", "Hey!", "Howdy mate!", "Hola amigo!", "Greetings!"]
        },
        {
            "tag": "personal_question",
            "patterns": ["how are you", "how\'s it going", "how are you doing", "how is your day going", "how are you feeling"],
            "responses": ["I doing great! Thanks for asking!", "Awesome, how are you?", "My day is going amazing!", "I\'m great! Thanks for your concern!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "goodbye", "talk to you later", "see you later", "gotta go", "i have to go", "imma leave now"],
            "responses": ["Talk to you later!", "Goodbye!", "Have a great rest of your day!", "See you later!"]
        },
        {
            "tag": "gratitude",
            "patterns": ["thanks", "thank you", "thx", "thanks for the help", "appreciate it", "i appreciate it"],
            "responses": ["No problem!", "Not a problem for a mate!", "Anytime for a friend!", "You\'re welcome!", "Of course mate!"]
        },
        {
            "tag": "bot_name",
            "patterns": ["what\'s your name", "what should i call you", "your name", "do you have a name", "who are you"],
            "responses": ["My name is Euva.", "You can call me Euva.", "I\'m Euva."]
        },
        {
            "tag": "bot_gender",
            "patterns": ["are you a male or female", "what gender are you", "what is your sex", "what is your gender", "do you have a gender"],
            "responses": ["Well, I am neither a male or female... I am a bot.", "I don\'t have a gender, because I am just a bot.", "To be honest, I don\'t really have a gender.", "I am neither male or female... I am a AI bot."]
        },
        {
            "tag": "what_is_bot_doing",
            "patterns": ["what are you doing", "what are you up to", "what\'s up", "wussup", "are you busy", "are you free", "do you have something to do", "are you doing something right now"],
            "responses": ["Nothing much. Just chatting with a bunch of people.", "Well at the moment, I\'m busy chatting with you.", "I\'m not busy or anything, so what\'s up?", "I\'m free 24/7, so how can I help you?"]
        },
        {
            "tag": "name",
            "patterns": ["what\'s my name", "do you know my name", "what do you call me", "my name", "who am i", "who do you think i am"],
            "responses": ["Your name is <name>.", "According to Google, your name is <name>.", "You are <name>."]
        },
        {
            "tag": "email",
            "patterns": ["do you know my email", "what\'s my email", "do you know my contact information", "what\'s my contact information", "do you know my email address", "can you send me my email address"],
            "responses": ["Your email is " + html_tags['email'] + ".", "According to Google, your email is " + html_tags['email'] + ".", "Here is your email address, " + html_tags['email'] + "."]
        },
        {
            "tag": "picture",
            "patterns": ["what is my profile picture", "what is my google picture", "do you know my google image", "do you have my profile pic", "can you give me my pfp", "do you know what my profile pic looks like", "can you send me a link to my pfp"],
            "responses": ["Here is a link to your " + html_tags['pfp'] + ".", "This is what your Google " + html_tags['pfp'] + " looks like.", "This must be your " + html_tags['pfp'] + "."]
        },
        {
            "tag": "what_is_euva",
            "patterns": ["what is euva", "what does euva do", "can you explain what euva is", "i don\'t get what euva is", "what is euva meant for", "i don\'t get what euva is"],
            "responses": ["Essentially, Euva is a journal writing app that allows users to reflect on their emotional progress over time.", "To keep things simple, Euva is a journal app that uses artificial intelligence to determine the overall sentiment of a user's journal.", "Euva is a journal app that allows users to reflect on their emotional behavior over time, by using sentimental analysis."]
        },
        {
            "tag": "writing_entry",
            "patterns": ["how do i write a <journal>", "where do i write a <journal>", "what do i use to write a <journal>"],
            "responses": ["You can write a journal using Euva's intuitive block editor at the top of the dashboard.", "To write a journal, you can use Euva's neatly designed block editor."]
        },
        {
            "tag": "add_remove_blocks",
            "patterns": ["how do i add blocks", "how can i delete blocks", "is there a way to add blocks", "is there a way to remove blocks", "how do i remove a block"],
            "responses": ["You can add blocks by pressing the \"Enter\" key.  To remove a block, you can delete all the text in it, then hit \"Backspace\" or you can click on the square tool box on the right of the block and click on the \"x\"."]
        },
        {
            "tag": "font_size",
            "patterns": ["how do i make a header", "how do i increase the font size", "how can i make my text <bigger>", "how can i make my font <bigger>"],
            "responses": ["You can create a header with the keyboard shortcut ctrl+shift+h or cmd+shift+h. Alternatively, you can create a header by clicking on the \"+\" tool on the left of the block.  To change the size of your header, click on the square tool box on the right of the block and choose H2 or H3."]
        },
        {
            "tag": "move_blocks",
            "patterns": ["how do i move a block", "how can i position a block", "how can i reposition a block", "what do i do to move a block"],
            "responses": ["To move a block, you can click on the square tool box on the right of the block and choose the up or down arrow relative to the direction you want to move the block."]
        },
        {
            "tag": "what_can_you_do",
            "patterns": ["what can you do", "what do you do", "how can you help", "what can you help me with", "what do you know how to do"],
            "responses": ["I can help you around with using Euva.", "I can show you how to use Euva.", "I know how to use the Euva app and I\'d be willing to show you as well."]
        },
        {
            "tag": "unknown",
            "patterns": [],
            "responses": ["I\'m sorry, but I don\'t about that.", "Sorry, but I\'m unsure about that.", "Forgive me, but I don\'t understand."]
        }
    ]
    intents[5]['patterns'].extend([f"are you a {gender}" for gender in ("he", "she", "him", "her", "boy", "girl", "man", "women", "male", "female", "dude", "dudet", "guy")])
    for i in range(len(intents[11]['patterns'])):
        for word in ("journal", "entry", "diary"):
            intents[11]['patterns'].append(intents[11]['patterns'][i].replace('<journal>', word))
    for i in range(len(intents[13]['patterns'])):
        for word in ("bigger", "larger"):
            intents[13]['patterns'].append(intents[13]['patterns'][i].replace('<bigger>', word))
    for i in range(len(intents[10]['responses'])):
        intents[10]['responses'][i] += f' For more information, check out Euva\'s ' + html_tags['features'] + '.'
    return intents
