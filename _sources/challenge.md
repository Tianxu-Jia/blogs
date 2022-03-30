# The Challenges of Churm Model

## 1. Forecast and Causation

<div style="margin-left:5%; margin-right:5%;">
The four classification prediction in churn model is a trivial problem in machine learning. We have many mature machine learning algorithms for that. The real challenge is that for customers who can be persuaded, how we make an intervention. For understand the challenge, we need to understand the basic idea of forecast in machine learning, and what it means when we say intervention. How to use reasoning language to describe the doctor's intervention in the patient's course of disease.


Prediction in machine learning is to predict another feature or event according to a certain feature or feature set. For example, predict someone's income based on their educational background, age, etc. Expressed in mathematical language, it is to establish the mapping between the feature data set and the predicted set. It means that we want to find a mathematical function between the two datasets. We can express if as 

$$
y = f(x)
$$



The mapping $f$ from $x$ to $y$ can be either correlation or causality. For example, we can use the cock crows to predict the rise of the sun, but We cannot control the rise of the sun by interfering with the crowing of the rooster. Why? Because between the cock crowing and the run rising is correlation, not causation. In the same way, we can predict a student's test score by his level ofeffort. If we interfere with a student's level of effort, we can really control his exam results. There is a causal relationship between a student's effort and his examination results.

Let's come back to our churn model problem. We hope to retain customers through intervention. So, we hope to find the reason which make customer stay. The forecast in machine learning doesn't identify the causal relation, so, we should find other methods of identifying the causalities of retaining a customers.


<p><strong>The first Challenge: Identify the causation of retaining customer.</strong></p>
</div>

## 2. Observation and experimentation
<div style="margin-left:5%; margin-right:5%;">
From the process of data generation, it can be divided into observation data and experimental data.

Experimental data refers to the data we can obtain by controlling the experimental process and repeating experiments. For example, nearly all physical and chemical experiments data. Causal reasoning is usually easier for it. We can control one variable and observe the change of another variable to infer whether there is a causal effect between them, and this kind of experiment can be observed and measured repeatedly. For example, we can control the cock's crowing and observe whether the sun rises. From that, we infer whether there is a causality between the cock crowing and the sun rising. In the object motion experiment, we can control the force applied to the object and observe the change in its acceleration to infer the causal relationship between force and acceleration.

Observation data means that a researcher does not (or can't) get involved in the data generation process, but only researches the passively recorded data. For example, if we want to study the world war, we can't launch another world war and study it with repeated experiments. For the study of an epidemic, it is impossible to repeat the experiment. It is also very expensive or impossible to repeat if we want to know the reason for a marketing promotion's success or failure. We can only obtain data through observation, not through intervention and experiment. 

The causal reasoning of observed data will become very difficult, and sometimes there is a lot of pseudo-knowledge in it. For example, what caused the war. What caused the economic recession and recovery? And so on. Similarly, in the customer churn model, what causes the customer churn is also a very challenging problem. The challenge of causal inference from observed data is that we can't repeat the experiment, and at the same time, the data does not have the mechanism of how it is generated. In data science, it is usually said that "all is in data", which is not true for observed data.

<p><strong>The second Challenge: How to identify causal from observation data?</strong></p>
    
</div>
    

## 3. Intervention and Counterfactual

<div style="margin-left:5%; margin-right:5%;">
    
Intervention is the action that changes the course of developing. For example, doctors change the development of a patient's illness through treatment. The marketing department retains customers through customer intervention.

However, our prediction of intervention results is very different from that in machine learning. Usually, the prediction in machine learning is conditional probability, that is, the probability of the prosperity of known condition A and the occurrence of event B, that is $ P(B|A) $. The conditional probability meand that if we already know that event a happened, how certain are we about whether time B happened. 
    
Intervention and conditional probabilities are completely different. Intervention means that if we do event A, what will happen to event B? For example, if a person is 50 years old and never smokes, it is predicted that he can live to 95 years old. This is a prediction problem based on conditional probability in machine learning. If he smokes 10 cigarettes a day from the age of 50, how old can he live? This is a problem of intervention in causal reasoning. The customer intervension is the same problem as these.

How to make decision of intervension? Like always, we knowledge is from out past experiences. For example, my friend Tom has been renting for 10 years. All his friends have bought house and making money. Tom regretted it. He thought that if he bought a house like his friends, he could make a fortune.Tom's regret is based on what didn't happen. What has not happened in the past is called counterfactual.In the intervension of churn model, what action we should take should based the counterfactual inference. This is completely the inferencing of forecast in machine learning, that is forecasting based on the facts that already happened. But the counterfactural inference is based the event that doesn't happened.

<p><strong>The thrid Challenge: Counterfactural inferencing based the event that doesn't exist.</strong></p>                  

</div>






    
        

