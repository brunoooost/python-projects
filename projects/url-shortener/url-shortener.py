#pip install pyshorteners or python -m pip install -U pyshorteners
import pyshorteners

#save the original url
long_url = input("Enter the URL to shorten: ")
 
#using tiny.url 
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

#printing the result
print("The Shortened URL is: " + short_url)
