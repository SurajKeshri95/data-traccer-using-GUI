import tkinter as tk
import psutil
import csv
from datetime import datetime

class DataUsageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Usage Tracker")

        # Data tracking labels
        self.label_upload = tk.Label(root, text="Upload: 0.00 KB/s", font=("Helvetica", 16))
        self.label_upload.pack(pady=10)

        self.label_download = tk.Label(root, text="Download: 0.00 KB/s", font=("Helvetica", 16))
        self.label_download.pack(pady=10)

        self.label_total = tk.Label(root, text="Total Used: 0.00 MB", font=("Helvetica", 16))
        self.label_total.pack(pady=10)
        
        # Button to view log data
        self.btn_view_log = tk.Button(root, text="View Log", command=self.view_log)
        self.btn_view_log.pack(pady=10)

        # Initialize previous data counters
        self.sent_old, self.recv_old = self.get_data_usage()

        # Initialize CSV file with headers
        with open('data_usage_log.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Upload Speed (KB/s)", "Download Speed (KB/s)", "Total Used (MB)"])

        self.update_stats()

    def get_data_usage(self):
        # Get current network usage statistics
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def log_data(self, timestamp, upload_speed, download_speed, total_used):
        # Append the current network stats to the CSV log file
        with open('data_usage_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, upload_speed, download_speed, total_used])

    def update_stats(self):
        sent_new, recv_new = self.get_data_usage()

        # Calculate speeds in KB/s and total data used in MB
        upload_speed = (sent_new - self.sent_old) / 1024
        download_speed = (recv_new - self.recv_old) / 1024
        total_used = (sent_new + recv_new) / (1024 * 1024)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_data(timestamp, upload_speed, download_speed, total_used)

        self.label_upload.config(text=f"Upload: {upload_speed:.2f} KB/s")
        self.label_download.config(text=f"Download: {download_speed:.2f} KB/s")
        self.label_total.config(text=f"Total Used: {total_used:.2f} MB")

        self.sent_old, self.recv_old = sent_new, recv_new

        # Update stats every second
        self.root.after(1000, self.update_stats)

    def view_log(self):
        # Create a new window for viewing the log
        log_window = tk.Toplevel(self.root)
        log_window.title("Log Data")

        # Create a Text widget with horizontal and vertical scrollbars
        text_widget = tk.Text(log_window, wrap='none', font=("Courier", 10))
        text_widget.pack(expand=True, fill='both')

        scrollbar_y = tk.Scrollbar(log_window, orient='vertical', command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.pack(side='right', fill='y')

        scrollbar_x = tk.Scrollbar(log_window, orient='horizontal', command=text_widget.xview)
        text_widget.configure(xscrollcommand=scrollbar_x.set)
        scrollbar_x.pack(side='bottom', fill='x')

        try:
            with open('data_usage_log.csv', 'r') as file:
                data = file.read()
            text_widget.insert(tk.END, data)
        except FileNotFoundError:
            text_widget.insert(tk.END, "Log file not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataUsageApp(root)
    root.mainloop()
