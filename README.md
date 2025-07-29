# Bluetooth BLE Device Scanner

This Python project scans for nearby Bluetooth Low Energy (BLE) devices and displays detailed information about each device, including address, name, RSSI, TX power, manufacturer data, service data, and service UUIDs.

## Features

- Scans for BLE devices using the [bleak](https://github.com/hbldh/bleak) library
- Displays device details in a readable format
- Supports manufacturer and service data parsing

## Requirements

Install dependencies using pip:

```sh
pip install -r requirements.txt
```

## Usage

Run the scanner:

```sh
python main.py
```

The output will list all discovered BLE devices and their details.

## Files

- [`main.py`](main.py): Main script for scanning and displaying BLE devices.
- [`requirements.txt`](requirements.txt): Python dependencies.
- [`output.txt`](output.txt): Example output from a scan.
- [`.gitignore`](.gitignore): Git ignore rules.

## License