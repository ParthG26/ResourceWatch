# ResourceWatch

**ResourceWatch** is a web-based application designed to track the resource usage of Docker containers in real-time. This tool provides an intuitive interface to visualize and monitor the CPU and memory consumption of running containers, helping developers and system administrators ensure that their containers are operating within predefined resource limits. With automatic alerts triggered when resource thresholds are exceeded, this project aids in optimizing resource allocation and avoiding over-consumption, ensuring smoother performance for containerized applications.

## Key Features:
- **Real-Time Monitoring:** Continuously monitor Docker containers’ CPU and memory usage with live, interactive charts that update at regular intervals.
- **Alerts for Resource Limits:** Set custom CPU and memory usage limits. When a container exceeds these limits, the tool raises an alert to notify you of potential resource over-consumption.
- **Visual Representation:** Dynamic line charts powered by Chart.js allow easy tracking of resource usage over time, with annotation features to clearly mark alert thresholds.
- **Resource Control Buttons:** Manually simulate memory consumption and control the memory-consuming processes using built-in start and stop buttons for testing purposes.
- **Responsive and Interactive UI:** Built with HTML, CSS, and JavaScript, the UI is easy to use and responsive, ensuring a seamless experience across devices.
- **Backend Integration:** The backend is powered by Flask, which interacts with Docker and the system to gather resource metrics using `psutil`. This ensures efficient and reliable data collection.

## Tech Stack:
- **Flask**: A lightweight web framework for building the backend and API endpoints.
- **Docker**: Used to create and manage containers that are monitored for resource usage.
- **psutil**: Python library used for retrieving information on system utilization (CPU, memory, etc.).
- **Chart.js**: A powerful JavaScript library for creating beautiful, interactive charts that visualize the real-time data.
- **HTML/CSS**: For building the responsive and user-friendly frontend interface.

## How It Works:
1. The Flask application interacts with Docker using the `docker` Python library to track containers running on the system.
2. **psutil** retrieves real-time metrics such as CPU and memory usage for each container.
3. Data is sent to the frontend where **Chart.js** visualizes it in the form of live updating charts.
4. Users can set resource limits, and if the system detects that a container’s usage exceeds the threshold, a visual alert is displayed on the dashboard.
5. Optional buttons allow users to simulate memory-intensive tasks and stop those tasks to observe how the system responds to changes in resource consumption.

## Usage:

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/docker-resource-monitor.git
cd docker-resource-monitor

