# 1. What is churn model?

<div style="margin-left:5%; margin-right:5%; font-size:20px">
    
    
If you Google churn model, you'll discover that it's most often used to predict whether or not a client will leave. There was a Kaggle challenge project about the churn model. Client churn was to be predicted using historical data.

Making a crystal future teller appears to be a fantastic idea!

Then we can ask another question: How did this churn model come about? Is it the product of a talented professor's imagination who wants to conduct academic research in AI and machine learning? Is it from the marketing or operations department of a company?


We can conjure up a story. Assume there are two hospitals. All of the doctors at Hospital One are geniuses. Based on the patient's symptoms and historical data, they can accurately predict when the patient will heal or die.

The doctors  in hospital two can do more work. They can not only predict the development of the patient's condition (when it will heal or die) based on the patient's symptoms and historical data, but they can also analyse the causal relationship of various factors and formulate intervention and treatment plans based on the patient's symptoms and historical data. So the doctors in the Hospital Two changed the development of the patient's condition, shorten the patient's course of disease, and reduce the patient's pain, and save the patient's life!


Obviously, we need doctors in the second hospital, although the doctors in the first hospital do forecast perfectly.


Now we return to our churn model issue. Who or what department came up with the customer churn model? What is the purpose of the model? Dealing with customers and being concerned about customer loss should fall under the purview of a company's marketing or operations department.


They care whether customers lose, but they are more concerned with what they need to do if a customer wants to lose in order to retain the customer while also maximising their business profits.


Doctors who can only predict the progression of a patient's disease but cannot intervene in the progression of the patient's disease are of little use. What the patient requires is an effective intervention by the doctor during the course of the disease. Similarly, when a company's market or operations department proposes a customer churn model, they are concerned with customer churn prediction. They are more concerned, however, that when a customer wishes to lose, they must intervene in order to retain the customer at the lowest possible cost and profit.


As shown in Figure 1, the customer churn model should include a customer churn forecasting and intervention system.


```{figure} ./images/churn-intervene.jpg
---
height: 450px
name: churn-intervene
---
Overall block diagram of churn forecast and consult service
```


<br>
   
Churn model project with Commercially valuable should include:

<div style="font-size:25px">
<b>
1. Predict the churn of customers  <br>
2. Intervene in customers who may be retained
</b>
</div>
    
<br>
<br>
    
This should be an iterative process that combines artificial intelligence and business consulting. Collect relevant data, create a basic data set, predict customer churn based on this data set, and then present intervention suggestions to the marketing/operations department. Continue to collect data after the intervention for the next round of prediction and intervention.


Things will become more complicated once we consider intervention and develop a customer churn model with business value. In the forecasting stage, the output will no longer be divided into two categories (churning/no-churning), but into four, as shown in Figure 2:
    
    
```{figure} ./images/4-classes.png
---
height: 450px
name: 4-classes
---
Classify customers into 4 groups
```

<div style="font-size:25px">
<b>
1. Do-Not-Disturbs(Sleeping Dog): This kind of coustomers will retain if we do nothing, otherwise, they will churn <br>
2. Definite leave: no matter what will happen, they will defininitly leave.  <br>
3. Definitely Stay(Sure things): no matter what will happen, they will defininitly definitely stay.  <br>
4. Persuadable: They will churn if we don't take some action to intervenwe them. <br>
    </b>
<br>
</div>

It is best if we do nothing for the first class of customers. Any intervention or persuasion will be futile for the second and third classes of customers. We only need to intervene with the fourth category of customers.


As a result, the churn model should be a two-part system: forecast and intervene. The forecast section determines who requires intervention, and the intervention section determines the best intervention decision.

</div>
