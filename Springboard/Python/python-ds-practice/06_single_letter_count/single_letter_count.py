def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_lower = word.lower()
    letter_lower = letter.lower()

    count = 0

    for char in word_lower:
        if char == letter_lower:
            count += 1
    return count 