# 📚 State Library Web Application  

**State Library Web Application** is a project that scrapes public library data by state using Selenium and displays it in an interactive web interface using Streamlit.

---

## 📌 **Project Overview**  

### **🔹 Components:**  
1. **Web Scraper (Selenium):**  
   - Uses `Selenium` to scrape public library data from [PublicLibraries.com](https://publiclibraries.com).  
   - Extracts details like **state, city, library name, address, zip code, and phone number**.  
   - Stores data in an **SQLite database** for further use.  

2. **Streamlit UI:**  
   - Provides an interactive interface for users to **search and filter library data**.  
   - Displays libraries by **state and city** in a structured table.  
   - Allows text-based searching for quick data lookup.  

---

## 🚀 **Features**  
👉 **Automated Web Scraping** using Selenium.  
👉 **Stores Data in SQLite** for easy access.  
👉 **Search & Filter Functionality** for quick lookup.  
👉 **Minimalistic & User-Friendly UI** built with Streamlit.  
👉 **Easy to Deploy** on local or cloud platforms.  

---

## 💂️ **Project Structure**  
```
state-library-webapp/
│── scraper/
│   │── library_scraper.py     # Selenium web scraper
│── streamlit_app/
│   │── app.py                 # Streamlit UI
│── database/
│   │── libraries.db           # SQLite database (generated after running scraper)
│── README.md                  # Project documentation
```

---

## 🛠 **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/State-Library-Web-Application.git
cd State-Library-Web-Application
```

---

## 🔄 **Running the Web Scraper**  
To scrape data and save it to an SQLite database:  
```bash
cd Library Scraper
python Library.py
```

---

## 🌍 **Running the Streamlit App**  
To launch the Streamlit web interface:  
```bash
cd streamlit_app
Streamlit run app.py
```
This will open the application in your web browser.

---

## 🛠 **Technologies Used**  
- **Python** (for backend processing)  
- **Selenium** (for web scraping)  
- **SQLite** (for storing scraped data)  
- **Streamlit** (for the interactive web UI)  
- **Pandas** (for handling data in the UI)  

---

## 🎉 **Contributions & Issues**  
- Contributions are welcome! Feel free to fork and submit a pull request.  
- If you find any issues, please create a GitHub issue.  

---

## 💎 **Contact**  
- **GitHub:** https://github.com/SidduKumar-1292 
- **Email:** siddukumar1292@gmail.com  

🚀 **Explore public libraries easily!** 📚





