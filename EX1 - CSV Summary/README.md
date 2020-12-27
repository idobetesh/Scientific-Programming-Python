# Scientific-Programming-Python-CSV-Summary 🐍

Creating a summary file to spec for a given CSV table file. 
The CSV file contains columns that can be either categorical, textual, or numerical features. Additionally, a JSON file with feature specs is attached. 
The JSON file will define the requested output: there will be one “groupby” feature, and for each other feature it will contain the requested behavior for the “group” (i.e. what aggregate function must be run on the column per group created). 
Textual columns will be discarded.
