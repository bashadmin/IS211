# IS211_Assignment5
IS211_Assignment5

Last week, we introduced the idea of an algorithm. Continuing with this topic, this week, we will primarily be focusing on data structures. Once again, just like last week, this material could cover an entire course, so this will be a brief overview of what you need to know about data structures.  A data structure is a way of storing data and functionality in such a way as to help us solve common problems. You already have some experience with the built-in data types used in Python, like tuples, lists and dictionaries. We use different data types to do different tasks and one of the most important skills you will need in programming is knowing when to use which data structure for the task at hand. This week’s reading will introduce you to some important data types, including stacks, queues and dequeues.

Required Content: Reading
Chapter 3 on Stacks, Queues and Deques in “Problem Solving with Algorithms and Data Structures” until section 3.7 Skip 3.4.7 - 3.4.10

Optional Content: Reading
If you feel like you need a review of prior data structures, read Chapters 7, 8 and 9 in “Learning Python”
Here is a wikiepdia entry on data structures, which should give a nice overview of what we mean by data structures
http://en.wikipedia.org/wiki/Data_structure%20
A list of many data structures used in computer science
http://en.wikipedia.org/wiki/List_of_data_structures

Optional Content: Useful Links
A visualization of how a stack works when implemented as a list
http://www.cs.usfca.edu/~galles/visualization/StackArray.html
A visualization of how a queue works when implemented as a list
http://www.cs.usfca.edu/~galles/visualization/QueueArray.html


This week’s assignment will focus on using one of the data structures from our reading, the Queue. In this week’s reading, there was a discussion about writing a program to simulate a printer and its print queue. The simulation would determine when print tasks would be generated, placed them on the printer’s queue to eventually be processed by the printer.
This week, we will do something similar. We will write a network simulator to simulate how network requests are processed by a single web server, and a group of web servers behind a load balancer.
We will see how the average wait time, or latency, is related to the server processing rate.  
Data file
http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv
