def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "hii","hiii","heyy","heyyy"):
        return "Hey, how are you?"

    if user_message in ("who are you", "who are you?", "what is your name?", "what is your name","what's your name"):
        return "I am Snappy the bot"

    if user_message in ("how’s the weather", "hows the weather", "How is the weather", "How's the weather"):
        return "Good enough for us to go on a drive"

    if user_message in ("what time is it", "whats the time", "time", "what's the time"):
        return "Look at the top of your screen for that or bottom right if you are using windows"

    if user_message in ("who made you","who made you?","who created you", "who's your creator"):
        return "Like its written in my description.... I was made by Chirag Malik"

    if user_message in ("how are you?", "how's you"):
        return "As perfect as i can get"

    if user_message in ("how old are you","how old are you?"):
        return "Well, I m younger than you for sure"

    if user_message in ("good morning", "morning"):
        return "Top o' the mornin' to ya!"

    if user_message in ("bye"):
        return "It was nice talking to you"

    if user_message in ("good night"):
        return "Good night."

    if user_message in ("how are you", "how are you?","how are you ?"):
        return "Not too shabby. Thanks for asking."

    if user_message in ("ideas", "idea" "what can you do"):
        return """Here are few basic things to ask, you can definitely use greeting like hey, hi, bye, good morning.
                  how old are you
                  how's the weather
                  who made you
                  who are you
                  what time is it
        """
    if user_message in ("okay", "yeah", "ok"):
        return "Yeah!"

    if user_message in ("i m good", "i m fine", "good", "i am good", "good"):
        return "That's great"



    return "I'm not sure I understand,Try sticking to the basic things. Type ideas for some sample questions"