# PostgreSQL Setup and Commands Guide for macOS

## Installation and Verification

### **1. Install PostgreSQL 15**
To install PostgreSQL version 15 on macOS using Homebrew, run:
```sh
brew install postgresql@15
```

### **2. Verify Installation**
To check if PostgreSQL is installed, use:
```sh
brew list | grep postgresql
```
This command will list all installed PostgreSQL versions.

---
## Starting PostgreSQL Service

### **3. Start PostgreSQL Service**
To start PostgreSQL as a background service on macOS:
```sh
brew services start postgresql
```
If you specifically installed PostgreSQL 15, use:
```sh
brew services start postgresql@15
```
This ensures that the correct version is running.

---
## Finding PostgreSQL Binary

### **4. Locate `psql` Binary**
If you need to find where `psql` is installed on macOS, run:
```sh
find /opt/homebrew -name psql 2>/dev/null
```
This command searches the `/opt/homebrew` directory for the `psql` executable.

---
## Configuring PATH

### **5. Add PostgreSQL to System PATH**
If `psql` is not found in your terminal, add it to your system's PATH:
```sh
echo 'export PATH="/opt/homebrew/Cellar/postgresql@15/15.10/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
This ensures that `psql` can be accessed from any terminal session on macOS.

---
## Verifying PostgreSQL Setup

### **6. Check PostgreSQL Version**
Once setup is complete, verify your installation with:
```sh
psql --version
```
If PostgreSQL is installed and correctly configured, this should return the version number.

---
## Connecting to PostgreSQL

### **7. Connect to PostgreSQL**
To access the PostgreSQL command-line interface:
```sh
psql -U postgres
```
If you receive an error about the role not existing, create a default user:
```sh
createuser -s postgres
```
Then try reconnecting.

---
## Conclusion
This guide helps you install, configure, and start PostgreSQL on macOS using Homebrew. If you encounter issues, ensure PostgreSQL is running and correctly added to your PATH.

For more details, visit the [official PostgreSQL documentation](https://www.postgresql.org/docs/).

