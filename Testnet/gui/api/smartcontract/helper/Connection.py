import tkinter as tk
from tkinter import messagebox
import socket
from web3 import Web3

infura_api_key = "64030d0ca36640db87457233878813eb"
ethereum_sepolia_rpc_url = "https://sepolia.infura.io/v3/"
# Connect to an Ethereum Sepolia Testnet node
w3 = Web3(Web3.HTTPProvider(ethereum_sepolia_rpc_url + infura_api_key))

def is_internet_available():
    try:
        socket.create_connection(("www.google.com", 80))
        messagebox.showinfo("Internet Connection", "Internet Connection Available!!")
        return True
    except OSError:
        messagebox.showinfo("Internet Connection", "No Internet Connection!! Please enable internet on your device")
        return False

def is_testnet_connected():
    if is_internet_available():
        try:
            if w3.is_connected():
                messagebox.showinfo("Testnet Connection", "Successfully connected to testnet")
                return True
            else:
                messagebox.showinfo("Testnet Connection", "Connection Failed! Try Again")
                return False
        except Exception as e:
            messagebox.showinfo("Testnet Connection", f"Connection Failed! Error: {e}")
            return False
    else:
        messagebox.showinfo("Internet Connection", "No Internet Connection!! Please enable internet on your device")
        return False

