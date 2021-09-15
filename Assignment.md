# Assignment for Senior Capstone hardware miniproject

Please make your "report" as a text/markdown file "Report.md" in your GitHub miniproject repository.
Just a couple paragraphs is fine.
We are mainly interested in that you could get the Pi running and measuring, and you can plot the data by transferring the data to your laptop and plotting.

1. [Install Raspberry Pi OS](./RaspberryPiSetup.md) to your Raspberry Pi microSD card
2. Ensure you can run the [wifi_scan.py](./wifi_scan.py) on your Raspberry Pi, and that it creates JSON data files. We suggest doing this in the Senior Design lab near the window (collecting data from cars on the highway).
3. Copy the JSON data collected to your laptop. Ideally collect 15+ minutes of data so the plots are more meaningful.
4. Make a Report.md as noted above in your GitHub mini-project repository, with the plots you generated via [wifi_plot.py](./wifi_plot.py) and any explanation/difficulties/discussion on your miniproject results.

Report for assignment for Senior Capstone hardware miniproject

1.	To begin with, we followed the instruction on how to set up the raspberry pi following the instructions provided and were able to make it work. However, the next time we went to the lab the rasppi would not start and we noticed that the green light was not turning on and after some troubleshooting, we were able to fix the problem.
2.	Also, we installed the updates needed for the raspberry pi and run the first python code ble_scan.py. We were able to observe the data collected and get more familiar with the python code. Then, we decided to run wifi_scan.py and observe all the data information collected. One important thing we learned is how to run python codes through the terminal, which will become helpful once we are working on the senior design projects.
3.	We then run the wifi_scan.py in the senior design lab and collected data for 100 data points and used wifi_plot.py to observe how the data is plotted (time vs. quantity). The plot showed that at most it was able to detect 8 objects (wifi points) at a time and they were moving relatively fast since the plot did not remain constant for a longer than 2 minutes.
4.	In sum, we were able to familiarize ourselves with the raspberry pi interface (how to set up the OS and connect to a computer via SSH), the python IDE and how to get code running, and think about how data can be collected and organized for multiple purposes. 

