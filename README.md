# ATM‑bash_scripting

A set of Bash shell scripts that simulate an Automated Teller Machine (ATM) interface,
allowing users to perform banking operations such as viewing balance, withdrawing money,
making deposits, and more — entirely via shell scripting on Unix/Linux.

## Features
- Simulate ATM interactions in the terminal (menu, input handling)  
- Basic banking operations: check balance, withdraw, deposit  
- User account / PIN verification mechanism  
- Easy to extend with transfer, logs, persistent file‑based database  

## Requirements
- A Unix‑compatible system (Linux, macOS, WSL)  
- Bash shell (`/bin/bash`)  
- Standard Unix command‑line tools (`sed`, `awk`, `grep`, `coreutils`)  
- (Optional) File permissions: ensure scripts are executable (`chmod +x script.sh`)

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/mrbadbug/ATM‑bash_scripting.git
   cd ATM‑bash_scripting
2. Link the project with database and pin_hashing
   ```bash   
   bash atm_db.sh   
   sqlite3 atm.db
   python3 Scripts/hash_pin.py "$pin"
   hashed_pin=$(python3 "$HASH_PYTHON_SCRIPT" "$pin")
3.Read/Update balance, Verify pin
   ```bash
   balance=$(sqlite3 "$DB_NAME" "SELECT balance FROM users WHERE account_number='$account_number';")
   sqlite3 "$DB_NAME" "UPDATE users SET balance = balance + $amount WHERE account_number='$account_number';"
   sqlite3 "$DB_NAME" "INSERT INTO transactions (account_number, type, amount) VALUES ('$account_number', '$transaction_type', $amount);"
   stored_hash=$(sqlite3 "$DB_NAME" "SELECT pin FROM users WHERE account_number='$account_number';")
   [[ "$hashed_pin" == "$stored_hash" ]]



   

   
