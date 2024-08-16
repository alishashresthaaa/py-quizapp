def get_quiz_response(score):
    if score == 5:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWFzeWQxMXQ0dzAzcWdwbnBvYmY0ZWpia2x1YndtcW01a3ExZjZrZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eIUpSyzwGp0YhAMTKr/giphy.gif",
            "title": "Quiz master!",
            "text": "Perfect score! You got all the questions right!",
        }
    elif score == 4:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG82eGxjdjgyamdzaHk3aXc2ZDc2MHM1ZW5jYWhjNHlhOXU2aHg2aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ihBQKvIE7gLEA/giphy.gif",
            "title": "Great!",
            "text": "You got almost all the questions right!",
        }
    elif score >= 3:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3F4dmZ2bHo4YzZvaGdhNXdmaTlxd2JnYTU3M3I5ZGl0ZDFuOHBlOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/KMikhPf3RV7pRAJ1YW/giphy.gif",
            "title": "Good!",
            "text": "You got most of the questions right!",
        }
    elif score == 2:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHkyaDh3c2Q0bWhreDVrdmZ1d2p3ZzVlZG5jbjJhNGlkbm45aGU1NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9oF7EAvaFUOEU/giphy.gif",
            "title": "Well!",
            "text": "You got a couple of questions right!",
        }
    elif score >= 1:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJmcG5qaWY1eWxrYjA0NGhkZDdqcnhvZjBiNzJ0OTVnbW5mbG90cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nspvD8XYqUxP2/giphy.gif",
            "title": "Reality Check!",
            "text": "You got one question right!",
        }
    else:
        return {
            "img": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDFnOHZreXIyYWdrc3FrYWhrZWgwYzR5c3MxNzB1aXVtOTFvYmN0OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OPU6wzx8JrHna/giphy.gif",
            "title": "Whoops!",
            "text": "You didn't get any questions right!",
        }
