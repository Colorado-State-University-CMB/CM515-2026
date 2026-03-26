# Importing & Exporting Data in R

So far, we've created objects by assignment expressions that directly specify their values. Next, we'll learn how to **import** data into R. There are many ways to do this, but we'll just go over one main approach. 

After that, we'll talk about getting plots and tables **out** of R, also called **exporting**. 

These process are sometimes referred to as **IO**, for "Input and Output". 

## How has life expectancy changed over time?

First, let's download a dataset to import.

I found an interesting dataset here: [Our World In Data](https://ourworldindata.org/)
  * Click on "Daily Data Insights" and find the article [Global average life expectancy has more than doubled since 1900](https://ourworldindata.org/data-insights/global-average-life-expectancy-has-more-than-doubled-since-1900)
  * I followed links to [Life Expectancy](https://ourworldindata.org/life-expectancy)
  * I downloaded the data by clicking on the down arrow in the lower right hand corner:

<img src="webContent/Screenshot 2025-02-05 at 5.51.08 AM.png" width="600">


## Importing Data 

❗**EXERCISE** Download a data file

  * ➡️ Right click here:  [life-expectancy_1900-2023_CountriesOnly.csv](https://drive.google.com/file/d/1OYmvfRjNrD0D99hv2He-PbOKDvNXyfFh/view?usp=sharing)
  * ➡️ Download the file by clicking the down arrow in the top right set of icons.
  * ➡️ Save the file somewhere in your Documents directory/folder that makes sense. Consider adding it to a folder called "CM515". 
  * ➡️ Ensure the file name saved is "life-expectancy_1900-2023_CountriesOnly.csv" by viewing it in Finder or explorer.
  
❗ Take a little time here to ensure you know where the file is. 

### Importing Data - Setting the working directory

To import the file into R, we first need to sync up where R **thinks** it is working on your computer with the folder that contains a document you want to import. This is a bit tricky and will require some knowledge of **paths**.

**Paths** - a path describes the location of a folder or file on your computer. Because folders are nested on a computer, the path will start on the left with the "topmost" or "outer most" directory, and then progressively list different sub-directories. 

In R, folder names are separated by a "/" character.

To determine where R "thinks it is" on your computer, use the command `getwd()` for **get working directory**. **directory** is a more computer science-y term for "folder".

```r
getwd()
```

The output is listed as a path. Notice how the output to getwd() matches with the folder names at the bottom of the "Finder" window and with the different folder icons.

<img src="webContent/Screen Shot 2023-01-23 at 9.06.12 AM.png" width="600">

:heavy_exclamation_mark: MAC tip: If you don't see you path in the Finder, pull down the View menu and select Show Path Bar.

:heavy_exclamation_mark: PC tip: If you don't see your path in the Explorer, follow [these directions](https://pureinfotech.com/show-full-path-file-explorer-windows-10/)


## Setting the working directory

❗**EXERCISE** We need to set R's working directory to match the directory where our file lives.

  * ➡️ Go to the **Files** Panel of RStudio.
  * ➡️ Navigate to the location containing the downloaded dataset (may take some sleuthing)
  * ➡️ Change the working directory by going to the **Files Menu Banner**, selecting **More**, and selecting **Set As Working Directory**
  * ➡️ For posterity, copy and paste the command line that appears on the console that looks like `setwd(/directory/directory/)` into your .R script for next time

## Importing Data - Reading in the data

❗**EXERCISE** Together, let's write the code to read the data file into R.

We will use the command `read.table()` to import the dataset

```r

# Check we're in the right place
getwd() 

# Check how read.table is used
help(read.table)

# Look at the data using read.table
read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)


# That only printed out the data from the file, it didn't capture it.
# To capture the data, use an assignment expression:
lifeExp <- read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)

```


:+1: Use help(read.table) to learn how you can also use `read.csv` or `read.csv2` to upload comma separated content, also! There are many ways to do the same thing in R.

  * There are many ways to do the same task - this is going to be a theme. 



## Importing Data - EDA (Exploratory Data Analysis)

⚠️ **BEST PRACTICES** It is a wise idea to inspect your data once you have read it into R.

➡️ Look at what you have acquired and make sure everything looks good!

```r
# EDA
dim(lifeExp)
str(lifeExp)
class(lifeExp)
summary(lifeExp)

```

## Obtaining, Cleaning, Wrangling, & Munging

I obtained the data from [Our World In Data](https://ourworldindata.org/). This is a great resource for worldwide statistics. I use this site because their data is **clean**. What do I mean by that?

  * no blank fields. Missing fields are labeled "NA"
  * no weird characters

One thing you will discover is that most datasets are NOT clean. It takes A LOT of ground work to make your data nice and neat and tidy. This ground work is called either **cleaning**, **wrangling**, or **munging** data, depending on your frustration level. 

I had to clean up this data quite a bit to make the neat and tidy file you just imported.
 
  * Removed duplicate data 
  
## Amending Imported Objects in R

Once we have imported our data into R, we store it in an object. 

Our data is a dataframe in the object `lifeExp`.

Let's look at its structure:

<img src="webContent/Screenshot 2025-02-05 at 8.03.22 AM.png" width="600">

I'd like to change the column `Entity` and `Code` to be factors instead of characters.

```r

# Amend data types
lifeExp$Entity <- as.factor(lifeExp$Entity)
lifeExp$Code <- as.factor(lifeExp$Code)

# EDA Again
dim(lifeExp)
str(lifeExp)
head(lifeExp)
class(lifeExp)
summary(lifeExp)

```

Screenshot 2025-02-05 at 8.03.22 AM

## Reviewing importing steps 

Just to review, here are the basic steps of importing data...

  1. Obtain the data - download it, collect it, etc.
  2. Clean the data (I did this step for you)
  3. Set the working directory
  4. Use `read.table`, `read.csv` or some other function to import the data
  5. Exploratory Data Analysis (EDA)
  6. Amend any data types necessary


----

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
    
----


# Exporting Data out of R - Note - we will skip this today

Next, I'll show you how to save data and plots we generate in R so they can be shared or published in reports, presentations, or publications.

  
⚠️ **BEST PRACTICES** Always include raw data tables as supplemental data when you publish a paper. Also, don't forget to acknowledge R, any packages, and note their versions in the materials & methods.


  * First, let's say we want to filter down this information to just one country and export it.

  * Which columns are which?

➡️ Follow along:

```r


# Let's subset the so we only keep data for the USA:
 
lifeExpUS <- lifeExp[which((lifeExp$Code) == "USA"), ]

dim(lifeExpUS)
head(lifeExpUS)

# Now, let's explore the function write.table() 
help(write.table)

```

----


➡️ Let's export using `write.table()`

```r

write.table(lifeExpUS, file = "lifeExpectancy_USA.txt", sep = "\t")

```

  * By default, R will export this table to your working directory.
  * Switch to your finder or explorer and open the file using a text editor
  * Yikes - I'm not loving those quotes. Let's return to the help page and see if we can change that...

```r

write.table(lifeExpUS, file = "lifeExpectancy_USA.txt", quote = FALSE, sep = "\t")

```

  * HOORAY! The help page really helped. We were able to find an option that met our needs.
  
⚠️ **WARNING** Sometimes when you open the file in excel, the headers are offset - double check

⚠️ **WARNING** Excel will automatically switch gene names to dates (ie: jun-1, oct-4). Use the **import** function in excel to specify the data type of each column to avoid this behavior.

  * **BONUS** - To export a vector object, use `write()` 

----- 

Continue on to [Installing Packages](07_Install.md)
  




