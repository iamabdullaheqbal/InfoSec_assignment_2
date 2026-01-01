from security import hash_password
import os

def dictionary_attack(stored_hash):
    """
    Perform dictionary attack on stored hash
    Returns the cracked password if found, None otherwise
    """
    # Check if dictionary file exists
    if not os.path.exists("dictionary/wordlist.txt"):
        print("Error: Dictionary file 'dictionary/wordlist.txt' not found")
        return None
    
    try:
        with open("dictionary/wordlist.txt", "r", encoding='utf-8', errors='ignore') as file:
            line_count = 0
            for word in file:
                word = word.strip()
                if not word:  # Skip empty lines
                    continue
                    
                line_count += 1
                if hash_password(word) == stored_hash:
                    print(f"Password found after checking {line_count} words")
                    return word
                
                # Progress indicator for large files
                if line_count % 10000 == 0:
                    print(f"Checked {line_count} words...")
            
            print(f"Checked {line_count} total words")
        return None
        
    except FileNotFoundError:
        print("Error: Dictionary file not found")
        return None
    except Exception as e:
        print(f"Error reading dictionary file: {e}")
        return None
