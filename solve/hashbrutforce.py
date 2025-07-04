import hashlib

def bruteforce_sha256(target_hash):
    attempts = 0
    for year in range(2000, 2030):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    candidate = f"{year:04d}{month:02d}{day:02d}"
                    print(f"candidate: {candidate}")
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
    target_hash = "1837f05e00bd84bb5a2e637f54ea6990493d589e9288028759c800d3329bd15b"
    result = bruteforce_sha256(target_hash)
    if result:
        print("Found:", result)
    else:
        print("No match found.")