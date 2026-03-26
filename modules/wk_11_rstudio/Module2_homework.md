# Week 2Assignment 

**Due:** Wed Feb 12, 2025. 10am. Turn in on canvas.

**Instructions:** 
  * Please turn in the answers to this assignment as a .txt document. To create a .txt document in R, go to **New File**, then select **Text file**. You can use any other text editor if you like. Please do not use Mac's Text Edit application, though.
  * DO NOT include the questions in the document you turn in. Answers only!
  * TURN in your assignment on canvas
  * If you are already versed in R, please feel free to substitute out any questions with the [BONUS Content](#bonus-content) at the end of this document. 
  
:white_check_mark: These are the learning objectives associated with each question

-----

## HOMEWORK QUESTION 1 (5 pts) 

:white_check_mark: The purpose is to build curiosity. Students can imagine what R packages will work for their individual goals and projects.

A. Answer the following: **What is your field of research?** You can use a rotation project or in-lab project. If you don't have a designated field of research, what is a field you would like to move into in the future?

B. Think about the research you would like to do. Use the [Bioconductor Website](https://www.bioconductor.org/) to explore topics that are relevant to you. Answer the following: **What are the names and url's of 2 - 3 packages you would be interested to learn more about?**

C. Evaluate the documentation your packages have available. Compare the documentation between the 2 - 3 packages you selected. Answer: **Which packages appear easier to learn and why?**

## HOMEWORK QUESTION 2 (5 pts)

:white_check_mark: Students will learn how to interface with R and RStudio

*Let's explore R-studio a little bit by learning about shortcut keys. Try the following and report what happens: (answers in words, phrases, or short sentences)**

A. What happens when you press **Alt+Shift+K** on a PC/Linux or **Option+Shift+K** on a Mac?

B. What happens when you are working on the "Console" and you press the **up arrow**?

C. What happens when you are working on the "Console" and you press **CTRL+L**?

D. What shortcut key helps you escape out of an executed command on the "Console"? For example, try executing a sleep function. This puts R to sleep for 5 minutes. (in other words - What would you press to return to the prompt before 5 minutes is complete?)

```r
Sys.sleep(5)
```


-----


## HOMEWORK QUESTION 3 (5 pts) 

:white_check_mark: Students will become familiar with a few basic R objects - vectors

:white_check_mark: Students will execute a few basic R functions

*We learned that vectors come in different classes depending on the data type they house. Answer the following in phrases or sentences.*

A. What are the classes of each of these vectors? 
```r
users <- c("alvin", "viet", "leila")
logins <- c(12, 5, 34)
```

B. If we merge these vectors together into super_vector by concatenating them together (below), what is the class of super\_vector? Why do you think this happened?

```r
super_vector <- c(users, logins)
```

C. How would you force super\_vector into a numeric sub-class? *write the line of code* What happens? *copy the output and write a sentence explanation*


-----

## HOMEWORK QUESTION 4 (5 pts) 

:white_check_mark: Students will become familiar with a few basic R objects - data frames

:white_check_mark: Students will execute a few basic R functions

Heather has written some code to create a data frame with columns for "languages", "greetings", and "partings". Each line of her code except the last line has a bug, or error. Can you de-bug Heather's code? Submit the re-written code.

```
# Heather's code:
languages <- ("English", "Spanish", "Japanese", "French")
_greetings_ <- c("hello", "hola", "ohio", "bonjour")
partings < c("bye", "adios", "mata", "salut")
dictionary <- DataFrame(languages, _greetings_, partings)
dimens(dictionary)
dictionary

```

*Hint: The final line of code should give you the following output:*

```
  languages greetings partings
1   English     hello      bye
2   Spanish      hola    adios
3  Japanese      ohio     mata
4    French   bonjour    salut
```

Turn in the amended code block.

-----


## HOMEWORK QUESTION 5 (5 pts)

Let's practice importing some data. Try to import your selected dataset to your computer

  * Import your dataset into R
    * How would you sync up your dataset to your current working directory?
    * Can you use read.tabl() or read.csv() to import your data?
    * Can you save it as an object?
    * Copy and paste the line of code you used to import your dataset and turn it in
  
  * Perform Exploratory Data Analysis on your dataset
    * Copy and paste the line of code and the reported answers using the following functions on your dataset: `dim`, `str`, `class`, `summary`
    
  * Are there any columns that need to change type (character -> factor)? If so, write the line of code you used to change the type.
-----

# Bonus content

:white_check_mark: Students are encouraged to cultivate their own personal curiosity in R, data science, and programming. Feel free to turn in any of these answers in lieu of Question 1 - 5 if you are experienced user.

  1. Explore the [Base R Cheatsheet](https://iqss.github.io/dss-workshops/R/Rintro/base-r-cheat-sheet.pdf)
  
   What is a function or object you haven't used before? Explore it. Write down what you tried and how it works. Submit code showing what you have done.
    
  2. Explore the [R Graph Gallery](https://www.r-graph-gallery.com/index.html).
  
   Choose a category of R plots that you would like to learn more about. Using the R Graph Gallery pages, wikipedia, and other internet resources, learn how these plots generate their data. Think about which plots you might use in your own research. 

   Next, read through some of the R code in the Gallery associated with each plot. Even if you don't understand the R code, just give it a try. Notice the difference between reading the comments versus the code.

   Write down the type of plot you explored and describe how you would like to use it in your work.

  3. Explore [Our World In Data](https://ourworldindata.org/).

   Click on **Articles By Topic** to activate a pull down menu to explore. You can download any dataset you want. 

   For example, if you go to [Internet access per country over time](https://ourworldindata.org/internet#internet-access), you can see different plots like so...

<img src="webContent/Screen Shot 2023-01-23 at 6.00.02 AM.png" width="600">

   You can select the **Download** menu tab at the bottom, and download the full dataset as a .csv file. Try it! Explore the data you've obtained!

<img src="webContent/Screen Shot 2023-01-23 at 6.00.16 AM.png" width="600">


    Try downloading and importing some of this data. Make a plot. Explain and turn in what you did. 
