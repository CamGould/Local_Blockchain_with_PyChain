# PyChain Ledger

# Preform the initial imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################

# Step One - Define a new python data class to allocate attributes and thier values 

@dataclass
class Record:
    # Set the first two variables as strings
    sender: str
    receiver: str
    # Set the last variable as an integer
    amount: int 

################################################################################

# Step 2 - Modify the Existing Block Data Class to Store Record Data

@dataclass
class Block:
    # Set up the attribute for record 
    record: Record

    # Initiate the other attributes needed
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

################################################################################

# Step Three - Streamlit Code

# Add the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])

# Create some text that will apear in the streamlit app
st.markdown(f"<h1 style='text-align: center; color: black;'>Welcome to Your Local Blockchain</h1>", unsafe_allow_html=True) 
st.markdown(f"<h3 style='text-align: center; color: black;'>This app allows you to store trasaction records using <em>PyChain</em> </h3>", unsafe_allow_html=True) 

# Set up the PyChain
pychain = setup()

################################################################################

# Step Four - Add Relevant User Inputs to the Streamlit Interface

# Add an input area where you can get a value for `sender` from the user.
sender = st.text_input("Who is the sender?", "[e.g.] Michael Jordan")

# Add an input area where you can get a value for `receiver` from the user.
receiver = st.text_input("Who is the Receiver?", "[e.g.] Jimmy Buffett")

# Add an input area where you can get a value for `amount` from the user.
amount = st.number_input("Amount", value=10 )

# Create a button to allow the user to add a block
if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # Update the new block to contain the data from the record attribute
    new_block = Block(
        record = Record(sender, receiver, amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    # Add the new block to the PyChain
    pychain.add_block(new_block)

    import time 

    # Add some user interface for when the block is adding 
    with st.spinner('Adding your block to the blockchain...'):
        time.sleep(1.5)
    st.success(f"{sender}'s block was added successfully!")

################################################################################

# Step Five - Streamlit Code (continued)
st.markdown(f"<h4 style='text-align: center; color: black;'>Here you can view all the transactions on your blockchain</h4>", unsafe_allow_html=True) 

pychain_df = pd.DataFrame(pychain.chain).astype(str)
# st.write(pychain_df)

# Lines 157 to 175 were learned from --Sharone Li-- using their post on 'Medium'
    # Here is the link to the post - https://towardsdatascience.com/make-dataframes-interactive-in-streamlit-c3d0c4f84ccb

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

gb = GridOptionsBuilder.from_dataframe(pychain_df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection(use_checkbox=False,) #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(pychain_df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='fresh', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

difficulty = st.sidebar.slider("Block Difficulty", 1, 6, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to inspect?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################

# Streamlit colour scheme 

# PC
#30C731
# TC
#01011E
# BC
#F7F7F7
# SBC
#DADAD8

# Serif