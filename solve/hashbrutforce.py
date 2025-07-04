import hashlib

def bruteforce_sha256(target_hash):
    attempts = 0
    for year in range(2000, 2030):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    candidate = f"{year:04d}{month:02d}{day:02d}"
                    h = hashlib.sha256(candidate.encode()).hexdigest()
                    attempts += 1
                    if h == target_hash:
                        print(f"Attempts: {attempts}")
                        return candidate
                except ValueError:
                    continue
    print(f"Attempts: {attempts}")
    return None

if __name__ == "__main__":
    target_hash = "30e6658e2326d26a1d6ba0dedbb2499fea570362a1ed19e6c2949afd8a458814"
    result = bruteforce_sha256(target_hash)
    if result:
        print("Found:", result)
    else:
        print("No match found.")