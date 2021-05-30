from bscscan import BscScan
from Crypto.Hash import keccak
import csv
import time
import os.path

with open("BSCScan_API.txt") as f:
    API_key = f.readline()
bsc = BscScan(API_key) # key in quotation marks


def main(wallet_address):
    BNB = int(bsc.get_bnb_balance(wallet_address))/1e18
    print(f"{BNB} BNB")

    DOT_address = "0x7083609fce4d1d8dc0c979aab8c869ea2c873402"
    DOT = int(bsc.get_acc_balance_by_token_contract_address(DOT_address,wallet_address))/1e18
    print(f"{DOT} DOT")

if __name__ == "__main__":
    wallet_address = "0xb218C5D6aF1F979aC42BC68d98A5A0D796C6aB01"
    main(wallet_address)
