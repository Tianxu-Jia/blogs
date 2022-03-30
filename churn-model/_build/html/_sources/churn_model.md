# What is churn model?

If you check on google about the churn model, mostly you will find that building a churn model is to forecast which client will leave or not. There was a Kaggle challenge project about the churn model. Client churn was to be forecasted based on historical data.

Make a future teller cristle seems fabulus! 

Then, we can ask a further question: How how needs this churn model come? Is it from the imagination of a talented professor who wants to do some academic research in AI and machine learning? Or is it from some company's marketing or operation department? 

We can image a story. Suppose there are two hosptials. In hospital one, all doctors are geniuses. They can accurately predict when the patient will heal or die according to the patient's symptoms and historical data. In hospital two, the doctors can do further work.They can not only predict the development of the patient's condition (when it will heal or die) based on the patient's symptoms and historical data, but also analyze the causal relationship of various factors and formulate intervention and treatment plans according to the patient's symptoms and historical data, so as to change the development of the patient's condition, shorten the patient's course of disease and reduce the patient's pain, Save the patient's life!


Obviously, we need doctors in the second hospital, although the doctors in the first hospital do forecast perfectly.

Now we come back to our churn model problem. Who or which department proposed the customer churn model? Why do they need the model? Dealing with customers and caring about whether customers are lost should be the market or operation department of a company. 

They care about whether customers lose, but they are more concerned about what they need to do if a customer wants to lose, so as to retain the customer and maximize their business profits at the same time.

Doctors who can only predict the development of the patient's course of disease, but can not intervene in the development of the patient's course of disease, are of little use. What the patient needs is the doctor's effective intervention in the course of the disease. Similarly, when a company's market or operation department puts forward a customer churn model, they are concerned about the prediction of customer churn. However, they are more concerned that when a customer wants to lose, they need to intervene, so as to retain the customer with the minimum cost and maximum profit.

So, specifically, the customer churn model should be a customer churn and intervention system, as shown in Figure 1:

```{figure} ./churn-intervene.jpg
---
height: 450px
name: churn-intervene
---
Overall block diagram of churn forecast and consult service
```

Churn model project with Commercially valuable should include:

1. Predict the loss of customers
2. Intervene in customers who may be retained

This should be an iterative process in which artificial intelligence and business consulting are closely combined. Firstly, collect relevant data, establish a basic data set, predict the churning of coustomer based on this data set, and then put forward intervention suggestions to marketing/operation department. After the intervention, continue to collect data for the next round of prediction and intervention.

Once we take intervention into account and build a customer churn model with business value, things will become more complicated. In the forecasting stage, the output will no longer be two categories(churning/no-churning), but four categories as shown below:

```{figure} ./4-classes.png
---
height: 450px
name: 4-classes
---
Classify customers into 4 groups
```


1. Do-Not-Disturbs(Sleeping Dog): This kind of coustomers will retain if we do nothing, otherwise, they will churn
2. Definite leave: no matter what will happen, they will defininitly leave.
3. Definitely Stay(Sure things): no matter what will happen, they will defininitly definitely stay.
4. Persuadable: They will churn if we don't take some action to intervenwe them.


For the first class of customers, it is optimal that we don't do anything. For the second and third classes of customers, any intervention and persuasion will be worthless. Only the fourth category of customers, we need to intervene.

So, the churn model should be a system that includes two parts: forecast and intervene. The forecast part identify who needs intervension and the intervention part determines the best intervention decision 


