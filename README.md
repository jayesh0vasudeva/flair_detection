# flair_detection

## Explaining the approach to task 1:

data was extracted with the PRAW library in python <br/>
to install PRAW: pip3 install praw <br/>
documentation for PRAW : https://praw.readthedocs.io/en/latest/ <br/> 
the data was then stored into a pandas dataframe which was then saved locally as CSV file <br/> 
data_extraction.ipynb does the job for all you need to have is Jupyter Notebook (open-source web application) and run each cell. <br/> 
<br/>
now to create the mongoDB instance, the library used is pymongo <br/>
to install pymongo: pip3 install pymongo <br/>
documentation for pymongo: https://api.mongodb.com/python/current/ <br/>
In order to get a visualisation of the database created I have used RoboMongo-ROBO 3T <br/>
the instance is created in the model.ipynb file <br/>

## Explaining the approach to task 2:

#### Step 1: Text processing
<ul>
  <li> Converts all the text to lower case </li>
  <li> replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space </li>
  <li>remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing.</li>
  <li> Removes the stop-words in the text</li>
  <li>Removes the digits in the text</li>
</ul>

#### Step 2: LSTM Modeling
<ul>
  <li>vectorizes the post content, by turning each text into either a sequence of integers or into a vector</li>
  <li>Limit the dataset to the top 500,00 words</li>
  <li>we then, set the maximum number of quesries at 250</li>
  <li>the processed data is then truncated and padded so that they are all in the same length for modeling </li>
  <li>followed by a conversion of categotical data to numbers</li>
  <li> TRAIN TEST SPLIT </li>
  <li>The first layer is the embedded layer that uses 100 length 1D tensors to represent each word</li>
  <li>The next layer is the LSTM layer with 100 memory units</li>
  <li>The output layer must create 13 output values, one for each class</li>
  <li>Activation function is softmax for multi-class classification</li>
  <li>Because it is a multi-class classification problem, categorical_crossentropy is used as the loss function</li>
</ul>

## Explaining the approach to task 3: Deploying our modeled web application 

I used flask Framework for the backend of our web application ( Flair Detector ) <br/>
and HTML,of course for our frontend
Flask Documentation: https://flask.palletsprojects.com/en/1.1.x/
(work is under progress)

## Problems Encountered and Solutions :-

Prob: One of the main problem at hand is the accuracy of our model, since there is a cap on the number of posts we can extract and for categories like AMA we have only 3 posts out of 900 (roughly) which causes a lot of biasness towards other categories which can be visualised in the graph (model.ipynb)<br/>
Sol: instead of using integer vector for reprsentation of sentence/words we will form tf-idf vectors and we can also use some pre-trained models (transfer learning), and one of the obvious solution is we increase the number of dense or LSTM/RNN layers.<br/>
<br/>
Prob: Besides that flask is not very google colaboratory friendly because of the HTTP protocol Methods require Local port (5000)<br/>
Sol: train it locally on your device, hassle free



  
