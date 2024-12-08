import requests
import argparse
import os

SERVER_URL = "http://127.0.0.1:5000"

def add_files(files):
    files_to_send = {os.path.basename(file): open(file, 'rb') for file in files}
    response = requests.post(f"{SERVER_URL}/add", files=files_to_send)
    print(response.json())

def list_files():
    response = requests.get(f"{SERVER_URL}/ls")
    print(response.json())

def remove_file(filename):
    response = requests.delete(f"{SERVER_URL}/rm", params={"filename": filename})
    print(response.json())

def update_file(files):
    files_to_send = {os.path.basename(file): open(file, 'rb') for file in files}
    response = requests.post(f"{SERVER_URL}/update", files=files_to_send)
    print(response.json())

def word_count():
    response = requests.get(f"{SERVER_URL}/wc")
    print(response.json())

def freq_words(limit, order):
    response = requests.get(f"{SERVER_URL}/freq-words", params={"limit": limit, "order": order})
    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Store Client")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("files", nargs="+", help="Files to add")

    ls_parser = subparsers.add_parser("ls")

    rm_parser = subparsers.add_parser("rm")
    rm_parser.add_argument("filename", help="File to remove")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("files", nargs="+", help="Files to update")

    wc_parser = subparsers.add_parser("wc")

    freq_parser = subparsers.add_parser("freq-words")
    freq_parser.add_argument("--limit", "-n", type=int, default=10, help="Limit the number of words")
    freq_parser.add_argument("--order", choices=["asc", "dsc"], default="dsc", help="Order of frequency")

    args = parser.parse_args()

    if args.command == "add":
        add_files(args.files)
    elif args.command == "ls":
        list_files()
    elif args.command == "rm":
        remove_file(args.filename)
    elif args.command == "update":
        update_file(args.files)
    elif args.command == "wc":
        word_count()
    elif args.command == "freq-words":
        freq_words(args.limit, args.order)
