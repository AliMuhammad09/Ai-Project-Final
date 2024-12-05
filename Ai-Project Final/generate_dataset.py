import pandas as pd

# Define the initial data
data = [
    ("I love this product, it's amazing!", "positive"),
    ("This is the worst thing I've ever bought.", "negative"),
    ("Absolutely fantastic experience!", "positive"),
    ("I'm very disappointed with the quality.", "negative"),
    ("Will definitely buy again.", "positive"),
    ("Not worth the money.", "negative"),
    ("Overall, it's okay, nothing special.", "neutral"),
    ("The service was acceptable but could be better.", "neutral"),
    ("This product is just fine.", "neutral"),
    ("I am extremely happy with my purchase!", "positive"),
    ("The quality is subpar and I wouldn't recommend it.", "negative"),
]

# Define the additional data with approximately equal sentiments
additional_data = [
    ("The product exceeded my expectations.", "positive"),
    ("Not as described, very disappointed.", "negative"),
    ("It's a decent product for the price.", "neutral"),
    ("Customer service was outstanding!", "positive"),
    ("I would not buy this again.", "negative"),
    ("Meets my needs perfectly.", "positive"),
    ("The item arrived broken.", "negative"),
    ("Satisfactory performance overall.", "neutral"),
    ("I'm very satisfied with the purchase.", "positive"),
    ("Terrible quality, do not buy.", "negative"),
    ("The experience was just average.", "neutral"),
    ("Excellent quality and fast shipping!", "positive"),
    ("Waste of money.", "negative"),
    ("It's okay but could be better.", "neutral"),
    ("Absolutely recommend it to everyone!", "positive"),
    ("Extremely poor quality.", "negative"),
    ("Just an average product.", "neutral"),
    ("I hate this.", "negative"),
]

# Extend each sentiment to approximately 17 entries
positive_entries = [entry for entry in additional_data if entry[1] == "positive"] * 6
negative_entries = [entry for entry in additional_data if entry[1] == "negative"] * 6
neutral_entries = [entry for entry in additional_data if entry[1] == "neutral"] * 6

# Combine the entries
combined_additional_data = positive_entries[:17] + negative_entries[:17] + neutral_entries[:17]

# Add enough entries to reach approximately 250 total entries
data.extend(combined_additional_data)

# Sort the data by sentiment
data_sorted = sorted(data, key=lambda x: x[1])

# Create a DataFrame
df = pd.DataFrame(data_sorted, columns=['review_text', 'sentiment'])

# Save to CSV
df.to_csv('D:\\Desktop\\dataset.csv', index=False)
