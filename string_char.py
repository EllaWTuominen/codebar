def count_string_characters(str):
    count = 0
    for chr in str:
        count += 1
    return count

print(count_string_characters("Hello, nice to meet you! Nice to meet you too!"))  # Output: 13

print(count_string_characters("Nice to meet you too!"))

print(count_string_characters("Local workstation"))
print(count_string_characters("Very nice to meet you indeed!"))
