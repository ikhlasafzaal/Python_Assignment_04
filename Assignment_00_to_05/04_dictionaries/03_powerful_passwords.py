# SHA256 hashing ke liye hashlib module import kar rahe hain
from hashlib import sha256

# Login function hai jo email aur password check karta hai
def login(email, stored_logins, password_to_check):
    """
    Is function ka kaam hai ki password_to_check ko hash karen aur phir usse stored_logins mein
    email ke corresponding hashed password se compare karen. Agar dono match karte hain toh
    login successful hota hai, otherwise nahi.

    email: email jiske liye hum password check karna chahte hain
    stored_logins: ek dictionary hai jisme emails ke corresponding unke hashed passwords stored hain
    password_to_check: wo password jo user ne diya hai aur jisko hum hash karenge aur check karenge
    """
    
    # Hum jo password user ne diya hai uska hash karte hain aur stored password se compare karte hain
    if stored_logins[email] == hash_password(password_to_check):
        return True  # Agar password match karta hai toh True return karenge
    
    return False  # Agar password match nahi karta toh False return karenge

# Password ko hash karne ka function
def hash_password(password):
    """
    Yeh function password ko SHA256 hashing mein convert karta hai.
    
    Inputs:
        password: wo password jo user ne diya hai.
    
    Outputs:
        hashed password: jo SHA256 hash banega.
    """
    # Password ko pehle byte format mein convert karte hain, phir SHA256 hash banate hain
    return sha256(password.encode()).hexdigest()

# Main function jo login test karne ke liye call kiya jaayega
def main():
    # Yeh dictionary hai jisme emails aur unke hashed passwords stored hain
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password = "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # password = "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password = "password"
    }
    
    # Test cases (login ko test kar rahe hain)
    print(login("example@gmail.com", stored_logins, "word"))  # Expected: False, galat password
    print(login("example@gmail.com", stored_logins, "password"))  # Expected: True, sahi password
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Expected: True, sahi password
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Expected: False, case-sensitive hai
    
    print(login("student@stanford.edu", stored_logins, "password"))  # Expected: True, sahi password
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Expected: False, galat password


# Yeh line zaroori hai, taake Python main() function ko run kar sake jab file execute ho
if __name__ == '__main__':
    main()
