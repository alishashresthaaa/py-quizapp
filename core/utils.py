def get_quiz_response(score):
    if score == 5:
        return "Perfect score! You got all the questions right!"
    elif score >= 3:
        return "Good job! You got most of the questions right!"
    elif score >= 1:
        return "You got some of the questions right. Keep practicing!"
    else:
        return "You didn't get any questions right. Better luck next time!"
