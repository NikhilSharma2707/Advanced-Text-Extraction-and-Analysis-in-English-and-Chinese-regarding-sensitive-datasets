import secrets

def generate_random_key():
    return secrets.token_urlsafe(16)

if __name__ == "__main__":
    num_keys = 10
    keys = [generate_random_key() for _ in range(num_keys)]
    for i, key in enumerate(keys):
        print(f"Key {i+1}: {key}")
