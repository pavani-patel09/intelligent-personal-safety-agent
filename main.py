from utils import send_alert, get_location

def main():
    print("Intelligent Personal Safety Agent Running...")
    
    location = get_location()
    print(f"Current location: {location}")
    
    emergency_detected = True
    if emergency_detected:
        send_alert(location)
        print("Emergency alert process completed!")

if __name__ == "__main__":
    main()
