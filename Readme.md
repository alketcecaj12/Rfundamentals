# Fundamentals of R

A structured, hands-on introduction to the R programming language, covering the core skills needed to load, manipulate, visualize, and analyze data. All examples use the `state_trends` dataset — a real-world compilation of US state-level personality, Google Trends, and sports data.

---

## Repository Structure

```
Rfundamentals/
├── R_code/          # All R scripts, organized by topic
├── data/            # Dataset files used throughout
│   ├── state_trends.csv
│   ├── state_trends.xlsx
│   └── state_trends code book.txt
└── README.md
```

---

## Dataset: `state_trends`

All scripts load data from the `data/` folder. The dataset covers the **48 contiguous US states** and has four categories of variables:

| Category | Variables |
|---|---|
| **Geographic** | `state`, `state_code`, `population`, `sq_miles`, `pop_density`, `region` |
| **Personality** | `psych_region`, `psy_reg`, `extraversion`, `agreeableness`, `conscientiousness`, `neuroticism`, `openness` |
| **Google Trends** (0–100 score, 2017–2022) | `data_science`, `artificial_intelligence`, `machine_learning`, `data_analysis`, `business_intelligence`, `spreadsheet`, `statistics`, `art`, `dance`, `museum`, `basketball`, `football`, `baseball`, `soccer`, `hockey` |
| **Sports teams** (0/1 flags) | `has_nba`, `has_nfl`, `has_mlb`, `has_mls`, `has_any`, `has_nhl` |

See `data/state_trends code book.txt` for full variable descriptions and sources.

---

## Scripts

Scripts are numbered by chapter and section. Run them in order for a progressive learning experience.

---

### Chapter 2 — R Basics

#### `02_04_Navigating.R` — Getting Started with RStudio

Introduces the RStudio interface and the `$` operator for accessing variables within a data frame.

```r
library(datasets)
df <- iris
head(df)

# Access a variable with $
hist(df$Sepal.Width, main = "Iris Sepal Width", xlab = "Sepal Width (in cm)")
```

**Key concepts:** loading packages, `head()`, `hist()`, the `$` operator.

---

#### `02_05_EnteringData.R` — Entering Data and Basic Math

Covers variable assignment, combining values into vectors, sequences, and arithmetic operations.

```r
a <- 1                    # Assign a single value
x <- c(1, 2, 5, 9)       # Combine into a vector
seq(20, -10, by = -3)     # Generate a sequence
x + y                     # Element-wise addition
2^6                        # Exponentiation
log10(100)                 # Base-10 logarithm
```

**Key concepts:** `<-` assignment, `c()`, `seq()`, arithmetic operators, `sqrt()`, `log()`.

---

#### `02_06_DataTypes.R` — Data Types and Data Structures

Covers R's core data types (numeric, character, logical) and its main data structures.

| Structure | Dimensions | Types allowed |
|---|---|---|
| Vector | 1D | One type only |
| Matrix | 2D | One type only |
| Array | nD | One type only |
| Data Frame | 2D | Mixed types |
| List | Flexible | Any type, any length |

```r
# Vectors
v1 <- c(1, 2, 3, 4, 5)
v2 <- c("a", "b", "c")
v3 <- c(TRUE, FALSE, TRUE)

# Data Frame (most common)
df2 <- data.frame(vNumeric, vCharacter, vLogical)

# Type coercion
coerce3 <- as.integer(5)
coerce5 <- as.numeric(c("1", "2", "3"))
coerce7 <- as.data.frame(matrix(1:9, nrow = 3))
```

**Key concepts:** `typeof()`, `is.vector()`, `is.matrix()`, `is.data.frame()`, `cbind()`, `data.frame()`, `list()`, type coercion with `as.*()` functions.

---

#### `02_07_Comments.R` — Comments and Code Organisation

Demonstrates how to use comments for documentation and to disable code, and how to structure scripts with section headers.

```r
# THIS IS A LEVEL 1 HEADER #################################
## This Is a Level 2 Header ================================
### This is a level 3 header. ------------------------------
```

**Key concepts:** `#` for comments, section headers for document outline navigation in RStudio.

---

#### `02_08_WorkingWithPackages.R` — Managing Packages

Explains how to install, load, and remove packages. Covers the difference between `library()` and `require()`, and how to call a function without loading its package.

```r
install.packages("pacman")     # Install a package
library(pacman)                # Load (errors if missing)
require(pacman)                # Load (warns if missing)
pacman::p_data(datasets)       # Use function without loading
detach("package:pacman", unload = T)  # Unload package
remove.packages("pacman")      # Remove from library
```

**Key concepts:** `install.packages()`, `library()`, `require()`, `package::function` notation, `detach()`, `remove.packages()`.

---

#### `02_11_SampleDatasets.R` — Built-in Datasets

Shows how to browse and explore R's built-in datasets package.

```r
library(help = "datasets")  # List all built-in datasets
?iris                        # Documentation for iris
?Titanic                     # Documentation for Titanic
```

**Key datasets explored:** `iris`, `UCBAdmissions`, `Titanic`, `state.x77`, `swiss`.

---

#### `02_12_ImportingData.R` — Importing Data

Covers reading CSV and Excel files using the `tidyverse` ecosystem.

```r
library(tidyverse)
library(readxl)

# Import CSV
df <- read_csv("data/state_trends.csv")

# Import Excel with transformations
df2 <- read_excel("data/state_trends.xlsx", sheet = "all_data") |>
  as_tibble() |>
  select(state_code, psych_region, extraversion:openness) |>
  rename(y = psych_region) |>
  mutate(y = as.factor(y))
```

**Key concepts:** `read_csv()`, `read_excel()`, `glimpse()`, tibbles vs data frames, the pipe `|>`.

---

### Chapter 3 — Data Visualization

#### `03_01_Colors.R` — Using Colors in R

Demonstrates the multiple ways to specify colors in R base graphics.

```r
colors()                          # List of 657 color names
barplot(x, col = "red3")          # By name
barplot(x, col = "#CD0000")       # By hex code
barplot(x, col = rgb(.80, 0, 0))  # By RGB (0–1 scale)
barplot(x, col = rainbow(6))      # Palette
```

**Key concepts:** color names, RGB triplets, hex codes, `palette()`, built-in palettes (`rainbow`, `heat.colors`, `terrain.colors`, `topo.colors`, `cm.colors`).

---

#### `03_02_BarCharts.R` — Bar Charts

Covers frequency bar charts, stacked bar charts, and side-by-side bar charts using base R and `tidyverse` pipes.

```r
# Simple frequency bar
df |> select(psy_reg) |> table() |> barplot()

# Sorted with options
df |> select(psy_reg) |> table() |> sort(decreasing = F) |>
  barplot(main = "Personalities of 48 US States", horiz = T, col = "#CD0000")

# Stacked and side-by-side
df_t |> barplot(legend = rownames(df_t))          # Stacked
df_t |> barplot(legend = rownames(df_t), beside = T)  # Side-by-side
```

**Key concepts:** `plot()`, `barplot()`, `table()`, `sort()`, `beside`, `horiz`, stacked vs. grouped bar charts.

---

#### `03_03_Histograms.R` — Histograms and Density Plots

Shows how to build histograms and density plots for continuous variables.

```r
hist(df$data_science, breaks = 7, col = "#CD0000", border = NA)

# Density plot
df |> pull(data_science) |> density() |> plot()
df |> pull(data_science) |> density() |> polygon(col = "#CD0000")
```

**Key concepts:** `hist()`, `breaks`, `density()`, `plot()`, `polygon()` for filled density curves, `pull()` vs `select()`.

---

#### `03_04_BoxPlots.R` — Box Plots

Covers single-variable boxplots, multi-variable boxplots, and grouped boxplots. Also demonstrates how to identify outliers.

```r
boxplot(df$dance, horizontal = T, notch = T, col = "#CD0000")

# Identify outliers
df |> filter(dance > 90) |> select(state, dance)

# Boxplot by group
df |> select(has_nhl, hockey) |> plot()
```

**Key concepts:** `boxplot()`, `notch` (confidence interval for median), outlier detection with `filter()`, grouped boxplots.

---

#### `03_05_Scatterplots.R` — Scatterplots

Covers bivariate and multivariate scatterplots, point styling, and adding a regression line.

```r
# All pairwise associations
df |> plot()

# Bivariate with options
df |> select(soccer, hockey) |>
  plot(main = "Scatterplot", col = "red3", pch = 20)

# Add linear regression line
lm(df$hockey ~ df$soccer) |> abline()
```

**Key concepts:** `plot()`, `pch` (plotting character), `abline()`, `lm()` for trend lines.

---

#### `03_06_LineCharts.R` — Line Charts / Time Series

Demonstrates time series visualization with single and multiple series.

```r
plot(uspop)                        # Single series
ts.plot(EuStockMarkets, col = rainbow(4))  # Multiple series

legend("topleft",
  legend = colnames(EuStockMarkets),
  col    = rainbow(4),
  lty    = 1
)
```

**Key concepts:** `plot()`, `ts.plot()`, `plot.ts()`, `legend()`, `abline()`, `text()` for annotations. Built-in datasets: `uspop`, `EuStockMarkets`.

---

#### `03_07_ClusterCharts.R` — Hierarchical Clustering Dendrogram

Shows how to compute hierarchical clusters and visualise them as a dendrogram.

```r
hc <- df |> dist() |> hclust()
hc |> plot(labels = df$state_code)
hc |> rect.hclust(k = 3, border = 2:4)  # Draw cluster boxes
```

**Key concepts:** `dist()` (distance matrix), `hclust()` (agglomerative clustering), `rect.hclust()` for cluster boundaries.

---

### Chapter 4 — Data Manipulation

#### `04_01_Selecting.R` — Filtering and Selecting Data

Covers subsetting rows by single and multiple conditions using `tidyverse`.

```r
# Single condition
df |> filter(data_analysis > 50) |> arrange(desc(data_analysis))
df |> filter(psych_region == "Relaxed and Creative")

# Multiple conditions
df |> filter(region == "South" | psych_region == "Relaxed and Creative")  # OR
df |> filter(region == "South" & psych_region == "Relaxed and Creative")  # AND
df |> filter(region == "South" & !psych_region == "Relaxed and Creative") # NOT
```

**Key concepts:** `filter()`, `select()`, `arrange()`, `desc()`, logical operators `|`, `&`, `!`, `print(n = Inf)`.

---

#### `04_02_Recoding.R` — Recoding Variables

Shows how to collapse or reassign categories using `recode()` and how to create new binary variables with `case_when()`.

```r
# Recode existing categories
df |> mutate(relaxed = recode(psych_region,
  "Relaxed and Creative"     = "yes",
  "Friendly and Conventional" = "no",
  .default = "no"))

# Create categories from numeric conditions
df |> mutate(
  like_arts = case_when(
    art > 75 | dance > 75 | museum > 75 ~ "yes",
    TRUE ~ "no"
  )
)
```

**Key concepts:** `mutate()`, `recode()`, `case_when()`, `.default` for unmatched values.

---

#### `04_03_NewVariables.R` — Creating New Variables

Covers computing row-wise averages across variables and reverse-coding Likert-scale items.

```r
# Row means (ignoring NAs)
df |> mutate(
  mean_xy  = rowMeans(across(x:y), na.rm = T),
  mean_xyz = rowMeans(across(x:z), na.rm = T)
)

# Reverse coding (1–7 scale → 8 - x)
df |> mutate(y_r = 8 - y)
```

**Reverse coding reference:**

| Scale | Formula |
|---|---|
| 1–7 | `8 - x` |
| 1–10 | `11 - x` |
| 0–5 | `5 - x` |
| −n to +n | `x * -1` |

**Key concepts:** `rowMeans()`, `across()`, `na.rm`, reverse coding patterns, the `psych` package for advanced options.

---

### Chapter 5 — Statistical Analysis

#### `05_01_Frequencies.R` — Frequency Tables

Covers summarising categorical variables and factors.

```r
summary(df)                        # Frequencies for factors
df |> select(region) |> table()    # Frequency table for character
df |> select(psych_region) |> summary()  # Preferred for factors
```

**Key concepts:** `summary()`, `table()`, character vs. factor variables, `as_factor()`, `mutate(across(...))`.

---

#### `05_02_Descriptives.R` — Descriptive Statistics

Covers summary statistics, Tukey's five-number summary, and boxplot statistics.

```r
df |> summary()
df |> select(statistics) |> summary()

fivenum(df$statistics)            # Min, Q1, median, Q3, max
boxplot.stats(df$statistics)      # Hinges, n, CI, outliers
```

**Key concepts:** `summary()`, `fivenum()`, `boxplot()`, `boxplot.stats()`. The `psych` package is recommended for extended descriptive statistics.

---

#### `05_03_Correlations.R` — Correlation Analysis

Covers correlation matrices, scatterplot matrices, and significance testing for individual pairs.

```r
df |> cor()                        # Correlation matrix
df |> cor() |> round(2)            # Rounded

# Test single correlation: gives r, p-value, and 95% CI
cor.test(df$DS, df$DA)
```

**Key concepts:** `cor()`, `cor.test()`, `round()`. Recommended packages for p-value matrices: `Hmisc`, `rstatix`.

---

#### `05_04_Regression.R` — Linear Regression

Covers bivariate and multiple linear regression, model diagnostics, and prediction.

```r
# Bivariate
fit1 <- lm(df$data_science ~ df$openness)
summary(fit1)
confint(fit1)
predict(fit1, interval = "prediction")
influence.measures(fit1)

# Multiple regression (three equivalent formulations)
lm(df)
lm(data_science ~ ., data = df)
lm(data_science ~ extraversion + agreeableness +
   conscientiousness + neuroticism + openness, data = df)
```

**Key concepts:** `lm()`, model formula syntax (`y ~ x`), `summary()`, `confint()`, `predict()`, `lm.influence()`, `influence.measures()`.

---

#### `05_05_Contingency.R` — Contingency Tables and Chi-Squared

Covers cross-tabulation of two categorical variables, percentage breakdowns, and the chi-squared test of independence.

```r
ct <- table(df$region, df$psy_reg)   # Contingency table

ct |> prop.table(1) |> round(2) * 100  # Row %
ct |> prop.table(2) |> round(2) * 100  # Column %
ct |> prop.table()  |> round(2) * 100  # Total %

tchi <- chisq.test(ct)
tchi$observed   # Observed frequencies
tchi$expected   # Expected frequencies
tchi$residuals  # Pearson residuals
tchi$stdres     # Standardised residuals
```

**Key concepts:** `table()`, `prop.table()`, `chisq.test()`, inspecting chi-squared object components.

---

## Prerequisites

- R (≥ 4.1): https://cran.r-project.org
- RStudio: https://posit.co/download/rstudio-desktop

### Required Packages

Install all at once:

```r
install.packages(c("tidyverse", "readxl"))
```

The `datasets` package is included with base R.

---

## Getting Started

```bash
git clone https://github.com/alketcecaj12/Rfundamentals.git
```

Open `Rfundamentals.Rproj` in RStudio, then open any script from the `R_code/` folder. Run lines with `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (macOS).

> **Tip:** Use `Session > Restart R` (`Ctrl+Shift+F10` / `Cmd+Shift+0`) between scripts to clear the environment and unload packages.

---

## Learning Path

```
Chapter 2: R Basics          →  Data types, structures, packages, importing data
Chapter 3: Visualisation     →  Colors, bar charts, histograms, boxplots,
                                scatterplots, line charts, clustering
Chapter 4: Data Manipulation →  Filtering, recoding, creating new variables
Chapter 5: Statistics        →  Frequencies, descriptives, correlations,
                                regression, contingency tables
```

---

## Author

Alket Cecaj — [github.com/alketcecaj12](https://github.com/alketcecaj12)
