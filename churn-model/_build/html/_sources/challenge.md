# 2. The Challenges of Churm Model

## 2.1. Forecast and Causation

<div style="margin-left:5%; margin-right:5%; font-size:20px">
    
In machine learning, the four classification prediction of the churn model is a simple problem. We have a large number of mature machine learning algorithms for this. The real challenge is determining how to intervene for customers who can be persuaded. To understand the challenge, we must first understand the fundamental concept of forecasting in machine learning, as well as what we mean by intervention. How to use logical reasoning language to describe a doctor's intervention in the course of a patient's disease.


In machine learning, prediction is the prediction of another feature or event based on a specific feature or feature set. Predict someone's income, for example, based on their educational background, age, and so on. It is to establish the mapping between the feature data set and the predicted set in mathematical terms. That is, we want to find a mathematical function that connects the two datasets. We can express it as follows:

$$
y = f(x)
$$



The mapping $f$ from $x$ to $y$ can be either correlation or causality. For example, we can use cock crows to predict the rising sun, but we cannot control the rising sun by interfering with rooster crowing. Why? Because the relationship between the cock crowing and the rising sun is one of correlation, not causation. Similarly, we can predict a student's test score based on his effort. We can really influence a student's exam results if we interfere with his level of effort. There is a causal relationship between a student's effort and his examination results.

Let's return to our churn model issue. We hope to keep customers by intervening. So, we're hoping to figure out what keeps customers stay. Because the forecast in machine learning does not identify the causal relationship, we must find other methods of identifying the causalities of customer retention.


<p style="color:blue; font-size:25px;"><strong>The first Challenge: Identify the causation of retaining customer.</strong></p>

</div>

## 2.2. Observation and experimentation
<div style="margin-left:5%; margin-right:5%; font-size:20px">
It can be divided into observation data and experimental data based on the process of data generation.

The data obtained by controlling the experimental process and repeating experiments is referred to as experimental data. For example, nearly all physical and chemical experiment data. Causal reasoning is usually easier for it. We can control one variable while observing the change in another variable to determine whether there is a causal effect between them, and this type of experiment can be observed and measured repeatedly. We can, for example, control the cock's crowing and observe whether the sun rises. We can then deduce whether there is a link between the cock crowing and the sun rising. In the object motion experiment, we can control the force applied to the object and observe the change in its acceleration to infer the causal relationship between force and acceleration.


Observation data indicates that a researcher does not (or cannot) participate in the data generation process, but instead only studies the passively recorded data. For example, if we want to study World War II, we can't launch another one and study it through repeated experiments. It is impossible to repeat the experiment in order to study an epidemic. It is also prohibitively expensive or impossible to replicate if we want to determine the cause of a marketing promotion's success or failure. We can only collect data through observation, not intervention or experimentation.

The causal reasoning of observed data will become extremely difficult, and there will be a lot of pseudo-knowledge in it at times. For instance, what caused the war. What factors contributed to the economic downturn and recovery? And so forth. Similarly, in the customer churn model, determining what causes customer churn is a difficult problem. The problem with inferring causality from observed data is that we can't repeat the experiment and, at the same time, we don't know how the data was generated. The phrase "all is in data" is commonly used in data science, but this is not true for observed data.
    
<p style="color:blue; font-size:25px;"> <strong>The second Challenge: How to identify causal from observation data?</strong></p>
    
</div>
    

## 2.3. Intervention and Counterfactual

<div style="margin-left:5%; margin-right:5%; font-size:20px">
    
    
Intervention is defined as any action that alters the course of development. Doctors, for example, can alter the course of a patient's illness through treatment. Customers are retained by the marketing department through customer intervention.

However, our prediction of intervention outcomes differs greatly from that of machine learning. In machine learning, the prediction is typically based on conditional probability, that is, the probability of the ff known condition A and the occurrence of event B, denoted by $ P(B|A) $. The conditional probability meand that if we already know that event a happened, how certain are we about whether time B happened. 
    
Intervention and conditional probabilities are not the same thing. Intervention means that if we do event A, what will happen to event B? For example, if a person is 50 years old and never smokes, it is predicted that he can live to 95 years old. This is a prediction problem based on conditional probability in machine learning. If he smokes 10 cigarettes a day from the age of 50, how old can he live? This is a problem of intervention in causal reasoning. The same issue exists with customer intervention.

How do you decide whether or not to intervene? As is customary, we derive our knowledge from our prior experiences. My friend Tom, for example, has been renting for ten years. All of his friends have purchased homes and are making money. Tom felt bad about it. He believed that if he bought a house like his friends, he would be able to make a fortune. Tom's regret stems from what did not occur. The term "counterfactual" refers to what did not occur in the past. What action we should take in the event of a churn model intervention should be based on counterfactual inference. This is entirely the inferencing of forecast in machine learning, that is, forecasting based on past events. However, the counterfactual inference is based on an event that did not occur.

<p style="color:blue; font-size:25px;"> <strong>The thrid Challenge: Counterfactural inferencing based the event that doesn't exist.</strong></p>                  

</div>






    
        

