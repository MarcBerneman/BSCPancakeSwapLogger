from bscscan import BscScan
from Crypto.Hash import keccak
import csv
import time
import os.path

class KeccakHasher:
    def __init__(self):
        self.str2hash= {}

    def getHash(self, chars):
        if chars not in self.str2hash:
            k = keccak.new(digest_bits=256)
            k.update(chars)
            data =  '0x' + k.hexdigest()[0:8]
            self.str2hash[chars] = data
        return self.str2hash[chars]

keccakHasher = KeccakHasher()
with open("BSCScan_API.txt") as f:
    API_key = f.readline()
bsc = BscScan(API_key) # key in quotation marks

def getContractInt(chars):
        data = keccakHasher.getHash(chars)
        val = bsc.get_proxy_call(contract, data=data)
        val = int(val,0)
        return val

def getContractReserves():
    data = keccakHasher.getHash(b'getReserves()')
    val = bsc.get_proxy_call(contract, data=data)
    reserve1 = int(val[2:66],16)
    reserve2 = int(val[66:130],16)
    return reserve1, reserve2

def main(contract):
    kLast = getContractInt(b'kLast()')
    reserve1, reserve2 = getContractReserves()
    LP = getContractInt(b'totalSupply()')
    print("sum(reserves)/LP: ", (reserve1+reserve2)/LP)

    fname = "logged_data/" + contract + ".csv"
    new_file = not os.path.isfile(fname) 
    with open(fname, "a" , newline='') as f:
        writer = csv.writer(f, delimiter=';')
        if new_file:
            writer.writerow(("Time","Reserve 1","Reserve 2", "LP", "kLast", "Sum reserves/LP"))
        writer.writerow((time.time(), reserve1, reserve2, LP, kLast, (reserve1+reserve2)/LP))

if __name__ == "__main__":
    contract = "0x05faf555522Fa3F93959F86B41A3808666093210" #UST-BUSD
    main(contract)
    contract = "0x7EFaEf62fDdCCa950418312c6C91Aef321375A00" #USDT-BUSD
    main(contract)
    contract = "0x58F876857a02D6762E0101bb5C46A8c1ED44Dc16" #BUSD-BNB
    main(contract)
    contract = "0xF45cd219aEF8618A92BAa7aD848364a158a24F33" #BTCB-BUSD
    main(contract)
    contract = "0x0eD7e52944161450477ee417DE9Cd3a859b14fD0" #CAKE-BNB
    main(contract)
    contract = "0x61EB789d75A95CAa3fF50ed7E47b96c132fEc082" #BTCB-BNB
    main(contract)
    contract = "0x62c1dEC1fF328DCdC157Ae0068Bb21aF3967aCd9" #USDT-BUSD (MDEX)
    main(contract)
    contract = "0xC05654C66756eBB82c518598c5f1ea1a0199a563" #MAMZN-UST
    main(contract)
    contract = "0xA3BfBbAd526C6B856B1Fdf73F99BCD894761fbf3" #MGOOGL-UST
    main(contract)
    contract = "0x91417426C3FEaA3Ca795921eB9FdD9715ad92537" #MNFLX-UST
    main(contract)
    contract = "0xEc6b56a736859AE8ea4bEdA16279Ecd8c60dA7EA" #MTSLA-UST
    main(contract)
    contract = "0xBCf01a42f6BC42F3Cfe81B05519565044d65D22a" #MCOIN-UST
    main(contract)