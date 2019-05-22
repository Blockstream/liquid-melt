#!/usr/bin/env python3
import wallycore as wally
import sys

b2h = wally.hex_from_bytes

if(len(sys.argv) != 2):
    print("Use "+sys.argv[0]+" minikey")
    exit()

minikey = sys.argv[1]

PREFIX = int('80', 16)  # wif prv
VERSION = int('39', 16)  # address
CA_PREFIX = wally.WALLY_CA_PREFIX_LIQUID  # 0c, confidential address

# check minikey is valid
minikey_checksum = b2h(wally.sha256((minikey + '?').encode()))
assert minikey_checksum[:2] == '00', 'Invalid minikey, incorrect checksum: {}'.format(minikey_checksum)

# compute private key
private_key = wally.sha256(minikey.encode())

# check that private_key is valid
wally.ec_private_key_verify(private_key)

# compute private key in WIF format
private_key_wif = wally.wif_from_bytes(
    private_key, PREFIX, wally.WALLY_WIF_FLAG_COMPRESSED)

# compute blinding key
blinding_private_key = wally.sha256(private_key + b'blindingkey')

# check that blinding_private_key is valid
wally.ec_private_key_verify(blinding_private_key)

# compute public blinding key
blinding_public_key = wally.ec_public_key_from_private_key(
    blinding_private_key)

# compute unconfidential address
unconfidential_address = wally.wif_to_address(private_key_wif, PREFIX, VERSION)

# compute confidential address
confidential_address = wally.confidential_addr_from_addr(
    unconfidential_address, CA_PREFIX, blinding_public_key)

print('liquid-cli importaddress {}'.format(unconfidential_address))
print('liquid-cli importprivkey {} "" false'.format(private_key_wif))
print('liquid-cli importblindingkey {} {}'.format(confidential_address,
                                                  b2h(blinding_private_key)))
