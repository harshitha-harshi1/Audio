import os

def analyze_bus_log(bus_no):
    log_path = fr"C:\Users\HP\Downloads\{bus_no}.log"

    if not os.path.isfile(log_path):
        print(f" Log file not found for bus {bus_no}: {log_path}")
        return

    # Read file content
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Check for audio announcement
    audio_announcement = any("audio announcement" in line.lower() or "announcement" in line.lower() for line in lines)

    # Extract stops
    stops = []
    for line in lines:
        if "pending stops" in line.lower():
            stop_text = line.split("pending stops", 1)[-1]
            candidates = stop_text.replace(",", ";").split(";")
            for stop in map(str.strip, candidates):
                if stop and stop not in stops:
                    stops.append(stop)

    # Print results
    print(f"\n Bus No: {bus_no}")
    print(" Audio Announcement:", "YES" if audio_announcement else "NO")

    if stops:
        print(" Pending Stops:")
        for s in stops:
            print("   -", s)

        print("\n➡ Journey Progression:")
        for i, stop in enumerate(stops):
            if i < len(stops) - 1:
                print(f" Current Stop: {stop} → Next Stop: {stops[i+1]}")
            else:
                print(f" Final Stop Reached: {stop}")
    else:
        print(" No pending stops found")


# Run the program
if __name__ == "__main__":
    bus_no = input("Enter Bus Number: ").strip()
    analyze_bus_log(bus_no)
