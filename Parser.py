import requests
import urllib2
from bs4 import BeautifulSoup

# Set to store the url's returned by the Input url.
starting_list = set()
input_url = raw_input("Enter url:\t")


# Function to store the response of Url and parse it's contents.
# Parameters: URL from user and a set to store the returned URLs.
def url_parser(given_url, link_set):

    # Part 1: Storing the content of the URL in file.

    # Creating BeautifulSoup Object to extract title of page.
    soup = BeautifulSoup(urllib2.urlopen(given_url))

    # Opening given url and storing it's content in "page" variable.
    page = urllib2.urlopen(given_url)
    page_content = page.read()

    # Extracting Title of page to store & create Unique file name for each URL.
    with open(soup.title.string.split("|")[0] + '.html', 'w') as fid:
        fid.write(page_content)

    # Part 2: Extracting URL from the given url.

    response = requests.get(given_url)
    html_data = response.text
    soup = BeautifulSoup(html_data)

    # Extracting all elements which starts with <a> tag.
    list_items = soup.find_all('a')

    # Looping over all tags one by one.
    for each_item in list_items:
        html_link = each_item.get('href')
        # If returned value is None, do nothing.
        if(html_link is None):
            pass
        else:
            # If returned value starts with "http" or "https"
            # store them as it is.
            # Example : "https://github.com/sharprakeshverma"
            if(html_link.startswith('http') or html_link.startswith('https')):
                link_set.add(html_link)
            # Else if it is a URI, add URL in front of it.
            # Example: "/sites/public_html/themes/"
            elif(html_link.startswith('/')):
                link_set.add(given_url + html_link)
            else:
                pass

if __name__ == "__main__":
    # Calling the parsing function
    url_parser(input_url, starting_list)

    # Set to store the all the URL (Optional).
    final_list = set()
    # Set to store the URL's returned from a URL.
    temporary_list = set()

    # Copying links returned by URL into the "final_list" set.
    for element in starting_list:
        final_list.add(element)

    # Calling the parser function on each of the URL's returned.
    for element in starting_list:
        url_parser(element, temporary_list)
        # Adding the further returned URL to the "final_list" set.
        for each_item in temporary_list:
            final_list.add(each_item)
        # Deleting all elements from the "temporary_list".
        temporary_list.clear()
