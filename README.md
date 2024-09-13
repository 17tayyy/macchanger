
## Requirements

- Python 3.x
- `termcolor` package (for colored output)

You can install the required package with:
```bash
pip install termcolor
````

## Usage

The script requires administrator privileges since it interacts with the system's network configuration. Make sure to run it as root or use `sudo`.

### Running the Script

To change the MAC address of a network interface, use the following options:

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
```

- `-i` or `--interface`: Specifies the name of the network interface (e.g., `eth0`, `ens33`, etc.).
- `-m` or `--mac`: Specifies the new MAC address in the standard format (e.g., `00:11:22:33:44:55`).

### Example

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```
