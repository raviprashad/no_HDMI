# 📡 Wireless Screen Casting (no_HDMI Required)

## 📌 Problem Statement
In many classrooms, teachers face a common issue: missing HDMI cables, which prevents them from connecting their laptops to digital boards or projectors.

## 💡 Solution
This project provides a wireless screen casting solution that allows you to cast your screen **without using an HDMI cable**, as long as both devices are connected to the same network.

The project is open-source and supports **Windows and Linux**.

---

## 🚀 Features
- No HDMI cable required  
- Wireless screen casting  
- Works on the same network  
- Cross-platform support (Windows & Linux)  
- Simple and easy to use  
- **Students can also view the live screen on their own devices using a browser**

---

## 🖥️ Supported Platforms
- Windows  
- Linux  

> Separate releases are available for each operating system.

---

## 📥 Installation

1. Go to the **Releases** section of this repository  
2. Download the appropriate file:
   - **Windows Release** for Windows  
   - **Linux Release** for Linux  

---

## 🔐 Administrative Permission Required
⚠️ Important:  
The script must be run with **administrative (root) privileges**.

- **Windows:**  
  Right-click the file and select **Run as Administrator**

- **Linux:**  
  Run the script using `sudo`

---

## 🌐 Network Requirements
- All devices must be connected to the **same network**  
- Teacher’s laptop, digital board, and students’ devices should be on the same Wi-Fi  
- Firewall should allow local network connections  

---

## ▶️ How to Use

1. Run the script on the **casting device** (teacher’s laptop)
2. Keep the script running
3. On any **display or student device**:
   - Open any web browser
   - Enter the IP address of the casting device followed by port **5000**

http://casting-device-ip:5000

Example:
http://192.168.1.10:5000


4. Press **Enter** to view the live screen

---

## 🏫 Use Cases
- Classroom teaching  
- Students viewing the lecture live on their own devices  
- Presentations  
- Meetings  
- Situations where HDMI cable is unavailable  

---

## 🤝 Contributions
Contributions and suggestions are welcome.  
Feel free to fork this repository and submit a pull request.

---

## 📄 License
This project is open-source.

```mermaid
graph TD
    A[Teacher Laptop<br/>Screen Casting Server] -->|HTTP :5000| B[Same Wi-Fi Network]

    B --> C[Digital Board<br/>Web Browser]
    B --> D[Student Device 1<br/>Web Browser]
    B --> E[Student Device 2<br/>Web Browser]
    B --> F[Student Device N<br/>Web Browser]



