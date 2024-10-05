from flask import Flask, render_template, jsonify
import docker
import psutil

app = Flask(__name__)
client = docker.from_env()

def get_container_stats(container_name):
    try:
        container = client.containers.get(container_name)
        stats = container.stats(stream=False)
        
        cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
        system_delta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
        cpu_usage = (cpu_delta / system_delta) * psutil.cpu_count() * 100.0
        
        memory_usage = stats['memory_stats']['usage'] / (1024 * 1024)  # Convert to MB
        
        return {
            'cpu_usage': round(cpu_usage, 2),
            'memory_usage': round(memory_usage, 2)
        }
    except Exception as e:
        print(f"Error getting stats: {e}")
        return {'cpu_usage': 0, 'memory_usage': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_consumer')
def start_consumer():
    try:
        client.containers.get('memory_consumer').start()
        return jsonify({"status": "started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/stop_consumer')
def stop_consumer():
    try:
        client.containers.get('memory_consumer').stop()
        return jsonify({"status": "stopped"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/check_resources')
def check_resources():
    return jsonify(get_container_stats('memory_consumer'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)