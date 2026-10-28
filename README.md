# Nmap Scan Parser 🛡️🐍

A lightweight Python utility designed to parse Nmap scan text outputs, extract open ports, IP addresses, and running services, and present them in a clean, structured format. Built as part of a cybersecurity portfolio to automate reconnaissance data handling.

## Features
- Parses standard Nmap scan text files.
- Extracts target IP addresses, open ports, protocols, and service names.
- Outputs a clean, organized summary of discovered attack surfaces.

## Usage
1. Export your Nmap scan results to a text file (e.g., `scan_results.txt`).
2. Run the parser script:
   ```bash
   python parser.py scan_results.txt
