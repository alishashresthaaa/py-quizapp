def get_quiz_response(score):
    if score == 5:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "You're a quiz master!",
            "text": "Perfect score! You got all the questions right!",
        }
    elif score == 4:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "Great job!",
            "text": "You got almost all the questions right!",
        }
    elif score >= 3:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "Good job!",
            "text": "You got most of the questions right!",
        }
    elif score == 2:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "Not bad!",
            "text": "You got a couple of questions right!",
        }
    elif score >= 1:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "You got one right!",
            "text": "You got one question right!",
        }
    else:
        return {
            "img": "https://media.giphy.com/media/3o7TKz6r8L5WV7Wgms/giphy.gif",
            "title": "Better luck next time!",
            "text": "You didn't get any questions right!",
        }
