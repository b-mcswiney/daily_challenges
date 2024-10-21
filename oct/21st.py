
def longest_substring(s, k):
    index = 1
    currentLetters = [s[0]]
    substring = s[0]
    substring_list = []

    # Get list of all substrings 
    while(index < len(s)):

        if s[index] not in currentLetters and len(currentLetters) < k:
            currentLetters.append(s[index])
        
        elif s[index] not in currentLetters and len(currentLetters) == k:
            currentLetters = [s[index - 1]]
            substring_list.append(substring)
            substring = s[index - 1]
            continue
        
        substring = substring + s[index]
        index = index + 1

    # Add last substring to list
    substring_list.append(substring)

    longest_substring = substring_list[0]

    for x in range(1, len(substring_list)):
        if len(substring_list[x]) > len(longest_substring):
            longest_substring = substring_list[x]

    return longest_substring

print(longest_substring("abcba", 2))
print(longest_substring("asdddssdnaddss", 2))
print(longest_substring("abcdbabccc", 3))