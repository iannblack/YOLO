import random
import time

# YOLO quotes
yolo_quotes = [
    "You only live once!",
    "Seize the day!",
    "Carpe diem!",
    "Live for the moment!",
    "Make today count!"
]

# Random actions
actions = [
    "Dance like no one's watching 💃",
    "Start learning that new skill you've been putting off 📚",
    "Text an old friend and say hi 👋",
    "Plan a spontaneous day trip 🚗",
    "Try cooking a new recipe 🍲",
    "Take a walk in the park 🌳",
]

def yolo_moment():
    # Generate a random quote and action
    quote = random.choice(yolo_quotes)
    action = random.choice(actions)
    print("🌟 YOLO MOMENT 🌟")
    print(f"Quote: {quote}")
    print(f"Suggested Action: {action}")

# Loop for a series of YOLO moments
for i in range(3):
    yolo_moment()
    time.sleep(2)  # Pause to build the suspense
    print("-" * 30)
