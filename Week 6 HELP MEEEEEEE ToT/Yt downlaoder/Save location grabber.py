def get_download_path():
    #Select download location
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    while True:
        save_path = input("Enter download location (Press Enter For Current Dir): ").strip()
        if not save_path:
            save_path = default_path
            print(f"Using default location {save_path}")
            break
        else:
            save_path = os.path.expanduser(save_path) # Handle ~ if user types it

            #check if path exists
            if os.path.exists(save_path):
                if os.path.isdir(save_path):
                    print(f"Valid directory: {save_path}")
                    break
                else:
                    print("Error: That path exists but is not a directory. Please enter a valid directory!")

            else:
                #Ask if the user wants to create it
                create = input(f"Directory '{save_path}' does not exist. Create it? (y/n): ").strip().lower()
                if create in ['y', 'yes']:
                    try:
                        os.makedirs(save_path, exist_ok=True)
                        print(f"Created directory: {save_path}")
                        break
                    except Exception as e:
                        print(f"Error creating directory: {e}")
                        print("Please try a different path.")
                else:
                    print("Please enter a different path.")