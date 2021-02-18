#The mood checker

user_name = input("Enter your name: ")

if user_name:
    input("After this part enter the mood how you feel " + user_name+". Press Enter to continue.")
    user_mood = input("Enter your mood: ")



if user_mood == "Happy":
    input("It is great to see you happy!")

elif user_mood == "Sad":
    input("Dont be, life is beautiful!")

elif user_mood == "Relaxed":
    input("Lets keep chilling then.")

elif user_mood == "Nervous":
    input("Take a deep breath 3 times.")

else:
    input("I don't recognize this mood.")


