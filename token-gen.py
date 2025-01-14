import streamlit as st
import string
import secrets

def generate_character_set(uppercase=False, lowercase=False, numbers=False, special_chars=False):
    """Generate a character set based on selected options"""
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    return chars

def generate_token(length, char_set):
    """Generate a secure token using the secrets module"""
    if not char_set:
        return "Please select at least one character type"
    return ''.join(secrets.choice(char_set) for _ in range(length))

def main():
    st.title("Secure Token Generator")
    st.write("Generate secure tokens for APIs, authentication, and session management.")
    
    # Token length selector
    token_length = st.slider("Token Length", min_value=8, max_value=128, value=32, step=1)
    
    # Character type options
    st.subheader("Character Types")
    col1, col2 = st.columns(2)
    
    with col1:
        uppercase = st.checkbox("Uppercase Letters (A-Z)", value=True)
        lowercase = st.checkbox("Lowercase Letters (a-z)", value=True)
    
    with col2:
        numbers = st.checkbox("Numbers (0-9)", value=True)
        special = st.checkbox("Special Characters (!@#$%^&*)", value=False)
    
    # Generate button
    if st.button("Generate Token"):
        char_set = generate_character_set(uppercase, lowercase, numbers, special)
        
        if not char_set:
            st.error("Please select at least one character type")
        else:
            token = generate_token(token_length, char_set)
            
            # Display the generated token
            st.success("Generated Token:")
            st.code(token, language=None)
            
            # Show token properties
            st.subheader("Token Properties")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"Length: {len(token)} characters")
                st.write(f"Character types used:")
                if uppercase:
                    st.write("- Uppercase letters")
                if lowercase:
                    st.write("- Lowercase letters")
            
            with col2:
                if numbers:
                    st.write("- Numbers")
                if special:
                    st.write("- Special characters")
                
                # Calculate entropy
                charset_length = len(char_set)
                entropy = token_length * (charset_length.bit_length())
                st.write(f"Entropy: ~{entropy} bits")

if __name__ == "__main__":
    main()