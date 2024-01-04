from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange

state_choices = [['AD', 'Andhra Pradesh'], ['AR', 'Arunachal Pradesh'], ['AS', 'Assam'], ['BR', 'Bihar'], ['CG', 'Chattisgarh'], ['DL', 'Delhi'], ['GA', 'Goa'], ['GJ', 'Gujarat'], ['HR', 'Haryana'], ['HP', 'Himachal Pradesh'], ['JK', 'Jammu and Kashmir'], ['JH', 'Jharkhand'], ['KA', 'Karnataka'], ['KL', 'Kerala'], ['LD', 'Lakshadweep Islands'], ['MP', 'Madhya Pradesh'], ['MH', 'Maharashtra'], ['MN', 'Manipur'], ['ML', 'Meghalaya'], ['MZ', 'Mizoram'], ['NL', 'Nagaland'], ['OD', 'Odisha'], ['PY', 'Pondicherry'], ['PB', 'Punjab'], ['RJ', 'Rajasthan'], ['SK', 'Sikkim'], ['TN', 'Tamil Nadu'], ['TS', 'Telangana'], ['TR', 'Tripura'], ['UP', 'Uttar Pradesh'], ['UK', 'Uttarakhand'], ['WB', 'West Bengal']]
list = [[0, 'Rice'],
        [1, 'Wheat'],
        [2 ,'Maize'],
        [3 ,'Cotton'],
        [4 ,'Sugarcane'],
        [5 ,'Barley'],
        [6 ,'Pulses (Various)'],
        [7 ,'Oilseeds (Various)'],
        [8 ,'Groundnut (Peanut)'],
        [9 ,'Soybean'],
        [10 ,'Bajra (Pearl Millet)'],
        [11,'Jowar (Sorghum)'],
        [12 ,'Paddy (Paddy)'],
        [13 ,'Turmeric'],
        [14,'Ginger'],
        [15,'Onion'],
        [16,'Potato'],
        [17,'Tomato'],
        [18,'Cauliflower'],
        [19,'Carrot'],
        [20,'Lentils (Masoor)'],
        [21,'Chickpea (Chana)'],
        [22,'Mustard'],
        [23,'Sunflower'],]

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10), Regexp(regex='^[0-9]+$')])
    pincode = StringField('Pincode', validators=[DataRequired(), Length(min=6, max=6), Regexp(regex='^[0-9]+$')])
    state = SelectField(u'State', choices=state_choices)     
    submit = SubmitField('Submit')       

class LoginForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10), Regexp(regex='^[0-9]+$')]) 
    submit = SubmitField('Submit')

class PriceForm(FlaskForm):
    state = SelectField(u'State', choices=state_choices) 
    submit = SubmitField('Submit')     

class MarketplaceForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    cost = IntegerField('Cost', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')  

class GovForm(FlaskForm):
    sector = SelectField(u'Sector', choices=[['Agriculture', 'Agriculture'], ['Finance', 'Finance'], ['Health', 'Health'], ['Education', 'Education']])
    submit = SubmitField('Submit')

class InventoryCategoryForm(FlaskForm):
    category = SelectField(u'Category', choices=[['Harvest', 'Harvest'], ['Livestock', 'Livestock']])
    submit = SubmitField('Submit')

class InventoryCreateForm(FlaskForm):
    name =  StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')

class CropCalendarForm(FlaskForm):
    crop = SelectField('Crop Name', choices=list )
    submit = SubmitField('Submit')

    