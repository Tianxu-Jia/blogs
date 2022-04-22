# 3. solutions to the the Challenges

<div style="margin-left:5%;">
    
Machine learning, whether regression or classification, seeks to discover the functional mapping relationship between input and output. Correlation and causality can be achieved through function mapping. The goal of developing a business churn model is to intervene and retain customers. As a result, it is critical to investigate causality and forecast the outcomes of intervention.

Causality and intervention have long been a source of contention. Countless sages have spent their lives attempting to identify some causalities. Newton established the link between force and acceleration. Through the Leaning Tower of Pisa experiment, Galileo demonstrated that the falling speed of an object has nothing to do with its mass. Unfortunately, until recently, the mathematical representation of causal reasoning and intervention was proposed, and from that emerged a set of strict mathematical theories and methods.


To begin our journey of real-world churn modelling, we must first clarify some fundamental concepts and how to represent causality.

</div>

## 3.1 Preliminary
### 3.1.1 Some Basic concept: Causal Graph and SCM(Structure Causal Model)

<div style="margin-left:5%;">
Smoking causes tar deposition in the lungs, which leads to lung cancer.
    
    
```{figure} ./images/smoking.jpg
---
height: 300px
width: 500px
---
An example of causal graph
```

Figure 3 depicts nodes, which are events such as smoking, tar, and lung cancer. The directed edge from node $A$ to node $B$ represents the causal of $B$. As the in figure 3, smoking is the causal of the tar in lung.  But, one may ask, tar in the must lead to lung cancer? Maybe not always! Churchill smoked heavily, but he lived to the age of 91 and died of natural causes rather than lung cancer. There is only a chance link between smoking and lung cancer. That is, the cause only causes the result to occur with a certain degree of probability. It's known as conditional probability $P(B|A)$. As a result, we can use the probability language to represent the causal-effect relationship. This type of graph is known as a probabilistic graphical model, and it is also known as a causal graph when we want to emphasise the causal-effect relationship in causal inference.

```{figure} ./images/churchill-smoking.jpg
---
height: 500px
width: 500px
---
Did smoking cause Churchill had lung cancer?
```
    
<br>
    
Tom and Jerry are two UK middle school students. They will take the GCSE exam. Tom is a hard worker. He studies for eight hours a day, whereas Jerry primarily plays computer games. He studies for only one hour per day. We can assume that Tom's test results will be higher than Jerry's. In a statistical sense, there should be a functional relationship between GCSE results and study hours.

<br>
    
$$ GCSE \, Score = f(study \, hours) $$
Like the causal graph, we can also use simalar graph to represent the causal-effect relationship, that is called SCM(Structure Causal Model)


![The SCM of study hours and GCSE score](./images/GCSE.jpg)
    

</div>

### 3.1.2 Special Attention: Conditional Probability and Convention
    
<div style="margin-left:5%;">
    
We must comprehend two particularly perplexing concepts: conditional probability and causality.
    

Assume you have two events, $A$ and $B$. We have already observed that event $A$ has occurred. How do we calculate the likelihood that an event $B$ will occur? In other words, how much information can we obtain from estimating the $B$ if we already know the event $A$? It is denoted mathematically as $P(B|A)$. For example, if the doctor took the patient's temperature and found it to be $39c$, what is the likelihood that he is infected with Covid-19? The doctor was curious about $P(infected with Covid19=Ture|temperature=39c)$. In our churn model problem, what is the probability that the customer will churn if we know he has lost his job? What we want to know is $P(customer will churn=Ture|job will be lost=Ture)$.
    

Conditional probability demonstrates that a researcher is only an observer and recorder of a natural system, not an intervenor. All most machine learning algorithms deal with the conditional probability problem.

It's a different story in terms of causality.
    
    
Let's say we create the event $A$. What about the possibility of event $B$ occurring? In the scenario, the researcher is not only an observer, but also a participant. He is also a component of the system that is being studied. A patent, for example, is extremely ill. He would die if he did not see a doctor. However, the patent decided to see a doctor. Judea Pearl @alma991011292629705181 invented do-calculus to represent causal inference after intervention $P(A|do(B))$. In the churn model, the marketing department discovered that the customer would leave. To keep him, the marketing team will take some steps. This case can be represented as $P(retain the customer|do(intervention))$.

</div>
    
    
### 3.1.3 Machine Learning and Correlation is not Causation.
    
<div style="margin-left:5%;">
    
It primarily solves classification and regression problems in AI and machine learning. The statistical concept underlying them is correlation, not causation. When deciding how to intervene in customer churn, we must consider causality rather than correlation.

For example, we can use the method of causal effect, rather than correlation, to examine the effects of the Russian-Ukrainian military conflict on customer churn.
    

The EU and the United Kingdom backed Ukraine in the military conflict between Russia and Ukraine. However, as @russianoil points out, Europe is heavily reliant on Russian energy supplies. As a result, Russia used energy as a tool to against EU. Please don't get me wrong; I'm just a data scientist looking into the following causal-effect and customer churn.
    
The conflict between Russia and Ukraine has increased energy prices in the UK and EU, causing people's living costs and home energy bills to rise. As a result, some energy companies experienced customer churn.
   

![](./images/R-U-conflict.jpg)

</div>

## 3.2 Causal Inference from Probabilitistic Graphical Model

<div style="margin-left:5%;">

The AB test is a type of causal reasoning method, but it is an experimental reasoning method. Experiential reasoning can be very costly at times. It is nearly impossible to conduct an experiment to determine the causal reasoning behind people's market behaviour. We require causal reasoning based on observed data.
    
Before we introduce the algorithms for causal inference based on experimental data, we will first discuss some PGM concepts (probabilitistic graphical model).
    

A directed probabilitistic graphical model is made up of a collection of nodes and directed edges. Two nodes are connected by a single directed edge. With an arrow, it travels from one node to another. One example is depicted in the figure below:

    
![](./images/GPM-1.jpg)
<center>Figure 6: directd graph</center>

   
 </div>
## 1. Backdoor Criterion
    coming soon

## 2.Structure Causal Model(SCM)
    coming soon

## 3. Counterfactual 
    coming soon

