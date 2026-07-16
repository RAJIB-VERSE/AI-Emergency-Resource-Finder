import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_helper import classify_emergency_local, classify_emergency_hf, classify_emergency
from utils import geocode_city

test_cases_ai = [
    # Serious Emergencies
    "my grandfather suddenly clutched his chest and collapsed",
    "a car crashed into a pole outside my house and someone is trapped",
    "my apartment building is shaking violently, books are falling off shelves",
    "the river overflowed and water is entering our ground floor, we need rescue",
    "my wife's water broke and she is having strong contractions",
    "i was walking in the woods and got bitten by a rattlesnake",
    "my child drank some cleaning liquid and is vomiting",
    "huge flames coming out of the restaurant kitchen next door",
    
    # Jokes / Metaphors / Non-emergencies
    "i am dying of laughter from this meme",
    "this new song is absolute fire",
    "my boss is a snake and bit me in the back",
    "there is a flood of emails in my inbox today",
    "i had a heart attack when i saw the price of those shoes",
    "my code keeps crashing",
    "im so pregnant with a food baby after that buffet"
]

print("=== AI Classifier Tests ===")
for case in test_cases_ai:
    print(f"\nInput: '{case}'")
    result = classify_emergency(case)
    print(f"Result: {result['emergency_type']} (conf: {result['confidence']}, method: {result['method']})")
    
test_cases_geo = [
    "Mumbai",
    "asdfasdfasdf", # Invalid city
    "12345",
    "",
]

print("\n=== Geocoding Tests ===")
for city in test_cases_geo:
    res = geocode_city(city)
    print(f"City: '{city}' -> {res}")

