import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO


def create_directory(query):
    # Create a directory with the search query name
    if not os.path.exists(query):
        os.makedirs(query)
    return query


def download_images(query, max_images=500):
    # Create a directory for the search query
    directory = create_directory(query)

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Make sure you have chromedriver installed
    driver.get("https://www.bing.com/images")

    # Find the search box and enter the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Scroll to load more images
    last_height = driver.execute_script("return document.body.scrollHeight")
    image_count = 0

    while image_count < max_images:
        # Scroll down to load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for images to load

        # Find all image elements
        images = driver.find_elements(By.CSS_SELECTOR, "img.mimg")

        # Download images
        for img in images:
            try:
                # Get the image source URL
                src = img.get_attribute("src")

                # Download the image
                if src and "http" in src:
                    response = requests.get(src)
                    if response.status_code == 200:
                        # Save the image
                        image = Image.open(BytesIO(response.content))
                        image_path = os.path.join(directory, f"{query}_{image_count}.jpg")
                        image.save(image_path)
                        print(f"Downloaded {image_path}")
                        image_count += 1

                        # Stop if we've reached the max number of images
                        if image_count >= max_images:
                            break
            except Exception as e:
                print(f"Error downloading image: {e}")

        # Check if we've reached the end of the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # No more images to load
        last_height = new_height

    # Close the browser
    driver.quit()


# Example usage
search_query = "cats"
download_images(search_query, max_images=500)
