# Given dictionary
test_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

search_value = 10

frequency = list(test_dict.values()).count(search_value)

print("Frequency of", search_value, "is:", frequency)