import os
import pyttsx3


engine=pyttsx3.init()
engine.setProperty('rate', 170)     
engine.setProperty('volume', 0.9)   
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
    
base_path = r"C:\Users\kansa\OneDrive\Desktop"

def find_file_path(file_name):
    os.chdir(base_path)
    folders_to_check = [base_path]
    extensions = ['.txt', '.csv', '.mp3', '.py', '.exe', '.jpg', '.png',
                  '.jpeg', '.pdf', '.docx', '.pptx', '.xlsx', '.doc',
                  '.html', '.css', '.js','.php']

    matched_files = []

    print("🔍 Checking:")
    while folders_to_check:
        current_folder = folders_to_check.pop(0)
        os.chdir(current_folder)

        files_in_dir = os.listdir()

        for ext in extensions:
            candidate = file_name + ext
            if candidate in files_in_dir:
                full_path = os.path.join(current_folder, candidate)
                matched_files.append(full_path)  

        subfolders = [
            os.path.join(current_folder, name)
            for name in files_in_dir
            if os.path.isdir(os.path.join(current_folder, name))
        ]
        folders_to_check.extend(subfolders)

    if not matched_files:
        print(f"❌ File '{file_name}' not found with known extensions.")
        return None, None

    if len(matched_files) > 1:
        engine.say(f"Found {len(matched_files)} files for '{file_name}'. Please choose one:")
        engine.runAndWait()
        for idx, path in enumerate(matched_files, 1):
            print(f"{idx}. {path}")

        try:
            selection = int(input("Enter the index number of the file you want to select: [0-exit] "))
            if selection == 0:
                print("Exiting without selection.")
                return None, None
            selected_path = matched_files[selection - 1]
        except (ValueError, IndexError):
            print("❌ Invalid selection.")
            return None, None
    else:
        selected_path = matched_files[0]

    selected_folder, selected_name = os.path.split(selected_path)
    print(f"✅ Selected: {selected_name} in {selected_folder}")
    return selected_folder, selected_name

def find_folder(folder_name):
    os.chdir(base_path)
    folders_to_check = [base_path]
    matched_folders = []

    print("📁 Scanning folders:")
    while folders_to_check:
        current_folder = folders_to_check.pop(0)
        os.chdir(current_folder)

        items_in_dir = os.listdir()
        for item in items_in_dir:
            full_path = os.path.join(current_folder, item)
            if os.path.isdir(full_path):
                if folder_name.lower() == item.lower():
                    matched_folders.append(full_path)
                folders_to_check.append(full_path)

    if not matched_folders:
        print(f"❌ Folder '{folder_name}' not found.")
        return None

    if len(matched_folders) > 1:
        engine.say(f"Found {len(matched_folders)} folders named '{folder_name}'. Please choose one:")
        engine.runAndWait()
        for idx, path in enumerate(matched_folders, 1):
            print(f"{idx}. {path}")

        try:
            selection = int(input("Enter the index number of the folder you want to select: [0-exit] "))
            if selection == 0:
                print("Exiting without selection.")
                return None
            selected_path = matched_folders[selection - 1]
        except (ValueError, IndexError):
            print("❌ Invalid selection.")
            return None
    else:
        selected_path = matched_folders[0]

    print(f"✅ Selected folder: {selected_path}")
    return selected_path