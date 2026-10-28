#!/usr/bin/env python3
"""
Nmap Scan Parser Tool
Author: Victor Murithi (VmurithiSeCops)
Description: Parses standard Nmap text output files to extract open ports and services.
"""

import sys
import re

def parse_nmap_file(filepath):
    print(f"\n[*] Analyzing scan file: {filepath}\n" + "="*50)
    
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            
        # Extract IP address from Nmap report header
        ip_match = re.search(r'Nmap scan report for (?:[^\s]+\s+)?\(?([0-9\.]+)\)?', content)
        target_ip = ip_match.group(1) if ip_match else "Unknown Target"
        print(f"[+] Target IP: {target_ip}")
        print("-" * 50)
        print(f"{'PORT':<12} {'STATE':<10} {'SERVICE':<15}")
        print("-" * 50)
        
        # Regex to find open ports e.g., "80/tcp open http"
        port_pattern = re.compile(r'^(\d+/(?:tcp|udp))\s+(\w+)\s+([^\n]+)', re.MULTILINE)
        matches = port_pattern.findall(content)
        
        if matches:
            for port, state, service in matches:
                print(f"{port:<12} {state:<10} {service:<15}")
        else:
            print("[-] No open ports found or unrecognized format.")
            
        print("="*50 + "\n[*] Parsing complete.\n")
        
    except FileNotFoundError:
        print(f"[!] Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <path_to_nmap_scan.txt>")
        sys.exit(1)
        
    scan_file = sys.argv[1]
    parse_nmap_file(scan_file)
