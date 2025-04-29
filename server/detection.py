def detect_anomaly(data):
    alerts = []

    cpu = data.get("cpu_usage")
    memory = data.get("memory_usage")

    if cpu is not None and cpu > 80:
        alerts.append(f"High total CPU usage: {cpu}%")
    if memory is not None and memory > 80:
        alerts.append(f"High total Memory usage: {memory}%")

    processes = data.get("processes", [])
    for proc in processes:
        if proc.get("cpu_percent") is not None and proc["cpu_percent"] > 50:
            alerts.append(f"Process {proc.get('name')} (PID {proc.get('pid')}) uses high CPU: {proc['cpu_percent']}%")
        if proc.get("memory_percent") is not None and proc["memory_percent"] > 30:
            alerts.append(f"Process {proc.get('name')} (PID {proc.get('pid')}) uses high Memory: {proc['memory_percent']}%")

    return alerts if alerts else None
