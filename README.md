
![DogGo Logo](https://i.imgur.com/26pMCAx.png)
# DogGo 
Hot Dogs for the next generation.
___
##Inspiration
We were inspired very locally, by the resident hot dog stand owner, Nasir Al-Huttam. He's been taking orders for the UTSC community for almost a decade, and has been in need of an easier way of taking orders, as taking orders through text has been somewhat cumbersome for him.

##Problem
Small businesses, especially food stands, have a difficult time managing non-immediate orders. Current solutions include receiving texts and calls from customers which is unintuitive because this process makes it to determine which orders to take first.

##Our solution
Streamline the order process and give the business a clean, interactive interface to track user orders and respond efficiently and cleanly.

##What it does
Using Microsoft Azure and Recast.ai, we've created a chatbot that takes orders from the customer from the Facebook Messenger app, and gives the user an interactive, intuitive experience akin to buying from another human, allowing them to even pay for their meal in advance, further streamlining the process.

##How we built it
For frontend, we used HTML and CSS, in combination with JQuery and Javascript to receive json files from the serverside, and interpret that information into display material for the business owner to look.

Recast.ai as well as the Microsoft Bot Framework was used to create the chatbot and program natural language and reactive conversation with the user. Node.js was also used.

The backend is powered by Python and Flask, using Microsoft Azure to deploy the database, postgreSQL, SQLAlchemy were also used.
