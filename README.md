# Readme

Hacklytics 2023
Nourish Track

healthcare submission

## Inspiration

Physical health is the cornerstone of a life well lived, that extends to people those around you.
Diets are a popular way for people to enhance their health by carefully regulating their food intake.
People are frequently ill and in need of care, therefore it would be beneficial to emphasize good nutrition as an essential part of healing.

We sought to create a tool that benefits both the healthcare sector and the general public. The goal of our study was to promote healthy eating and reduce the need for and costs of direct healthcare. In particular, we were interested in how fast we recover from a sickness by consuming the right nutrition profile, delivered by healthy foods as opposed to nutrient supplements. 

## What it does

Macro and micro nutrients are needed in certain quantity ranges for healthy bodily function. Nutrient deficiencies and needs are also correlated to different kinds of ailments (some more directly). 

With Nourish Track, you can easily discover foods that match your particular nutritional needs, in supported collaboration with your doctor and care providers. 
It would enable you to enter both additive and subtractive needs, giving you a soulful and a fun way of intaking otherwise direct medicines.

## How we built it
We descended into a dataset rabbit hole when examining various data regarding dietary composition, food ingredient breakdowns, potential recipes using various ingredients, and so forth.
We obtained the nutrient breakdown and information about the chemical breakdown of the component from the USDA's FoodData Central (FDC).

We mapped multiple datasets to obtain a more holistic one, that could describe the nutrient distribution most helpful to recover from various disease or ailment. 

We used this mapping to further map different ingredients required for recovery.
The goal is to get the most-recommended dishes prepared from these ingredients.
We use similarity clustering method to identify which foods could help for each ailment.
We used OpenAI Clip to generate dish images to encourage users to eat healthier. 


## Challenges we ran into
As with any data project, one of the main tasks and associated challenges come with data state and fit for the task: is the amount of data sufficient, is the data complete enough, is the data accurate, how far must the data be cleaned to take care of not just missing data and potential inaccuracies, but all the detailed data format readiness between dataset and usability. 

Projects are delivered by people, usually requiring a team, and that team can often be composed of individuals with different backgrounds, ideas, and strong opinions. This presents a challenge when there are competing priorities and plans. 

## Accomplishments that we're proud of
We were ultimately able to stick together and work out the challenges that we faced!
Our application is a working proof-of-concept!

## What we learned
We learned that finding the relevant datasets can be a challenge. 
As always, cleaning the datasets is an iterative process, that we did successfully! An accomplishment.

## What's next for Nourish Track
Further development for Nourish Track would include fleshing out various elements for functionality and accuracy. One thing to be worked on is to ensure that the app ecosystem follows all regulations, such as HIPAA. More nutrition and recipe info could be added to the database, which would require more data (discovery), and data cleaning, and collab with medical profession. 
