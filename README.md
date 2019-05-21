# Import your Liquid Token

## Scan the QR code
Read the Mini Private Key from the QR Code present on your physical token with a QR Code reader.

![scan](./screenshots/scan.jpeg?raw=true)

The QR Code contains a Mini Private Key like `S4EkYCKTuhxv6vzVbWHThW874QubqG`.

## Calculate address and private key
In order to gain control the token from your Liquid node you need to import the address, the private key and the blinding key. You can obtain all this codes using the provided script available in this repository; you can install this software using the following procedure.

Clone this repository in a directory.

```
git clone https://github.com/Blockstream/liquid-melt.git
cd liquid-melt
````

Create a Python virtual environment and install dependencies.

```
virtualenv -p python3 venv3
. venv3/bin/activate

pip install -r requirements.txt
```

Then call the import.py script passing the mini private key as the first argument.

```
python import.py S4EkYCKTuhxv6vzVbWHThW874QubqG
```

The script will print the commands you need to write in the console.

```
liquid-cli importaddress Q4B7E8S1o2mSCB3JtMud3ExqVrcsN4EKPH
liquid-cli importprivkey Ky3q5qRjLXAugu42eAtAYia5T4B1WkxMzgc8A8fHJSoqcosfJ9XJ false
liquid-cli importblindingkey VTpuyes4Qff2p7eZswtjPJbhyhSHmPARAx64gvxqDF7ByYLhYjAiQDXbUB2uhZYQgQQ3w8rgLAJ4MgXb 3d184554a50c7e72b324e95711f29181acac4ad2d855e3619f7fd8b9ec766e66
```

The first line shows you the unconfidential address derived from your Mini Private Key, the second shows the private key and the third shows the confidential address and the corresponding blinding key.

## Import the token in your wallet
Download latest release of Liquid or Liquid-qt from the [official repository](https://github.com/ElementsProject/elements/releases).

If you use liquid-cli from the command line just copy the previous lines in your shell.

If you use the liquid-qt app, navigate on the console in this way:

- click on HELP,
- click on Debug Window,
- select the Console tab.

![console](./screenshots/console.png?raw=true)
![debug window](./screenshots/debug_window.png?raw=true)

Copy the three commands removing the "liquid-cli" prefix.

Remember to move the imported token to another address on your direct control or anyone who knows the Mini Private Key might access and move the same token before you do.
