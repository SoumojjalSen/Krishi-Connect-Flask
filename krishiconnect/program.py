
dic = {
  "crops": [
    {
      "crop_id": 0,
      "crop_name": "Rice",
      "sowing_time": "June-July",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "120-150 days"
    },
    {
      "crop_id": 1,
      "crop_name": "Wheat",
      "sowing_time": "October-November",
      "harvesting_time": "April-May",
      "crop_type": "Rabi",
      "crop_period": "150-180 days"
    },
    {
      "crop_id": 2,
      "crop_name": "Maize",
      "sowing_time": "July-August",
      "harvesting_time": "October",
      "crop_type": "Kharif",
      "crop_period": "90-120 days"
    },
    {
      "crop_id": 3,
      "crop_name": "Cotton",
      "sowing_time": "May-June",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "150-180 days"
    },
    {
      "crop_id": 4,
      "crop_name": "Sugarcane",
      "sowing_time": "September-October",
      "harvesting_time": "March-April",
      "crop_type": "Rabi",
      "crop_period": "270-330 days"
    },
    {
      "crop_id": 5,
      "crop_name": "Barley",
      "sowing_time": "November-December",
      "harvesting_time": "April-May",
      "crop_type": "Rabi",
      "crop_period": "90-120 days"
    },
    {
      "crop_id": 6,
      "crop_name": "Pulses (Various)",
      "sowing_time": "Varies by type",
      "harvesting_time": "Varies by type",
      "crop_type": "Rabi/Kharif",
      "crop_period": "Varies by type"
    },
    {
      "crop_id": 7,
      "crop_name": "Oilseeds (Various)",
      "sowing_time": "Varies by type",
      "harvesting_time": "Varies by type",
      "crop_type": "Rabi/Kharif",
      "crop_period": "Varies by type"
    },
    {
      "crop_id": 8,
      "crop_name": "Groundnut (Peanut)",
      "sowing_time": "June-July",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "100-130 days"
    },
    {
      "crop_id": 9,
      "crop_name": "Soybean",
      "sowing_time": "June-July",
      "harvesting_time": "September-October",
      "crop_type": "Kharif",
      "crop_period": "100-120 days"
    },
    {
      "crop_id": 10,
      "crop_name": "Bajra (Pearl Millet)",
      "sowing_time": "June-July",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "90-110 days"
    },
    {
      "crop_id": 11,
      "crop_name": "Jowar (Sorghum)",
      "sowing_time": "June-July",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "90-110 days"
    },
    {
      "crop_id": 12,
      "crop_name": "Paddy (Paddy)",
      "sowing_time": "June-July",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "100-120 days"
    },
    {
      "crop_id": 13,
      "crop_name": "Turmeric",
      "sowing_time": "March-April",
      "harvesting_time": "November-December",
      "crop_type": "Rabi",
      "crop_period": "240-300 days"
    },
    {
      "crop_id": 14,
      "crop_name": "Ginger",
      "sowing_time": "March-April",
      "harvesting_time": "November-December",
      "crop_type": "Rabi",
      "crop_period": "240-270 days"
    },
    {
      "crop_id": 15,
      "crop_name": "Onion",
      "sowing_time": "October-November",
      "harvesting_time": "April-May",
      "crop_type": "Rabi",
      "crop_period": "180-210 days"
    },
    {
      "crop_id": 16,
      "crop_name": "Potato",
      "sowing_time": "October-November",
      "harvesting_time": "March-April",
      "crop_type": "Rabi",
      "crop_period": "100-120 days"
    },
    {
      "crop_id": 17,
      "crop_name": "Tomato",
      "sowing_time": "August-September",
      "harvesting_time": "December-January",
      "crop_type": "Rabi",
      "crop_period": "70-90 days"
    },
    {
      "crop_id": 18,
      "crop_name": "Cauliflower",
      "sowing_time": "July-August",
      "harvesting_time": "October-November",
      "crop_type": "Kharif",
      "crop_period": "100-120 days"
    },
    {
      "crop_id": 19,
      "crop_name": "Carrot",
      "sowing_time": "October-November",
      "harvesting_time": "February-March",
      "crop_type": "Rabi",
      "crop_period": "120-150 days"
    },
    {
      "crop_id": 20,
      "crop_name": "Lentils (Masoor)",
      "sowing_time": "October-November",
      "harvesting_time": "February-March",
      "crop_type": "Rabi",
      "crop_period": "100-120 days"
    },
    {
      "crop_id": 21,
      "crop_name": "Chickpea (Chana)",
      "sowing_time": "October-November",
      "harvesting_time": "February-March",
      "crop_type": "Rabi",
      "crop_period": "120-150 days"
    },
    {
      "crop_id": 22,
      "crop_name": "Mustard",
      "sowing_time": "October-November",
      "harvesting_time": "February-March",
      "crop_type": "Rabi",
      "crop_period": "120-150 days"
    },
    {
      "crop_id": 23,
      "crop_name": "Sunflower",
      "sowing_time": "October-November",
      "harvesting_time": "February-March",
      "crop_type": "Rabi",
      "crop_period": "90-120 days"
    }
  ]
}
def get_data(crop_id):
  return dic["crops"][crop_id]

 
