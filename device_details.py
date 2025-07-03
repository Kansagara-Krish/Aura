# This is a k python file created by your personal assistant
import psutil
import datetime

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        print("Battery information not available on this system.")
        return None  # Return None to indicate no battery data

    battery_percentage = battery.percent

    # Optional: print status details for user reference
    print(f"Battery Percentage: {battery_percentage}%")

    if battery.power_plugged:
        status = "Full" if battery_percentage == 100 else "Charging"
    else:
        status = "Discharging"
        if battery.secsleft not in [psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN]:
            time_left = str(datetime.timedelta(seconds=battery.secsleft))
            print(f"Time Remaining: {time_left}")

    print(f"Status: {status}")
    return battery_percentage

if __name__ == "__main__":
    try:
        get_battery_status()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure 'psutil' library is installed (pip install psutil).")