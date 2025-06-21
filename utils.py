def parse_log_file(log_data):
    summary = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    for line in log_data.splitlines():
        if "ERROR" in line:
            summary["ERROR"] += 1
        elif "WARNING" in line:
            summary["WARNING"] += 1
        elif "INFO" in line:
            summary["INFO"] += 1

    return summary