<h1 align="center">Creating a Local Blockchain using PyChain Ledger</h1>
<h2 align="center"> A Blockchain-Based Ledger Project with a User-Friendly Interface</h2>
<h4 align="center"> Created by <em>Cam Gould</em> for the <em>University of Toronto Fintech BootCamp</em> </h4>

<p align="center">
  <img
    src="https://raw.githubusercontent.com/CamGould/Local_Blockchain_with_PyChain/main/Supplemental/ezgif.com-gif-maker-3.gif"
  >
</p>

### Background Information
For this project I will be a hypothetical fintech engineer who’s working at one of the five largest banks in the world. I've been recently promoted to act as the lead developer on their decentralized finance team. My task is to build a ***blockchain-based ledger system***, complete with a ***user-friendly web interface***. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.
<br>
<br>
In this assignment, I will use the *PyChain Legder* to build a blockchain that runs locally and can be interacted with and verified using a user-friendly *Streamlit* interface.
<br>
### Project Files
Use the following link to jump right into the Python Code:
<br>
<br>
This notebook contains the [Python Code of the Streamlit App](https://github.com/CamGould/Local_Blockchain_with_PyChain/blob/main/Python%20Code/pychain.py)

### Project Outline and Instructions
To create the *PyChain Ledger* and *Streamlit App* I will complete the following steps:
<br>
1. I will create a new *dataclass* called **Record**.
    1. This class will serve as the blueprint for the financial transaction records that the blocks of the ledger will store.
2. Create and modify the existing **Block** data class to store *Record data*.
3. Add **Relevant User Inputs** to the *Streamlit interface*.
    1. These user input interfaces will allow the user to transact, interact, & verify aspects of the PyChain.
4. I will preform transactions on the local blockchain to showcase how its usage.

### Streamlit Theme Settings Used in the Demonstration 
If you like the visual apperance of my application you can replecate the theme in your own using the following [custom streamlit theme](https://blog.streamlit.io/introducing-theming/):
<br>
```
[theme]

# Primary accent for interactive elements
primaryColor = '#30C731'

# Background color for the main content area
backgroundColor = '#F7F7F7'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#DADAD8'

# Color used for almost all text
textColor = '#01011E'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "serif"
```
