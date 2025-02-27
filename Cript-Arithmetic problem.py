from itertools import permutations
def is_valid_mapping(mapping, words, result):
    def word_to_number(word):
        return int("".join(str(mapping[char]) for char in word))
    num1 = word_to_number(words[0])
    num2 = word_to_number(words[1])
    num3 = word_to_number(result)
    return num1 + num2 == num3
def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)  
    if len(unique_chars) > 10: 
        print("Too many unique characters to assign digits!")
        return None
    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        if is_valid_mapping(mapping, words, result):
            print("Solution found:")
            for char, digit in mapping.items():
                print(f"{char} -> {digit}")
            return mapping
    print("No solution found.")
    return None
words = ["SEND", "MORE"]
result = "MONEY"
solve_cryptarithmetic(words, result)
