
File Store Service
==================

This project provides a simple **File Store Service** with an HTTP server and a command-line client to manage text files. Users can store, list, delete, update files, and perform operations like word counting and frequent word analysis.

Features
--------

1. Add files to the server.
2. List all stored files.
3. Remove a specific file.
4. Update the contents of a file.
5. Count the total words in all stored files.
6. Find the most/least frequent words in stored files.

Prerequisites
-------------

1. **Python 3.8+** installed on your system.
2. **Pip** (Python's package manager) installed.
3. (Optional) **Git** for cloning the repository.

Installation and Setup
----------------------

1. **Clone the repository** or download the files:
   ```bash
   git clone https://github.com/Rutujjagtap/Backend_File_Store.git
   cd Backend_File_Store
   ```

2. **Install required Python packages**:
   ```bash
   pip install flask requests
   ```

Usage
-----

### 1. Start the Server

Run the server script to start the HTTP server.

```bash
python server.py
```

- The server will run on `http://localhost:5000`.
- Keep this terminal open while using the client.

### 2. Use the Client

The client script allows you to interact with the server.

**Basic Commands**:

- **Add files to the server**:
  ```bash
  python client.py add file1.txt file2.txt
  ```
  Adds `file1.txt` and `file2.txt` to the server.

- **List all files in the server**:
  ```bash
  python client.py ls
  ```

- **Remove a file from the server**:
  ```bash
  python client.py rm file1.txt
  ```

- **Update a file on the server**:
  ```bash
  python client.py update file1.txt
  ```

- **Count total words in stored files**:
  ```bash
  python client.py wc
  ```

- **Find the most/least frequent words**:
  ```bash
  python client.py freq-words --limit 5 --order asc
  ```

Examples
--------

### Adding Files
```bash
python client.py add file1.txt file2.txt
```

### Listing Files
```bash
python client.py ls
```
Output:
```
["file1.txt", "file2.txt"]
```

### Removing a File
```bash
python client.py rm file1.txt
```

### Word Count
```bash
python client.py wc
```
Output:
```
{"word_count": 123}
```

Notes
-----

1. All files are stored in the `filestore` folder on the server.
2. Ensure the server is running before using the client.
3. For large files, the system handles network interruptions gracefully.
