An advanced version of the shop_report script purely written in python, that utilizes pandas to process draft-data for analytic purposes.

Generates a report with data from an external CSV-file containing useful information about a shops inventory e. g. which product performs the best or how likely it is to become rare and has to be restocked.

When this was written I realized how powerful data-analyses can be and what an impact it has on the efficiency of a company's resources and their utilization. It gave me a lot of ideas how process optimization works taking in consideration sensors, reports, datasets - basically collecting all the data you can possibly collect and understand your assets better and where the best point of leverage might be. 
The code can be seen as a placeholder for much more complex operations in a completely different scenario but also involving draft analyses. Maybe you have a milling machine that needs monitoring and this code will help you reduce the wear of certain parts. 
If you're an experienced data scientist this might not be new to you, but for me coming to this realization was a big step and it made my curiosity in data science grow even more. 

Visualization / diagram / video

This tool is written on Debian and should work with other Linux distributions as well. But not yet tested.

To install just copy the folder csv_report to your drive and make the main.py executable.

How it works:
main.py imports the defined modules in reports.py where the actual logic is happening. Running main prints a shop-report analyzing the inventory.csv file. As I mentioned the code can be seen as a placeholder. At this point it can prompt reports based on the customized modules and the CSV as the input. All data of the CSV-file can be accessed, added and tampered with depending on your goal.

How to tweak this project for your own uses?
Since this is an example project, I'd encourage you to clone and rename it to use it for you own purpose.

Found a bug?
The code is not debugged, because the script is not used in the wild, but I might consider working on common errors that may occur. If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

Known issues:
Feel free to find some :)

End of README.md
