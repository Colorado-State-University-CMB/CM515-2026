## Markdown

R Markdown files are mostly written using Markdown. To write R Markdown files, you need to understand what markup languages like Markdown are and how they work. 

In Word and other word processing programs you have used, you can add formatting using buttons and keyboard shortcuts (e.g., "Ctrl-B" for bold). The file saves the words you type. It also saves the formatting, but you see the final output, rather than the formatting markup, when you edit the file (WYSIWYG -- what you see is what you get). 

In markup languages, on the other hand, you markup the document directly to show what formatting the final version should have (e.g., you type `**bold**` in the file to end up with a document with **bold**).

Examples of markup languages include:

- HTML (HyperText Markup Language)
- LaTex
- Markdown (a "lightweight" markup language)

To write a file in Markdown, you'll need to learn the conventions for creating formatting. This table shows what you would need to write in a flat file for some common formatting choices:

| Code | Rendering | Explanation |
|:----:|:---------:|:-----------:|
| `**text**` | **text** | boldface |
| `*text*` | *text* | italicized |
| `~~text~~` | ~~text~~ | strikethrough |
| `[text](www.google.com)` | [text](www.google.com) |hyperlink |

Some other simple things you can do in Markdown include:

- Lists (ordered or bulleted)
- Equations
- Tables
- Figures from file
- Block quotes
- Super/subscripts

For more Markdown conventions, see [RStudio's R Markdown Reference Guide](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf) (link also available through "Help" in RStudio). 

### Tables in R Markdown 

If you want to create a nice, formatted table from an R dataframe, you can do that using `kable` from the `knitr` package. 
Let's recreate the life expectancy table from earlier.  

```r
read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)
lifeExp <- read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)
lifeExp$Code <- as.factor(lifeExp$Code)
lifeExpUS <- lifeExp[which((lifeExp$Code) == "USA"), ]
```

Now, we can use `kable()` to create a table.

```r
knitr::kable(lifeExp)
```

There are a few options for the `kable` function:

```{r echo = FALSE, results = 'asis'}
kable_opts <- data.frame(arg = c("`colnames`",
                                 "`align`",
                                 "`caption`",
                                 "`digits`"),
                         expl = c("Column names (default: column name in the dataframe)",
                                  "A vector giving the alignment for each column ('l', 'c', 'r')",
                                  "Table caption",
                                  "Number of digits to round to. If you want to round columns different amounts, use a vector with one element for each column."))
pander::pandoc.table(kable_opts, split.cells = c(10, 50),
               justify = "rl", style = "multiline")
```

```{r}
my.df <- data.frame(letters = c("a", "b", "c"),
                numbers = rnorm(3))
kable(my.df, digits = 2, align = c("r", "c"),
      caption = "My new table", 
      col.names = c("First 3 letters", 
                    "First 3 numbers"))
```

From Yihui:

>"**Want more features?** No, that is all I have. You should turn to other packages for help. I'm not
going to reinvent their wheels."

If you want to do fancier tables, you may want to explore the `xtable` and `pander` packages. As a note, these might both be more effective when compiling to pdf, rather than html.
