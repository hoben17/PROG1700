# Lesson: Using while loops and pop() in python
# Example Scenerio
# You have a list of gifts that you want to reveal one by one until the list is empty.

gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
countdown = len(gifts)

while gifts: # Loop name runs as long as gifts is not empty
    item = gifts.pop() # Removes the last item
    print(f"you pick: {item}")