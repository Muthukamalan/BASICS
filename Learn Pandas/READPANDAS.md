# Effective Pandas
## Pattern for Data Manipulation

### Intro
- [X] Data 

### Data Structure
- [X] Summary

### Series
- [X] Index abstraction
- [X] pandas Series
- [X] NaN value
- [X] Optional Integer Support for NaN
- [X] Similar to Numpy
- [X] Categorical Data

### Series Deep Dive
- [X] Loading the Data
- [X] Series Attributes

### Operators(& Dunder Methods)
- [X] Intro
- [X] Dunder Methods
- [X] Index Alignment
- [X] Broadcasting
- [X] Iteration
- [X] Operator Methods
- [X] Chaining

### Aggregate Methods
- [X] Aggregation
- [X] Count and Mean of an Attribute
- [X] .agg and Aggregation Strings

### Conversion Methods
- [X] Automatic Conversion
- [X] Memory Usage
- [X] String and Category Types
- [X] Ordered Categories
- [X] Converting to Other Types

### Manipulation Methods
- [X] .apply and .where
- [X] If Else
- [X] Missing Data
- [X] Filling in Missing Data
- [X] Interpolating Data
- [ ] Clipping 
- [ ] Sorting Value
- [ ] Sorting the Index
- [ ] Dropping Duplicates
- [ ] Ranking Data
- [ ] Replacing Data
- [ ] Binning

### Indexing Operations
- [ ] Prepping the Data and Renaming the index
- [ ] Resetting the index
- [ ] .loc Attributes
- [ ] .iloc
- [ ] heads and tails
- [ ] Filtering Index Values
- [ ] Reindexing

### String Manipulation
- [ ] String and Objects
- [ ] Categorical Strings
- [ ] The .str Accessor
- [ ] Searching
- [ ] Splitting
- [ ] Optimizing .apply with Cython
- [ ] Replacing Text

### Date and Time Manipulation
- [ ] Date Theory
- [ ] Loading UTC Time Data
- [ ] Loading Local Time Data
- [ ] Local Time to UTC
- [ ] Converting to Epochs
- [ ] Manipulating Dates

### Dates in the Index
- [ ] Finding the missing data
- [ ] filling in missing data
- [ ] intepolation
- [ ] dropping missing values
- [ ] shifting data
- [ ] rolling average
- [ ] resampling
- [ ] gathering aggregate values(but keeping index)
- [ ] groupby operation
- [ ] cumulative operations

### Plotting with a Series
- [ ] Plotting in jupyter
- [ ] .plot 
- [ ] histogram
- [ ] box
- [ ] kde
- [ ] line
- [ ] line plot with multiple aggregations
- [ ] bar
- [ ] pie
- [ ] styling

### Categorical Manipulation
- [ ] Categorical data
- [ ] Frequency Counts
- [ ] benefits of categories
- [ ] conversion to Ordinal categories
- [ ] .cat accessor
- [ ] category gotchas
- [ ] generalization

### Dataframes
- [ ] database and spreedsheet analogues
- [ ] simple python version
- [ ] Dataframes
- [ ] Construction
- [ ] Dataframe Axis


### Similarities with Series and DataFrame
- [ ] getting the data
- [ ] view data

### Math Methods in DataFrames
- [ ] Index alignment
- [ ] duplicate index

### Looping and Aggregation
- [ ] for loops
- [ ] aggregaions
- [ ] .apply method

### Columns Types, .assign an Memory Usage
- [ ] Conversion methods
- [ ] memory usage

### Creating and Updating Columns
- [ ] Loading the Data
- [ ] more column cleanup

### Dealing with Missing and Duplicated Data
- [ ] Missing data
- [ ] duplicates

### Sorting Columns and Indexes
- [ ] Soring columns
- [ ] Sorting columns Order
- [ ] Setting and Sorting the index

### Filtering and Indexing Operations
- [ ] Renaming an Index
- [ ] Resetting the Index
- [ ] Dataframe Indexing, Filtering & Querying
- [ ] Indexing by Position
- [ ] Indexing 

### Plotting with DataFrames
- [ ] line plots
- [ ] bar
- [ ] scatter
- [ ] area and stacked bar
- [ ] column distributions with KDEs,Histograms and Boxplots


### Reshaping Dataframes with Dummies
- [ ] dummy columns
- [ ] undoing dummy columns

### Reshaping By Pivoting and Grouping
- [ ] Using a custom Aggregation function
- [ ] multiple aggregation
- [ ] per column aggregations
- [ ] grouping by hierarchy
- [ ] grouping with functions


### More Aggregations
- [ ] Aggregation while keeping rows
- [ ] Filtering parts of groups


### Cross-tabulation Deep Dive
- [ ] cross-tabulation
- [ ] adding margins
- [ ] normalizing results
- [ ] hierarchical columns with cross tabulations
- [ ] heatmaps

### Melting, Transpose and Stacking Data
- [ ] melting data
- [ ] Un-melting data
- [ ] Transposing data
- [ ] stacking and Unstacking
- [ ] Flattening hierarchical index and columns


### Working with TimeSeries
- [ ] loading the data
- [ ] adding timezone info
- [ ] exploring the data
- [ ] slicing ts
- [ ] missing ts data
- [ ] exploring seasonality
- [ ] resampling data
- [ ] rules with offset aliases
- [ ] combining offset aliases
- [ ] anchored offset aliases
- [ ] resampling to finger-grain frequency
- [ ] grouping a date column with pd.Grouper



### Joining Dataframes
- [ ] Adding rows to Dataframes
- [ ] Adding cols to Dataframes
- [ ] Joins
- [ ] joins indicators
- [ ] merge validations
- [ ] joining data example
- [ ] dirty devil flow and weather data
- [ ] joining data
- [ ] validating joined data
- [ ] visualization of merged data

### Exporting data
- [ ] Dirty devil data
- [ ] read and write
- [ ] create csv
- [ ] export to ecel
- [ ] feather
- [ ] sql
- [ ] json

### Styling Dataframes
- [ ] Loading the Data
- [ ] Sparklines
- [ ] .style
- [ ] Formatting
- [ ] Embedding Bar plots
- [ ] Highlighting
- [ ] Heatmap and gradients
- [ ] Captions
- [ ] css properties
- [ ] stickiness and hidding
- [ ] hiding the index


### Debugging pandas
- [ ]  Checking if Dataframe are Equal
- [ ] Debugging Chains
- [ ] Debugging Apply
- [ ] Memory Usage
- [ ] Timing Info
