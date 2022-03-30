# The Challenges of Churm Model

## 1. Forecast and Causation
<p style="margin-left:5%; margin-right:5%;">
The four classification prediction in churn model is a trivial problem in machine learning. We have many mature machine learning algorithms for that. The real challenge is that for customers who can be persuaded, how we make an intervention. For understand the challenge, we need to understand the basic idea of forecast in machine learning, and what it means when we say intervention. How to use reasoning language to describe the doctor's intervention in the patient's course of disease.
</p>

<p style="margin-left:5%; margin-right:5%;">
Prediction in machine learning is to predict another feature or event according to a certain feature or feature set. For example, predict someone's income based on their educational background, age, etc. Expressed in mathematical language, it is to establish the mapping between the feature data set and the predicted set. It means that we want to find a mathematical function between the two datasets. We can express if as 

$$
y = f(x)
$$

</p>

<p style="margin-left:5%; margin-right:5%;">
The mapping $f$ from $x$ to $y$ can be either correlation or causality. For example, we can use the cock crows to predict the rise of the sun, but We cannot control the rise of the sun by interfering with the crowing of the rooster. Why? Because between the cock crowing and the run rising is correlation, not causation. In the same way, we can predict a student's test score by his level ofeffort. If we interfere with a student's level of effort, we can really control his exam results. There is a causal relationship between a student's effort and his examination results.
</p>

<p style="margin-left:5%; margin-right:5%;">
Let's come back to our churn model problem. We hope to retain customers through intervention. So, we hope to find the reason which make customer stay. The forecast in machine learning doesn't identify the causal relation, so, we should find other methods of identifying the causalities of retaining a customers.
</p>

<p style="margin-left:5%; margin-right:5%;"><strong>The first Challenge: Identify the causation of retaining customer.</strong></p>


## 2. Observation and experimentation
    

## 3. Intervention and counterfactual
                  







    
        

