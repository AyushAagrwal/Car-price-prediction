from turtle import title
import streamlit as st
import pickle
model=pickle.load(open('Car_price_predicting_model.pkl','rb'))

def main():
    string='Car Price Prediction'
    st.set_page_config(page_title=string,page_icon='')
    st.title('Car Price Predictor')
    st.markdown('#### Are you planning to sell a car')
    st.image("1646570251679.jpeg")
    st.write('')
    st.write('')
    year=st.number_input('In which year you have purchased a Car?',1980,2022,step=1,key='year')
                                                                   #startingYear,latestYear
    #calculating                                                                
    Year_old=year-2022
    present_price=st.number_input('what is the current ex-price of the car? (In Lakhs)',0.00,100.00,step=0.25,key='present_price')
    
    drived=st.number_input('How much car has been completed?',0.00,500000.00,step=500.00,key='drived')
    
    Owner=st.radio('The number of owners the car had previously?',(0,1,2),key='Owner')

    fuel_type_petrol=st.selectbox('What is the fuel type of the car?',('petrol','diesal','CNG'),key='fuel')
    if(fuel_type_petrol=='petrol'):
        fuel_type_petrol=1
        fuel_type_Diseal=0
    elif(fuel_type_petrol=='diseal'):
        fuel_type_petrol=0
        fuel_type_Diseal=1
    else:
        fuel_type_petrol=0
        fuel_type_petrol=0

    Seller_type_Individual=st.selectbox('Are u a dealer or Individual',('Dealer','Individual'),key='deal')
    if(Seller_type_Individual=='Individual'):
        Seller_type_Individual==1
    else:
        Seller_type_Individual=0    
    
    # Transmission_Mannual=st.selectbox('What is the transmission type?',('Mannual','Automatic'),key='manual')
    # if(Transmission_Mannual=='Mannual'):
    #     Transmission_Mannual==1
    # else:
    #     Transmission_Mannual=0

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    # if st.button('Estimate Price',key='Product'):
    #     try:
    #         Model=model #get a model()
    #         prediction=Model.predict([[present_price,drived,Owner,Year_old,fuel_type_petrol,fuel_type_Diseal,Seller_type_Individual,Transmission_Mannual]])
    #         output=round(prediction[0],2)
    #         if output<0:
    #             st.warning("You will be not able to sell this car !!")
    #         else:
    #             st.success('u can sell this car in {} lakhs'.format(output))
    #     except:
    #         st.warning("OOps!! Something went to worng\n Try Again")
    
    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[present_price,drived,Owner,Year_old,fuel_type_petrol,fuel_type_Diseal,Seller_type_Individual,Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")

if __name__=='__main__':
    main() 