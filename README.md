# BSCPancakeSwapLogger

Logger for PancakeSwap liquidity pools

## Requirements

Make a **python 3.8.5** virtual environment and install the requirements with the following code. You might need to install *pip* and *venv*.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Scripts

- YieldFarmingLog.py: logs PancakeSwap contract data
- YieldFarmingAnalyze.py: makes plots out of the logged data
- BSCWalletReader.py: example of how wallet token can be read
