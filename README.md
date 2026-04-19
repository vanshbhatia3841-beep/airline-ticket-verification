# ✈️ Airline Ticket Verification

A Python-based command-line tool that allows airline staff to look up and verify passenger tickets from a MySQL database using passenger name, phone number, or booking ID.

---

## 📋 Features

- Search tickets by **First & Last Name**, **Phone Number**, or **Booking ID**
- Displays a clean, formatted table of matching ticket records
- Handles multiple matching records — prompts staff to select the correct one
- Allows staff to mark a ticket as **VERIFIED** directly from the terminal
- Connects securely to a MySQL database using `mysql-connector-python`

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Database:** MySQL
- **Library:** `mysql-connector-python`

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/airline-ticket-verification.git
cd airline-ticket-verification
```

### 2. Install dependencies

```bash
pip install mysql-connector-python
```

### 3. Configure the database connection

Open `airline_verify.py` and update the connection details:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_password",
    database="airline",
    auth_plugin='mysql_native_password'
)
```

### 4. Set up the MySQL database

Make sure your MySQL database has a table named `ticket` with the following columns:

| Column | Type |
|---|---|
| ID | INT AUTO_INCREMENT (Primary Key) |
| Airline | VARCHAR |
| BOOKINGID | VARCHAR |
| First Name | VARCHAR |
| Last Name | VARCHAR |
| Phone No | VARCHAR |
| Age | INT |
| From | VARCHAR |
| To | VARCHAR |
| Date | DATE |
| Time | TIME |
| Verification | VARCHAR DEFAULT 'PENDING'|

---

## 🚀 Usage

Run the script from your terminal:

```bash
python airline_verify.py
```

You will be prompted to choose a lookup method:

```
Enter the type of detail you can provide to get the ticket (Name/Phone/ID):
```

- **Name** → Enter first and last name
- **Phone** → Enter the passenger's phone number
- **ID** → Enter the Booking ID

After results are displayed, you can confirm whether the ticket should be marked as `VERIFIED`.

---

## 📸 Sample Output

```
ID        Airline        Booking ID     First Name     Last Name      Phone          Age     From      To        Date          Time      Verification
------------------------------------------------------------------------------------------------------
1         IndiGo         BK10293        John           Doe            9876543210     28      DEL       BOM       2024-05-10    10:30     PENDING

Is the ticket Verified or not? (Yes/No): Yes
Ticket 1 has been updated to VERIFIED.
```

---

## ⚠️ Security Note

> **Do not commit your database credentials to GitHub.**  
> Consider using a `.env` file with the [`python-dotenv`](https://pypi.org/project/python-dotenv/) library to manage sensitive credentials safely.

Add a `.env` file:
```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=airline
```

And add `.env` to your `.gitignore`:
```
.env
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Vansh** — [GitHub Profile](https://github.com/your-username)
