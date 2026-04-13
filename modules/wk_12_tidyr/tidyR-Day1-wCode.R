# The data is part of the supplemental material released with the paper
# Paper: https://onlinelibrary.wiley.com/doi/10.1111/ele.70296
# Data and code: https://figshare.com/articles/journal_contribution/Sex_ratio_bias_triggers_demographic_suicide_in_a_dense_tortoise_population/30752687

# It seems it is not possible to download programatically, therefore I am
# downloading and unzipping the file into
# data-raw/Sex_ratio_bias_triggers_demographic_suicide-main/R/input in two files
# body_condition.csv and clutch_size.csv

#Step 1: download data file into your current working directory 
#best to make cwd a new folder for this week's class!
getwd()


# Read in body_condition.csv
tortoise_body_condition <- readr::read_csv(
  "Sex_ratio_bias_triggers_demographic_suicide-main/R/input/body_condition.csv"
)

# read in clutch_size.csv
clutch_size <- readr::read_csv(
  "Sex_ratio_bias_triggers_demographic_suicide-main/R/input/clutch_size.csv"
)


#fixing 1, 2, 3, and 4 (removing unwanted columns)
names(tortoise_body_condition) #look at what we have

tortoise_body_condition %>% #can also use |>
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>%
  names() #did it do what we wanted?

#fix 5 -- grouping by individual
View(tortoise_body_condition) #look at our whole dataframe

length(which(tortoise_body_condition$ind == 1)) #how many rows belong to individual 1?

tortoise_body_condition %>% group_by(ind) %>% summarise(n = n()) #how many rows belong to each individual?

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) #makes sure all individuals' rows are right after the other now

#fix 6 -- sorting by year_recode
head(tortoise_body_condition$year_recode) #not currently ordered

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% #makes sure all individuals' rows are right after the other now
  arrange(year_recode, .by_group = TRUE) %>% #ascending year_recode; .by_group option keeps individuals grouped together 
  head() #did this fix it?

#fix 7 -- rename columns
names(tortoise_body_condition) #what do the abbreviations mean? --> have to get from paper

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% #makes sure all individuals' rows are right after the other now
  arrange(year_recode, .by_group = TRUE) %>% #ascending year_recode; .by_group option keeps individuals grouped together 
  ungroup() %>% #let's remove our grouping to prevent potential issues with later analysis
  rename(
    straight_carapace_length_mm = SCL,
    body_mass_grams = BM, # we are assuming it's grams
    body_condition_index = BCI,
    individual = ind,
    locality = loc
  ) %>% # new column name = old column name
  names() #did this fix it?

#fix 8 -- change order of columns
names(tortoise_body_condition) #what is the current order?

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% 
  arrange(year_recode, .by_group = TRUE) %>% 
  ungroup() %>% 
  rename(
    straight_carapace_length_mm = SCL,
    body_mass_grams = BM, 
    body_condition_index = BCI,
    individual = ind,
    locality = loc
  ) %>% 
  relocate(
    individual,
    year,
    year_recode,
    season,
    locality,
    sex,
    body_mass_grams,
    body_condition_index,
    straight_carapace_length_mm
  ) %>% #put column names in the order you want them in
  names() #did this fix it?

#fix 9 -- recode 'locality' column values
tortoise_body_condition %>% select(loc) %>% unique() #what are all options of loc?

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% 
  arrange(year_recode, .by_group = TRUE) %>% 
  ungroup() %>% 
  rename(
    straight_carapace_length_mm = SCL,
    body_mass_grams = BM, 
    body_condition_index = BCI,
    individual = ind,
    locality = loc
  ) %>% 
  relocate(
    individual,
    year,
    year_recode,
    season,
    locality,
    sex,
    body_mass_grams,
    body_condition_index,
    straight_carapace_length_mm
  ) %>% 
  mutate( #creates new column(s)
    locality = locality %>% #save new column to same name as old column (rewrites old column). can also give new column a new name and remove old column (via select()), but this maintains the names we added in a previous step
      recode_values( #expand one letter values to full word values
        "b" ~ "Beach",
        "p" ~ "Plateau",
        "k" ~ "Konjsko"
      )
  ) %>%
  select(locality) %>%
  unique() #did this fix it?

#fix 10 -- recode 'season' column values
tortoise_body_condition %>% select(season) %>% unique() #what are all options of season?

tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% 
  arrange(year_recode, .by_group = TRUE) %>% 
  ungroup() %>% 
  rename(
    straight_carapace_length_mm = SCL,
    body_mass_grams = BM, 
    body_condition_index = BCI,
    individual = ind,
    locality = loc
  ) %>% 
  relocate(
    individual,
    year,
    year_recode,
    season,
    locality,
    sex,
    body_mass_grams,
    body_condition_index,
    straight_carapace_length_mm
  ) %>% 
  mutate( #creates new column(s)
    locality = locality %>% #save new column to same name as old column (rewrites old column). can also give new column a new name and remove old column (via select()), but this maintains the names we added in a previous step
      recode_values( #expand one letter values to full word values
        "b" ~ "Beach",
        "p" ~ "Plateau",
        "k" ~ "Konjsko"
      )
  ) %>%
  mutate(
    season = season |>
      dplyr::recode_values(
        "sum" ~ "Summer",
        "sp" ~ "Spring"
      )
  ) %>%
  select(season) %>%
  unique() #did this fix it?


#save cleaned df to a new object
tortoise_body_condition_cleaned <- tortoise_body_condition %>%
  dplyr::select(-c(...1, res, log_BCI, loc_sex_cohort)) %>% #fixes 1, 2, 3, and 4
  group_by(ind) %>% 
  arrange(year_recode, .by_group = TRUE) %>% 
  ungroup() %>% 
  rename(
    straight_carapace_length_mm = SCL,
    body_mass_grams = BM, 
    body_condition_index = BCI,
    individual = ind,
    locality = loc
  ) %>% 
  relocate(
    individual,
    year,
    year_recode,
    season,
    locality,
    sex,
    body_mass_grams,
    body_condition_index,
    straight_carapace_length_mm
  ) %>% 
  mutate( #creates new column(s)
    locality = locality %>% #save new column to same name as old column (rewrites old column). can also give new column a new name and remove old column (via select()), but this maintains the names we added in a previous step
      recode_values( #expand one letter values to full word values
        "b" ~ "Beach",
        "p" ~ "Plateau",
        "k" ~ "Konjsko"
      )
  ) %>%
  mutate(
    season = season |>
      dplyr::recode_values(
        "sum" ~ "Summer",
        "sp" ~ "Spring"
      )
  )

#####
#clutch size dataset

#SAK REMOVE FOLLOWING CODE FROM RMD FOR STUDENTS!
rename(
  individual = ind,
  locality = Locality,
  straight_carapace_length_mm = SCL,
  body_mass_grams = BM,
  eggs = Eggs,
  date = Date,
  age = Age
) %>%
  mutate(date = as.Date(date, origin = "1899-12-30")) %>%
  relocate(
    individual,
    age,
    date,
    locality,
    eggs,
    body_mass_grams,
    straight_carapace_length_mm
  )