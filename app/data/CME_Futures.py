"""
    Define the symbols you want with the following format:
        SYMBOL: ID

    Where:

        - SYMBOL is the products symbol
            - You should already know the symbol
              of the product you want to add.

        - ID is the products id
            - ( Find on https://www.cmegroup.com )
            - Inspect element
            - Go to Network
            - Find the GET method "ContractsByNumber?..."
            - ID = productID
"""

futures_map = {
    'GE': "1",
    'ES': "133",
    'ZT': "303",
    'ZF': "329",
    'ZN': "316",
    'TN': "7978",
    'ZB': "307",
    'UB': "3141",
    'GC': "437",
    'SI': "458",
    'HG': "438",
    'CL': "425",
    'NG': "444",
    'BTC': "8478",
    '6E': "58",
    'ZQ': "305",
    'SR3': "8462",
}
