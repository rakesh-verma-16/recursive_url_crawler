import requests
import urllib2
from bs4 import BeautifulSoup

""" This file contains code to understand what's happening in the backend.
It's made to act like a verbose command.
It contains comments for almost each part of the programme.x
This file prints the URL which is being processed,
all the links returned by a URL,
How many times the loop will run.
The Number of Children Url nested in the Parent URL
Total Number of links processed from the URL given by user."""

# Creating a list to store links returned by URL given from user.
starting_list = set()
input_url = raw_input("Please enter the url:\t")

# Function to store the response of Url and parse it's contents.
def url_parser(given_url, link_set, count):

    print "<-------------------------------------------------------------->"
    print "URL being processed is: " + given_url
    # Part 1: Storing the content of the URL in file.

    # Creating BeautifulSoup Object which will be used to extract title of page.
    soup = BeautifulSoup(urllib2.urlopen(given_url))

    # Opening given url and storing it's content in "page" variable.
    page = urllib2.urlopen(given_url)
    page_content = page.read()

    # Extracting Title of page to store to create Unique file name for each URL.
    print "Creating file with the name: " + str(soup.title.string.split("|")[0]) + ".html"
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
        # Extracting "href" tagged item from all <a> tags.
        html_link = each_item.get('href')

        if(html_link is None):
            pass
        else:
            # If returned value is URL (i.e, a complete link), just add it to the temporary list.
            if(html_link.startswith('http') or html_link.startswith('https')):
                link_set.add(html_link)
            # Else if It is a URI (i.e, a relative link), add URL to it and then save it in temporary list.
            elif(html_link.startswith('/')):
                link_set.add(given_url + html_link)
            else:
                pass

    print "Links returned by the URL are: \n"
    for element in link_set:
        print element
        print "\n"

    print "Total links in the given url were:  " + str(len(link_set)) + "\n"


if __name__ == "__main__":

    # Calling the parsing function
    url_parser(input_url, starting_list, 0)

    # Set to store the all the URL (Optional).
    final_list = set()
    # Set to store the URL's returned from a URL.
    temporary_list = set()

    # Copying links returned by URL into the "final_list" set.
    for element in starting_list:
        final_list.add(element)

    # Calling the parser function on each of the URL's returned.
    count = 1
    for element in starting_list:
        url_parser(element, temporary_list,count)
        count += 1
        # Adding the further returned URL to the "final_list" set.
        for each_item in temporary_list:
            final_list.add(each_item)
        # Deleting all elements from the "temporary_list" as all links are stored in "final_list"
        temporary_list.clear()

    # Printing all links returned by the URL when scraping is completed.
    count = 0
    print "Total links scraped are: " + str(len(final_list))
    for element in final_list:
        count +=1
        print "Element number " + str(count) + " processing"
        print element
        print "\n"
