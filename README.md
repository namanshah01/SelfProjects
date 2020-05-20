# Self Projects

Projects I create based on skills and concepts learnt.

## Covid-19 Prediction
The first machine learning project i made using a real world dataset.
I used polynomial regression to predict the number of cases for next 7 days.
I have put the original and the updated .csv file in the folder.
You can find the source of information [here](https://ourworldindata.org/coronavirus-source-data).

The project is also updated with new .ipynb file, containing :
- Comparision of the predicted data and actual data with a graph
- The net r-squared value showing the model's efficieny
<p>After comparing the results, the model shows a r-squared value of 0.92.
With this i conclude the project was successful.

## Breast Cancer Prediction
I solved this using 'support vector machines'. The original dataset consists of 30 features,
which when used, gives an accuracy of about 98% with linear and rbf kernels
(check the file Breast_Cancer_Pred(Compare).ipynb for these results).
But for this project, I used feature selection.
<p>Features with a p-value less than or equal to 0.05 were only selected.
Applying selection was a success as, 5 selected features were able to deliver results that were
significantly close to results with all 30 features.
Find the dataset (breast_cancer_data.csv) and the code (Breast_Cancer_Prediction.ipynb), in the folder.
<p>I conclude the project to be successful with an accuracy score of about 95% with the linear kernel.

## Red Wine Quality
Originally i meant to solve this as a KNN problem, but it wasn't giving good accuracy.
I have now solved it with 'random forest regression.
I tried to apply feature selection to this, but it didn't end up giving good results.
<p>The model is giving an overall accuracy of 73.75%.
I have included a confusion matrix for a more detailed insight into the results.

## Menu Driven Program
A mini-project i made using basic python concepts :
- Functions
- Object Oriented Programming
- File Handling
<p>It is a program that program stores user information(name, roll number and address) in a text file.
The user can add, update, search or delete the records present.
  
## Personal Detail Form
This is a GUI project i made a while ago, it's a form filling system made with importing tkinter.
It makes use of many methods like, a dropdown box, check button, radio button and messageboxes.
It's a dummy program, that is, the information storing system,
and a way to access it through GUI itself is yet to be added in it.
