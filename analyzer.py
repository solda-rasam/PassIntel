import hashlib
import requests
import math

def check_pwned_api(password):
    """
    Checks if a password has been leaked in data breaches using the HaveIBeenPwned API.
    Uses K-Anonymity (only sends the first 5 characters of the SHA-1 hash for privacy).
    """
   
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, remaining_char = sha1_password[:5], sha1_password[5:]
    
  
    url = f'https://api.pwnedpasswords.com/range/{first5_char}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return 0 
    except requests.RequestException:
        return 0

   
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == remaining_char:
            return int(count)  
            
    return 0  

def calculate_entropy_and_time(password):
    """
    Calculates password entropy and estimates brute-force cracking time.
    """
    if not password:
        return 0, "0 seconds"

    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    charset_size = 0
    if has_lower: charset_size += 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_special: charset_size += 33

   
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    pool_possibilities = charset_size ** len(password)

    
    guesses_per_second = 100_000_000_000
    seconds_needed = (pool_possibilities / 2) / guesses_per_second

   
    if seconds_needed < 1:
        time_text = "Instantly"
    elif seconds_needed < 60:
        time_text = f"{int(seconds_needed)} seconds"
    elif seconds_needed < 3600:
        time_text = f"{int(seconds_needed / 60)} minutes"
    elif seconds_needed < 86400:
        time_text = f"{int(seconds_needed / 3600)} hours"
    elif seconds_needed < 31536000:
        time_text = f"{int(seconds_needed / 86400)} days"
    elif seconds_needed < 31536000000:
        time_text = f"{int(seconds_needed / 31536000):,} years"
    else:
        time_text = "Centuries"

    return round(entropy, 2), time_text


if __name__ == "__main__":
    test_pass = "Password123!"
    leak_count = check_pwned_api(test_pass)
    ent, crack_time = calculate_entropy_and_time(test_pass)
    
    print(f"Analysis for: {test_pass}")
    print(f"Leak Count: {leak_count} times in known data breaches")
    print(f"Entropy: {ent} bits")
    print(f"Estimated Cracking Time: {crack_time}")