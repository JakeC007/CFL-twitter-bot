# CFL-twitter-bot
This is the source code/syntax for a context-free language twitter bot that I wrote. This bot is written in [`Tracery`](https://github.com/galaxykate/tracery) and is hosted and powered by [cheapbotsdonequick](https://cheapbotsdonequick.com/)

You can follow this bot [@Learningtotalk1](https://twitter.com/Learningtotalk1) 

## About This Bot
I wrote this bot with an idea to apply some of the basic phrase structure rules commonly taught in an introductory syntax course to a CFL. Likely not an original idea, but I thought it would be interesting. I then combined those rules with (roughly) the 100 most common words in English for N, V, AdV, a smattering of Adjs, and few important determiners.  


The PS rules I implemented are here enumerated below
 - VP -> V(NP)(PP)(AdvP)
 - NP -> (Det)(AdjP)N(PP)
 - PP -> P(NP)
 - AdvP -> (AdvP)Adv
 - AdjP -> (AdvP) Adj
 
 These rules are then combined into the following simple TP strctures:
 
 TP<sub>1</sub>             |  TP<sub>2</sub>
:-------------------------:|:-------------------------:
![](https://github.com/JakeC007/CFL-twitter-bot/blob/master/resources/img/TP1.png)  |  ![](https://github.com/JakeC007/CFL-twitter-bot/blob/master/resources/img/TP2.png)
 


Obviously there are more complex PS rules, but tweets have a character limit and the more complex the rule I make the less likley the tweet will be under the character limit. Hence the rules I choose. 
