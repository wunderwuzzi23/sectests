import tailer
import sys
import urllib.parse
import time

def monitor_file(file_path):
    for line in tailer.follow(open(file_path)):
        if "ci=" in line:
            encoded_str = line.split('=')[1]
            encoded_str = encoded_str.split(' ')[0]
            decoded_str = urllib.parse.unquote(encoded_str)
            decoded_str = urllib.parse.unquote(decoded_str)
            print(">> " + decoded_str+"\n")

        if "ci%3D" in line:
            encoded_str = line.split('ci%3D')[1]
            encoded_str = encoded_str.split(' ')[0]
            decoded_str = urllib.parse.unquote(encoded_str)
            decoded_str = urllib.parse.unquote(decoded_str)
            print(">> "+decoded_str+"\n")
        time.sleep(1)

if __name__ == "__main__":
    file_path = "/var/log/nginx/access.log"
    if len(sys.argv) == 2:
        file_path = sys.argv[1]

    print(f"Monitoring {file_path} for ChatGPT messages:")
    print()
    monitor_file(file_path)
