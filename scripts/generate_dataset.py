import random
import pandas as pd

random.seed(42)

DRUGS = [
    "weed", "cocaine", "heroin", "mdma", "lsd",
    "brown sugar", "ganja", "charas", "hash", "ecstasy"
]

SLANG = [
    "stuff", "snow", "powder", "tabs", "joint", "dope"
]

OBFUSCATED = {
    "weed": ["w33d", "we*d", "w.e.e.d"],
    "cocaine": ["c0ca!ne", "coke", "sn0w"],
    "mdma": ["md*m@", "ecst@sy"]
}

POSITIVE_TEMPLATES = [
    "Do you have {}?",
    "Selling {} tonight",
    "{} available near metro",
    "Need {} urgently",
    "DM for {}",
    "Looking for {}",
    "Can you arrange {}?"
]

NEGATIVE_TEMPLATES = [
    "Drug abuse is dangerous",
    "Police arrested drug dealers",
    "This movie talks about drugs",
    "Drugs ruin lives",
    "Anti drug campaign starts today",
    "Let's meet for coffee",
    "How are you doing today?"
]

def generate_positive():
    drug = random.choice(DRUGS)
    template = random.choice(POSITIVE_TEMPLATES)

    if drug in OBFUSCATED and random.random() < 0.3:
        drug = random.choice(OBFUSCATED[drug])

    return template.format(drug)

def generate_negative():
    return random.choice(NEGATIVE_TEMPLATES)

def main():
    data = []

    for _ in range(5000):
        data.append((generate_positive(), 1))

    for _ in range(5000):
        data.append((generate_negative(), 0))

    random.shuffle(data)

    df = pd.DataFrame(data, columns=["text", "label"])
    df.to_csv("data/raw/text/train.csv", index=False)

    print("✅ train.csv generated with", len(df), "rows")

if __name__ == "__main__":
    main()