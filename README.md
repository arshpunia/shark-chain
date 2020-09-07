# shark-chain #
shark-chain is a functional productivity solution that aims to declutter planning, capturing and progress-measurement by virtue of minimalism. There are no shiny buttons or pop-ups, just a simple command-line interface that allows you to: 

- Create a TODO lists
- Edit today's TODO list on the fly
- Capture tasks or ideas for future review as they come to your mind
- Mark tasks as completed
- Run a numeric analysis on your daily/weekly performance. This includes
   - Completion ratios
   - Task completion timestamps (Useful for determining most productive hours)
   - SharkCoins minted (More on this in further sections)

Minimalism, however should not be mistaken for boring. There is a (admittedly) rudimentary blockchain operating underneath it all that adds your completed tasks to a _ledger_; so for every 5 tasks you complete, the system jumps through the hoops of calculating a proof of work and mints 1 SharkCoin as an incentive for your perseverance. 

_Please note that this codebase is not intended for public use at the moment. shark-chain in its present shape and form was built by me to suit my requirements when it came to productivity. I am presently learning microservices and web app development so I can start working on a consumer version in Q1 2021 and have a beta out by Q3 2021._

_If you would like to play with shark-chain, please reach out and I'd be happy to help you set it up. If possible, I can also work on customizing the software for you_

_If you have any suggestions, please reach out to me and I'd be happy to discuss them with you_


The following sections illustrate various features of shark-chain. As has been noted before, it is not consumer ready, but if you are still interested, follow along :smile: 

**A note on work-tasks and auxiliary-tasks**

In building the product, I made a distinction between work tasks and auxiliary tasks. 

_work-tasks_ are tasks directly related to professional or academic life, such as an upcoming deadline or a deliverable on a work/personal project. 

_auxiliry-tasks_ are tasks that, though important or resourceful, are not directly linked to my professional or academic life. This could involve things like finishing a certain percentage of a book, going for a run, etc. Note that auxiliary-tasks do not have a TODO attached to them in shark-chain.

## TODOs for the future :calendar: ##

If you want to set a TODO list for a future date (of course you can edit it later), you can just write the tasks to a file and invoke the script as: 

`python SharkCoin.py -ft <date> <file-name>`

This will create a TODO list for `date` in the database. 

## Creating a TODO list for today ##
If you want to set a TODO list for today (of course you can edit it later), you can simply write the tasks to a file and invoke the script as: 

`python SharkCoin.py -t <file-name>`

## Adding a task to today's TODO list ##

If you want to add a task to today's TODO list: 

`python SharkCoin.py -nt <task-name>`

## Marking a work task as completed ##
To mark a work-task as complete: 

`python SharkCoin.py -w <task-name>`

Please note that `task-name` needs to be in today's TODO list for shark-chain to recognize the task and mark it as complete.

Running this command will also report your completion ratio for today, in addition to the mean completion ratio for the current week. 

You will also see a donut chart displaying the percentage of tasks completed and the percentage you are yet to attack. 

![Output upon completing a task](https://github.com/arshpunia/shark-chain/blob/master/images/CompletingTasks.PNG)

## Marking an auxiliary task as completed ##

To mark an auxiliary task as complete: 

`python SharkCoin.py -a <task-name>`

As has been noted earlier, auxiliary-tasks can be more ad-hoc and are not attached to a TODO list. 

As with completed work tasks, you will see some basic metrics showing your performance for the day and the current week

## Querying for work-tasks that are not yet completed ##

To list all the tasks for today that have not yet been marked as completed: 
`python SharkCoin.py -q`

![Querying Tasks](https://github.com/arshpunia/shark-chain/blob/master/images/QueryingTasks.PNG)

## Capturing a thought/task ##

Sometimes it happens (at least with me) when a task suddenly comes to mind, or I have a big idea. Instead of risking losing it, shark-chain allows you to add it to a database, that can later be queried for you to investigate or explore it further. 

`python SharkCoin.py -c <idea>`

Note that `<idea>` is not a task that is added to today's TODO list. Instead, it is added to a separate database, isolated from everything else, including lapses of your memory :brain:

## Querying captured ideas ## 

To list all the ideas you have captured (and not deleted from the database): 

`python SharkCoin.py -cq`

## Analyze performance ##

To conduct an analysis of your daily performance, including your completion ratios and time metrics (For details on what is tracked, look [here](#metrics)): 
`python SharkMetrics.py -r`

In addition to the text-based output, one graph is also shown. It displays the trend of your completion ratios throughout the week, a quick, helpful indicator of your performance. 

![Performance Analysis](https://github.com/arshpunia/shark-chain/blob/master/images/Metrics.PNG)

## Query performance statistics ##

To query your performance metrics for today:
`python SharkMetrics.py -q`

## The BlockChain (Or the lack of a real one) ##

Around the time I first started developing shark-chain, I was listening to a _fascinating_ [episode](https://tim.blog/2017/06/04/nick-szabo/) of the Tim Ferris show where he interviewed Nick Szabo and Naval Ravikant. In what is one of my favourite podcast episodes ever, Tim, Nick, and Naval explore the origins, evolution and prospects for blockchains and cryptocurrencies. It is a truly enlightening conversation, one I highly recommend, and while it did not turn me into a _crypto-bro_ (I don't think anything ever will), it did instil a sense of awe surrounding ledgers and proofs of work. 

And so I decided to have fun in my own little way with blockchains and cryptocurrencies by infusing one into what was then an un-named work tracking system. 

For every five tasks you complete, shark-chain combines the task names into a single string and keeps trying to suffix it with a numerical value till its hash matches a defined pattern. Once this proof-of-work has been computed, a coin is "minted" (or "mint", I don't know, English is my third language) and shark-chain adds the hash to a SQL database. 

Now before the crypto utopians come at me with their $10k rigs and hardware wallets, I know that what I have is far from a real block-chain; its not distributed, its not immutable, it literally lies on an unencrypted database, and it has a million other flaws. My answer is that I never set out to create a blockchain based system; I just wanted to play with some of the concepts that are involved. Plus, the coins are a nice incentive for completing tasks, so I figured why not? 

## Metrics ##

shark-chain tries to capture some basic metrics that you can use to track your performance. For example, I use a Tableau dashboard (see image) to visualize my weekly performance and productivity trends which I then use to set targets for the upcoming week. Here is a brief description of the metrics that are measured by shark-chain: 

- Work Completed Tasks (wct): A simple ratio of the number of tasks completed to the number of tasks targeted. Probably the most important metric tracked
- Coins from work: Tracks the number of coins that you "earned" from completing work-related tasks. A fun metric, but certainly not the most useful considering it is not a ratio
- Coins from auxiliary: Just like "coins from work", except for auxiliary tasks 
- Time metrics: Tracks the number of tasks completed every hour of the day. In an ideal world, this would be helpful to track my most productive hours. However, I usually take this with some salt as I do not always mark tasks as completed as soon as I finish them, but still great to gather a general sense at the macro level. 

![Visualizing overall metrics in Tableau](https://github.com/arshpunia/shark-chain/blob/master/images/Dashboard.PNG)


## The Road ahead ##

- Like I have mentioned before, shark-chain is custom built for my use, and I plan on keep adding features as my priorities shift and evolve. With that said, I will get started on a more generic version hopefully in Q1 2021. 
- One of biggest blunders I made early on was to not have a simple ID for each task. It is sometimes cumbersome and even inefficient to have to write the entire task description while marking it as complete. I'll definitely fix this soon.
- However, if you want to play with shark-chain, please reach out, and I'd be happy to help you set it up, and even make custom mods for your use cases. 

## Suggestions ##

As always, if you have any questions or suggestions, please reach out and I'd be happy to discuss them with you. 
