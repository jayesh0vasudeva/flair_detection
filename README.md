# flair_detection

## Explaining the approach to task 1:

data was extracted with the PRAW library in python <br/>
to install PRAW: pip3 install praw <br/>
documentation for PRAW : https://praw.readthedocs.io/en/latest/ <br/> 
the data was then stored into a pandas dataframe which was then saved locally as CSV file <br/> 
data_extraction.ipynb does the job for all you need to have is Jupyter Notebook (open-source web application) and run each cell. <br/> 
<br/>
<br/>
now to create the mongoDB instance, the library used is pymongo <br/>
to install pymongo: pip3 install pymongo <br/>
documentation for pymongo: https://api.mongodb.com/python/current/ <br/>
In order to get a visualisation of the database created I have used RoboMongo-ROBO 3T <br/>
the instance is created in the model.ipynb file <br/>

## Explaining the approach to task 3:

#### Step 1: Text processing
<ul>
  <li> Converts all the text to lower case </li>
  <li> replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space </li>
  <li>remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing.</li>
  <li> Removes the stop-words in the text</li>
  <li>Removes the digits in the text</li>
</ul>

