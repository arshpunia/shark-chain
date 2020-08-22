# shark-chain #
shark-chain is a functional productivity solution that aims to declutter planning, capturing and progress-measurement by virtue of minimalism. There are no shiny buttons or pop-ups, just a simple command-line interface that allows you to: 
- Capture tasks or ideas for future review as they come to your mind
- Add to today's TODO list
- Create a TODO list for any day in the future
- Mark tasks as completed
- Run a numeric analysis on your daily/weekly performance. This includes
   - Completion ratios
   - Task completion timestamps (Useful for determining most productive hours)
   - SharkCoins minted (More on this in further sections)

Minimalism, however should not be mistaken for boring. There is a (admittedly) rudimentary blockchain operating underneath it all that adds your completed tasks to a ledger; so for every 5 tasks you complete, the system jumps through the hoops of calculating a proof of work and mints 1 SharkCoin as an incentive for your perseverance. 

_Please note that this codebase is not intended for public use at the moment. shark-chain in its present shape and form was built by me to suit my requirements when it came to productivity. I am presently learning microservices and web app development so I can start working on a consumer version in Q4 2020 and have a beta out by Q2 2021._

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

## Marking an auxiliary task as completed ##

To mark an auxiliary task as complete: 

`python SharkCoin.py -a <task-name>`

As has been noted earlier, auxiliary-tasks can be more ad-hoc and are not attached to a TODO list. 

## Querying for work-tasks that are not yet completed ##

To list all the tasks for today that have not yet been marked as completed: 
`python SharkCoin.py -q`

## Capturing a thought/task ##

Sometimes it happens (at least with me) when a task suddenly comes to mind, or I have a big idea. Instead of risking losing it, shark-chain allows you to add it to a database, that can later be queried for you to investigate or explore it further. 

`python SharkCoin.py -c <idea>`

Note that `<idea>` is not a task that is added to today's TODO list. Instead, it is added to a separate database, isolated from everything else, including your memory :brain:

## Querying captured ideas ## 

To list all the ideas you have captured (and not deleted from the database): 

`python SharkCoin.py -cq`

## Analyze performance ##

To conduct an analysis of your daily performance, including your success ratios and time metrics: 
`python SharkMetrics.py -r`

## Query performance statistics ##

To query your performance metrics for today:
`python SharkMetrics.py -q`

## TODO ##
- Add section on coins and the _blockchain_ design
- Explain the different types of metrics
- Add a few images
- Method to remove a captured thought
- metrics.py to get stats for the week

## Suggestions ##

As always, if you have any questions or suggestions, please reach out and I'd be happy to discuss them with you. 
