# data-traccer-using-GUI

This is a Python-based GUI Data Tracker that allows users to monitor system resources like CPU usage, memory usage, and network activity in real-time. It includes a simple and user-friendly graphical interface built using Tkinter (or PyQt, depending on your choice).

✅ Features
Built with Python and GUI (Tkinter or PyQt)

Real-time display of:

🔹 CPU usage

🔹 Memory usage

🔹 Network upload/download speed

Live updating charts or labels

Option to export tracked data to .csv

Adjustable tracking interval

Easy-to-use interface for both beginners and advanced users

🛠️ Technologies Used
Python 3.x

GUI Framework: Tkinter (or PyQt5)

psutil – to fetch system stats

matplotlib (optional) – for real-time plotting

csv, datetime, time – for logging and time control

🧑‍💻 How to Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/data-tracker-gui.git
cd data-tracker-gui
2. Install Required Packages
bash
Copy
Edit
pip install psutil
# If using PyQt:
# pip install pyqt5
# If using matplotlib for charts:
# pip install matplotlib
3. Run the Application
bash
Copy
Edit
data_tracker_gui.py
🖥️ Interface Overview
CPU, Memory, and Network usage displayed live

Start/Stop tracking with a button

Save log to .csv file

Set custom time intervals via input field

📁 Sample Output Log
scss
Copy
Edit
Timestamp,CPU_Usage(%),Memory_Usage(%),Upload(KB),Download(KB)
2025-06-09 16:25:30,15.3,42.7,102.4,88.9
2025-06-09 16:25:35,16.8,43.2,110.5,90.1
🧰 Use Cases
Desktop resource monitoring tool

Helpful for developers and system admins

Educational tool to learn system performance tracking

Basis for more complex monitoring dashboards

🚀 Future Enhancements
Add dark/light theme switch

Enable notifications for high resource usage

Export logs to PDF

Cloud sync of logs

Optional background mode

