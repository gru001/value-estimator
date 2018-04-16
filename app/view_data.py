import os
import webbrowser

import pandas

# Read dataset into a data table using Pandas
data_table = pandas.read_csv("ml_house_data_set.csv")

# Create Web page view of data
html = data_table[0:100].to_html()

# Save html to temporary file
with open("data.html","w") as f:
    f.write(html)

# Open  the web page in web browser
full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))