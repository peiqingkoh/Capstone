
#### Project directory:
1)code 
 - 1_Kaggle_twcs.ipynb
 - 2_ChatBot_MultiClassClassificaiton.ipynb 
 - 3_ChatBot_TopicModelling.ipynb 
 
2)datasets
 - AirAsiaSupport_df.csv
 - AmericanAir_df.csv
 - British_Airways_df.csv
 - combine_airlines1.csv 
 - Delta_df.csv
 - SouthwestAir_df.csv 
 
3)flaskservice

4)Airline_ChatBot

5)apstone Project - Feedback ChatBot.ppt

6)README.md



#### Data science process as follows:
- Define the problem.
- Obtain the data.
- Explore the data.
- Model the data.
- Evaluate the model.
- Answer the problem.


#### With the given sets of data , the following steps are done
- Problem Statements
- Data Import and cleaning
- Model preparation
- Exploratory Data Analysis 
- Modelling & Evaluating
- Conclusion


#### 1) Problem Statements
In the 2nd quarter of 2019, a new research from Juniper Research (Research, Forecasting & Consultancy for Digital Technology Markets) found the number of successful retail chatbot interactions will reach 22 billion by 2023, up from an estimated 2.6 billion in 2019. (https://www.juniperresearch.com/press/press-releases/chatbot-interactions-retail-reach-22-billion-2023)

Chatbot can been seen as a strong potential to reduce operational cost when comparing the values in terms of manhours cost and having the system running 24/7.

Another benefits of using chatbot through the support and questions from customers, insights on where are the pain points can also be derive. These feedbacks can then be used to help the company improve or focus more to help improve user experience and increase user stickiness.

5 airlines (AirAsia, AmericanAir, British Airway, Delta and SouthWest Air) decided to come together to do a joint venture project of building a Chatbot to help reduce opertional cost and increased their sales revenue. The project will be completed in 4 stages.

- 1st stage: Chatbot able to deal with feedback from the passengers.
- 2nd stage: Chatbot able to predict which feedback belongs to the respective airline.
- 2nd stage: Chatbot handle general queries from passengers.
- 3rd stage: Chatbot able to query the database for details like flight booking, cancellation etc.

With that, being a data scientist at AirAsia, I was task to complete the first stage of the project to do a test run to see the general response from the passengers and making predictions if possible.
    

#### 2) Data Import and cleaning
- The dataset was taken from https://www.kaggle.com/thoughtvector/customer-support-on-twitter. Cleaning was done like checking for null and removing duplicates. Texts were also converted to lower case. Stopwords and Lemmatizing are also done.


#### 3) Model preparation
- Multiclass : Data set are being split into train and test sets.
- Topic Modelling: Creating of dictionary and corpus was done.

#### 4) Exploratory Data Analysis 
- Multiclass: EDA was done like doing wordcloud and looking as those most frequently appear words.
- Topic Modelling: ---


#### 5) Modelling & Evaluating
- Multiclass: 3 models were being buillt. Logistic regression, Naive Bayes and Random Forest. Logistic Regression was selected for the production model.
- Topic Modelling: LDA and pyLDAvis was used to evaluate the topics. 


#### 6) Conclusion
Using LDA, I was able to come up with 5 topics which will be used as Intent Classificaiton for the Airline Feedback Chatbot. For the multiclass classification, i only managed to complete making into production model. Integeration into chatbot still in process.

