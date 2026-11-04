# We have a list of gifts and want to assign points based on the gift
gifts = ["✏️", "🧸", "🎮", "📚", "🎧"]

# Technology = 10
# Toys = 5
# Books = 3

score = 0

for gift in gifts:
    # Apply scoring rules
    # Check for tech gifts
    if gift in ["🎮","🎧"]:
        score = score + 10
    elif gift in["✏️", "📚"]:
        score +=3
    elif gift in["🧸"]:
        score +=5
    print(f"You see: {gift} | Total Score: {score}")

print(f"\n Final Score {score}")
 




