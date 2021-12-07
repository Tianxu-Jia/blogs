#!/usr/bin/env python
# coding: utf-8

# # Machine learning and Causal Inference
# 
# ### Tianxu Jia
# ### Station10 Ltd

# ## Criticism of machine learning..

# Artificial intelligence has evolved through countless waves, finally ushering in a new revolution in the age of the deep learning explosion. People are amazed to discover that AI has become powerful enough to beat the highest level of human Go players, to accurately catch absconding criminals through facial recognition technology, and to learn grammar from thousands of poems and create new verses without breaking a sweat, on a level comparable to ancient poets. In the year 2020, when the new crown pneumonia is raging, artificial intelligence is even more prominent, playing a vital role in epidemic prediction, crowd control, community distribution, disease tracing and new drug development, greatly solving the problem of urban governance for mega populations in extremely harsh conditions.
# 
# Behind all these applications, advanced deep learning technologies and ample data and computing resources are to be credited. However, it is also becoming increasingly apparent that many skills that humans can easily understand and master are still difficult for artificial intelligence. This is particularly true in the field of robotics: thanks to advances in AI, robots can already sense their environment with precision, build complex maps and even communicate with people like friends without barriers. However, many everyday operations that humans find very simple are still a long way off for robots. There are many reasons for this, but one of the most important is that while robots have made great breakthroughs in their sensory capabilities, their brains, or 'decision making' capabilities, are particularly inadequate, making it difficult for them to adapt when faced with similar but different tasks. For example, with improvements in hardware such as motors and gearboxes, robots have been able to execute trajectories with precision and apply forces and moments with accuracy, but the lack of adaptability or 

# On the other hand, when faced with a complex and changing sequence of tasks, humans can easily know what to do and what not to do, what to do first and what to do second, based on their long-standing knowledge, experience and habits. For example, when making a cup of coffee, we usually add the coffee powder first, then fill it with boiling water, then add a little milk, and finally add a cube of sugar. This order is not absolute, we can also add sugar first and then milk, or boiling water first and then coffee powder, it doesn't seem to matter. But we rarely add the milk first, then the boiling water, then the coffee (which certainly doesn't make for good coffee). But it's not so easy to make robots understand this large set of logic. The robot doesn't know that the reason for adding the boiling water first is that it is the boiling water that brews the coffee powder, while the milk does not. Examples include the planning of complex processes on production lines, the order in which 

# ## Machine Learning Make No Sense Without Speaking Causality.

# That said, we're finally getting to the good stuff! Much of the logic behind what robots can't learn is actually cause and effect. The complex world is full of cause and effect, and human beings are the masters of the world, adept at forming their own knowledge by drawing patterns from a wide variety of things. A wise man knows the autumn by its leaves, but a foolish man "sees the coffin before he cries". Now, more and more scientists are realising that robots and artificial intelligence also need this kind of reasoning ability in order to move from weak to strong artificial intelligence. Many researchers who study and apply deep learning are also starting to incorporate causal ideas and theories. This is also partly due to the fact that deep learning itself is not a panacea, or even flawed, for example it requires large amounts of data (and collecting large numbers of samples in many fields is not easy), but it also requires finely designed network structures and well-tuned hyperparameters. These factors aside, deep learning itself does not take into account causality, but merely 'curve-fitting'. This is a point that will be elaborated upon later.
# 
# Here is a simple example of why the absence of cause and effect can be problematic [1]. We know that deep learning, and in particular imitation learning-based thinking, has been studied in the field of driverlessness for several years. One of the earliest algorithms, called DAgger, was to record the driving process of an experienced human driver and then train a model for controlling the vehicle. However, during training it was found that not 

# That said, we're finally getting to the good stuff! Much of the logic behind what robots can't learn is actually cause and effect. The complex world is full of cause and effect, and human beings are the masters of the world, adept at forming their own knowledge by drawing patterns from a wide variety of things. A wise man knows the autumn by its leaves, but a foolish man "sees the coffin before he cries". Now, more and more scientists are realising that robots and artificial intelligence also need this kind of reasoning ability in order to move from weak to strong artificial intelligence. Many researchers who study and apply deep learning are also starting to incorporate causal ideas and theories. This is also partly due to the fact that wouldn't deep learning have been better off using more data features? As this example proves, it's not necessarily good. The reason for the misleading algorithm is that the data on the left contains information about the brake indicator, and the algorithm incorrectly establishes a correlation between the brake indicator and the action of applying the brake, mistakenly assuming that if the brake indicator is on, the brake should be applied. The data on the right, on the other hand, does not contain information about the brake indicator, and the algorithm can only focus on the pedestrian outside the window, thus happening to establish the correct relationship. It turns out that focusing on the pedestrian outside the window rather than the brake indicator is the correct decision. The root of this is that the brake 

# ## Ladder of Causality

# In the field of causality, I have to mention one of the biggest names in the field, Judea Pearl, known as the "father of Bayesian networks", a Turing Award winner who sparked controversy and thought when she gave a presentation at the NIPS conference in 2017. At the time, the deep learning genre was much more fraught than it is now (it's actually slowly been rationalised over the years), so it's understandable that no one was asking for it. Since then, Pearl has written an accessible popular science book, The Book of Why: The New Science of Cause and Effect[2], the Chinese version of which, The Book of Why: The New Science of Cause and Effect, has been published by CITIC Publishing Group[3]. This book also seems to be leading a revolution in caus

# In this book Pearl divides causality into three levels (what he calls the 'ladder of causality'). From the bottom to the top, they are: association, intervention, and counterfactual reasoning. At the bottom is Association, which is what we usually know deep learning to be doing, finding correlations between variables through observed data. This does not lead to the direction in which events affect each other, only that they are related. For example, we know that event A happens when event B also happens, but we do not dig into whether it is because the occurrence of event A causes event B to happen. The second level is Intervention, where we want to know whether Event B will change when we change Event A. The highest level is Conterfactuals, which can also be understood as 'cause and effect', i.e. we want to know if we can change event A if we want event B to change in some way.

# Fig

# So in short, correlation is not the same as causation; the first level of the ladder of causation involves only correlation, the second and third levels only involve causation. The relationship between these three levels can be explained clearly using a classic example. The New England Journal of Medicine published a paper stating that the more chocolate a country consumes, the more Nobel Prize winners that country produces per capita [4]. Such a conclusion is absurd, but what is the problem? By analysing the data, one does find that countries with high chocolate sales tend to win more Nobel Prizes, with an almost linear relationship between the two. But going this far only fits the bottom rung of the ladder of causality - correlation - and we only know that the two are related. In order to find out whether there is a causal relationship between the two, we can intervene and reason counterfactually. We can ask: if the nationals of a country with fewer Nobel prizes were given more chocolate, would that country have more Nobel laureates? This is the second level of 'intervention'. Obviously, the answer is no (eating more chocolate does not lead to more Nobel prizes). Similarly, we can ask the question, if people in countries with a high number of Nobel Prizes did not eat so much chocolate, would they have won so many Nobel Prizes? This is the third level of counterfactual reasoning, and it is clear that the answer is yes (even if they did not eat so much chocolate, they would still win the Nobel Prize), because winning the Nobel Prize is not the 'fruit' of eating chocolate, but 

# Fig

# Therefore, one of the biggest goals of studying causality is to find out what the real causal relationships between things are and to get rid of the confusing pseudo-causal relationships. Causality may be irrelevant in the case of the chocolate Nobel Prize, but it is very important in the fields of economics, medicine, the environment, politics, etc., and directly determines the behaviour of decision-makers. For example, if the causal relationship between 'taking a pill' and 'being cured of a disease' is not precisely known, then doctors will not be able to correctly determine whether or not to take the pill to treat the disease.
# 
# Fortunately, there are more than enough ways to get past the fog and find the causal link between events.

# Reference:
# 
#     1. Pim de Haan, Dinesh Jayaraman, Sergey Levine, "Causal Confusion in Imitation Learning", arXiv:1905.11979 https://arxiv.org/abs/1905.11979?context=stat.ML    
#     2. Judea Peral, Dana Mackenize, "The Book of Why, the New Science of Cause and Efect" 2019, Penguin Random House, UK.
#     3. Franz H Messerli, "Chocolate Consumption, Cognitive Function, and Nobel Laureates", The New England Journal of Medicine, vol. 367, no.16, pp.1562-1564, 2012. https://www.nejm.org/doi/full/10.1056/NEJMon1211064

# Here is my nifty citation {cite}`aa`.

# ```{bibliography}
# ```

# 

# 

# 
