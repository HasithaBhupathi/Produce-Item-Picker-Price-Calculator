from perant import Item
from work_space import user

import streamlit as st
import pandas as pd

### make the title
st.title("Produce Item Picker & Price Calculator")

### Add the Item informations
fruit_names = pd.read_csv("Fruit Prices 2022.csv")
vegetable_names = pd.read_csv("Vegetable_Prices_2022.csv")



### Make user selected dataframe

### Streamlit provides st.session_state to remember variables between interactions (like button clicks).
### Since streamlit app wrok from top to bottom if we didn't use st.session_state the dataframe make again and again

if "user_selected_items" not in st.session_state:
    st.session_state.user_selected_items = pd.DataFrame({
        "Cetagory": pd.Series(dtype='str'),
        "Name": pd.Series(dtype='str'), 
        "Quantity": pd.Series(dtype='int'),
        "Discount": pd.Series(dtype='float')
        
        })
     
    
#### Make the add item field
with st.container():
    
    st.subheader("Add Items")
    cetagory, name = st.columns(2)
    
    with cetagory:
        item_cetagory = st.selectbox("Item cetagory", ["fruit","vegetable"])
    
    with name:
        
        if item_cetagory == "fruit":
            item_name = st.selectbox("Fruit name", fruit_names["name"])
         
        else:
            item_name = st.selectbox("Vegetable name", vegetable_names["name"])    

with st.container():
    
    quantity,discount = st.columns(2)
    
    with quantity:
        item_quantity = int(st.number_input("Quantity in grams", min_value= 0,max_value=10000))
        ### If we use both min_value,max_value, and value are float then number_input will be float scale.
        ### if we use both min_value, max_value, and value are int then number_input weil be integer scale.
    
    if item_cetagory == "fruit":
        with discount:
            item_discount = float(st.number_input("Discount",min_value=0.0,max_value=1.0,value=0.2))    
    
    else:
        with discount:
            item_discount = float(st.number_input("Discount", min_value= 0.0,max_value=1.0,value=0.1))

            
item_add = st.button("Add")
    
### add new item to the user selected items
if item_add:
    
    new_data = pd.DataFrame({
        "Cetagory": [item_cetagory],
        "Name": [item_name], 
        "Quantity": [item_quantity],
        "Discount": [item_discount]
        })
    
    st.session_state.user_selected_items = pd.concat([st.session_state.user_selected_items, new_data], ignore_index=True)
    
    
    #### The ignore_index = True in pd.concat() means, when combining data, reset the row index to be a clean, continuous 
    #### range (0, 1, 2, …), and don’t keep the original index values from the individual DataFrames.
    
    #### Moreover when we add a new raw into a empty dataframe then empty dataframe columns must be defined by their
    #### data types. If not it confeuse to use concatanate.  


### remove a selected item
with st.container():
    
    st.subheader("Remove Items")
    remove_intex = int(st.number_input("Item index", min_value=0))
    
    item_remove_, remove_all_= st.columns(2)
    
    with item_remove_:
        item_remove = st.button("Remove")
        
        if item_remove:
            if remove_intex in st.session_state.user_selected_items.index:
                st.session_state.user_selected_items.drop(index = [remove_intex], inplace = True)
                # When we use inplace= True, it directly modyfied the dataframe in memory, we noneed to assighe to
                # st.session_state.user_selected_items. 
                
                #st.session_state.user_selected_items = st.session_state.user_selected_items.drop(index = [remove_intex])      
                # If we ddon't use inplace = True the we need to assign into st.session_satate.user_selected_items
                # if not changes will not set under name "user_selected_items".
                
                
            else:
                raise IndexError(f"Index {item_remove} is not valid")
        
        
    with remove_all_:
        remove_all = st.button("Remove All")
      
        if remove_all:
            st.session_state.user_selected_items = pd.DataFrame({"Cetagory": pd.Series(dtype='str'),
                                                                "Name": pd.Series(dtype='str'), 
                                                                "Quantity": pd.Series(dtype='int'),
                                                                "Discount": pd.Series(dtype='float')
                                                                }) 
    
            ### When we delete all again we need to create and assign column data type, if we didn't assign columns data
            ### type when we add new item from .concat() it will be confuise

### show the updated selecte items    
st.table(st.session_state.user_selected_items)


### Calculations total price
with st.container():
    
    st.subheader("Calculations")
    total_price_button, total_price_lebal = st.columns(2)
    
    with total_price_button:
        total_price = st.button("Total Price")
    
        if total_price:
            for i in st.session_state.user_selected_items.index:
                user(st.session_state.user_selected_items["Cetagory"][i],st.session_state.user_selected_items["Name"][i],st.session_state.user_selected_items["Quantity"][i],st.session_state.user_selected_items["Discount"][i])
            
            with total_price_lebal:
                st.write(f"Total price is : ${round(Item.total_price(),4)}")
            
        else:       
            with total_price_lebal:
                st.write("------------------")              
        

### calculate the total discount
with st.container():
    
    total_discount_button,total_discount_lebal = st.columns(2)
    
    with total_discount_button:
        total_discount = st.button("Total Discount")
        
        if total_discount:
            for i in st.session_state.user_selected_items.index:
                user(st.session_state.user_selected_items["Cetagory"][i],st.session_state.user_selected_items["Name"][i],st.session_state.user_selected_items["Quantity"][i],st.session_state.user_selected_items["Discount"][i])
        
            with total_discount_lebal:
                st.write(f"Total discount is : ${round(Item.total_discount(),4)}")
            
        else:
            with total_discount_lebal:
                st.write(f"-----------------")            



### Calculate the final price
with st.container():
    
    final_price_button, final_price_lebal = st.columns(2)
    
    with final_price_button:
        final_price = st.button("Final Price")
        
        if final_price:
            for i in st.session_state.user_selected_items.index:
                user(st.session_state.user_selected_items["Cetagory"][i],st.session_state.user_selected_items["Name"][i],st.session_state.user_selected_items["Quantity"][i],st.session_state.user_selected_items["Discount"][i])
        
            with final_price_lebal:
                st.write(f"Final price is : ${round(Item.final_price(),4)}")
            
    
        else:
            with final_price_lebal:
                st.write(f"-----------------")           
    

# We need to make sure below class attributes are empty, if not when we click Total Price, Total Discount, and Final Price
# then same user selected items add into below attributes again and again. 
Item.all_fruits = []
Item.all_vegetables = []


#### Add sidebar
st.sidebar.title("About this")
st.sidebar.write("""This app lets users create a custom shopping list of fruits and vegetables by selecting items, 
                quantities, and discounts. It calculates the total price, total discount, and final price. You can also
                add or remove items, and submit feedback, which is saved for future review.""")


"""
#### take user feedback and save these feedbacks in csv file.
st.write("-----------------------------------------------------------------")
feedback = str(st.text_area("Put your feedback here"))
send_button = st.button("Send")

exesting_feedback_dataframe = pd.read_csv("feedback.csv")

if send_button:
    new_feedback = pd.DataFrame({
        "feedback": [feedback]
    })
    
    updated_feedback_dataframe = pd.concat([exesting_feedback_dataframe, new_feedback], ignore_index=True)   
    updated_feedback_dataframe.to_csv("feedback.csv",index = False)    
    
    #### index = Fase in .to_csv() means don't write the dataframe index in .csv file then our csv file is below as:
    #### item,price
    #### Apple,100
    #### Carrot,50
    
    #### if index = True then below as:
    #### ,index,item,price
    ####  0,Apple,100
    ####  1,Carrot,50
"""
    
    

    
