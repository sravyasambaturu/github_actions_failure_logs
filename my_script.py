import requests
import os

def fetch_and_save(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    with open(filename, "w") as f:
        f.write(response.text)

def process_file(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content.upper()

def main():
    url = "https://www.example.com"
    filename = "output.txt"

    fetch_and_save(url, filename)
    processed_content = process_file(filename)
    print(processed_content)
    os.remove(filename)

if __name__ == "__main__":
    main()