import os
import requests

def fetch_image():
    
    url = input("Enter the URL of the image: ")


    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        
        filename = url.split("/")[-1]
        if not filename:  
            filename = "downloaded_image.jpg"

        
        filepath = os.path.join(folder, filename)

    
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Image saved successfully as {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f" Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    fetch_image()
