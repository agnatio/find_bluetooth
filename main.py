import asyncio
from bleak import BleakScanner


def format_hex_dict(d):
    return {hex(k) if isinstance(k, int) else k: v.hex() for k, v in d.items()}


async def scan_ble():
    print("🔍 Scanning for BLE devices...\n")

    devices = await BleakScanner.discover(return_adv=True)

    print(f"\n📡 Found {len(devices)} BLE device(s):\n")

    for i, (address, value) in enumerate(devices.items()):
        print(f"🟢 Device {i + 1}")
        print(f"  Address       : {address}")

        if isinstance(value, tuple) and len(value) == 2:
            device, adv = value

            name = device.name or adv.local_name or "Unknown"
            print(f"  Name          : {name}")
            print(f"  RSSI          : {adv.rssi} dBm")
            print(f"  TX Power      : {adv.tx_power or 'N/A'}")

            # Manufacturer data
            mfg = format_hex_dict(adv.manufacturer_data)
            if mfg:
                print(f"  Manufacturer  : {mfg}")
            else:
                print(f"  Manufacturer  : None")

            # Service data
            if adv.service_data:
                print(f"  Service Data  :")
                for uuid, data in adv.service_data.items():
                    print(f"    {uuid}: {data.hex()}")
            else:
                print(f"  Service Data  : None")

            # UUIDs
            if adv.service_uuids:
                print(f"  Service UUIDs : {', '.join(adv.service_uuids)}")
            else:
                print(f"  Service UUIDs : None")

        else:
            print(f"  ⚠️ Unexpected format: {value}")

        print("-" * 60)


if __name__ == "__main__":
    asyncio.run(scan_ble())
