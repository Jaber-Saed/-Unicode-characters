from PIL import Image
from picharsso import new_drawer

if __name__ == "__main__":
    # Open image
    # image = Image.open("logo.jpeg")
    image = Image.open("logo")
    

    # Define drawer
    drawer = new_drawer("gradient", height=31, colorize=False,negative = False,charset = ' :!?PG@')
    
    # Print drawer output
    print(drawer(image))