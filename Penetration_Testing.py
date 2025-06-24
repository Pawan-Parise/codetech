import socket
import itertools

# --- Port Scanner ---
def port_scanner(target, ports=[21, 22, 80, 443]):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is open")
            sock.close()
        except:
            pass

# --- Brute Force (sample dictionary attack) ---
def brute_force(username, password_list, correct_password):
    for password in password_list:
        print(f"Trying: {password}")
        if password == correct_password:
            print(f"✅ Password found: {password}")
            break

# Run toolkit
target_ip = input("Enter target IP: ")
port_scanner(target_ip)

print("\nStarting Brute Force...")
brute_force("admin", ["123", "admin", "pass", "root"], "admin")
