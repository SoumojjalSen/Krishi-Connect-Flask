# Define a dictionary to store scheme information
schemes = {
    "Agriculture": [
        {
            "name": "National Scheme Of Welfare Of Fishermen",
            "description": "Provides financial assistance to fishermen. They can use these for constructing houses and community halls for both recreation and work purposes. Further, through the amount availed under this scheme, fishermen can install tube wells.",
            "eligibility": "Fishermen",
        },
        {
            "name": "Krishonnati Yojana - Sub Mission On Seed And Planting Material (SMSP)",
            "description": "The Sub-Mission on Seeds and Planting Material (SMSP) aims to increase the production of certified / quality seed, increase SRR, upgrade the quality of farm-saved seeds, strengthen the seed multiplication chain, promote new technologies and methodologies in seed production, processing, testing, etc.",
            "eligibility": "Agriculture",
        },
        {
            "name": "Kisan Credit Card",
            "description": "The Kisan Credit Card (KCC) scheme was introduced in 1998 for issue of Kisan Credit Cards to farmers on the basis of their holdings for uniform adoption by the banks so that farmers may use them to readily purchase agriculture inputs and draw cash for their production needs.",
            "eligibility": "Credit Card",
        },
        {
            "name": "National Agriculture Market",
            "description": "e-NAM a pan-India electronic trading portal was launched on 14th April 2016, by the Prime Minister of India, with the aim of networking the existing mandis on a common online market platform as “One Nation One Market” for agricultural commodities in India.",
            "eligibility": "Agriculture",
        },
        {
            "name": "Pradhan Mantri Kisan Samman Nidhi",
            "description": "Farmer welfare scheme by Ministry of Agriculture and Farmers Welfare to provide income support to all landholding farmers' families in the country to supplement their financial needs for procuring various inputs related to agriculture and allied activities as well as domestic needs.",
            "eligibility": "Agricultural Inputs",
        },
        {
            "name": "Sub-mission On Agriculture Mechanization",
            "description": "The Sub-Mission on Agricultural Mechanization was launched in 2014-15 by the Ministry of Agriculture and Farmers’ Welfare.",
            "eligibility": "Agriculture Mechanization",
        },
        {
            "name": "Rashtriya Krishi Vikas Yojana",
            "description": "Rashtriya Krishi Vikas Yojana is a centrally Sponsored scheme. It was initiated in 2007 for ensuring the holistic development of agriculture and allied sectors by allowing states to choose their own agriculture and allied sector development activities as per the district/state agriculture plan.",
            "eligibility": "KRISHI",
        },
        {
            "name": "Agri-Clinics And Agri-Business Centres Scheme",
            "description": "A welfare scheme by the Ministry of Agriculture and Farmers' Welfare was launched in 2002. AC&ABC aims at agricultural development, supplementing the efforts of public extension by providing extension and other services to farmers either on a payment basis or free of cost as per the business model.",
            "eligibility": "Agriculture Business",
        },
        {
            "name": "India Africa Fellowship",
            "description": "India Africa fellowship programme started in 2010-11 under the India-Africa forum summit to support the agricultural resource development in Africa through formal education of African Scientists/Faculty and students in India.",
            "eligibility": "Africa",
        },
        {
            "name": "ICRO Amrit Internship Programme",
            "description": "The IPL Centre for Rural Outreach (ICRO) has launched ICRO Amrit Internship Programme focused on youth productivity for prosperity. The interns will be placed at the headquarters and Regional Offices of NPC/ IPL. The duration of the internship will be 3 months initially, renewable up to four times.",
            "eligibility": "Diploma",
        },
        {
            "name": "Galvanizing Organic Bio-Agro Resources Dhan (GOBARdhan)",
            "description": "GOBARdhan Scheme was launched in April 2018 as a part of the Solid and Liquid Waste Management component under Swachh Bharat Mission (Grameen) to positively impact village cleanliness and generate wealth and energy from cattle and organic waste. The main focus of GOBARDHAN is to keep villages clean.",
            "eligibility": "Agriculture",
        },
        {
            "name": "Pradhan Mantri Matsya Sampada Yojana",
            "description": "Introduced by the Department of Fisheries, Pradhan Mantri Matsya Sampada Yojana (PMMSY) is a scheme to bring about ecologically healthy, economically viable, and socially inclusive development of the fisheries sector of India.",
            "eligibility": "Agriculture",
        },
    ],
    "Education": [
        {
            "name": "Scholarship Scheme for Meritorious Students",
            "description": "Provides scholarships to meritorious students.",
            "eligibility": "Students with high academic performance",
        },
        {
            "name": "National Apprenticeship Promotion Scheme (NAPS)",
            "description": "Promotes apprenticeship training.",
            "eligibility": "Employers and apprentices",
        },
    ],
    "Finance": [
        {
            "name": "Pradhan Mantri Jan Dhan Yojana (PMJDY)",
            "description": "Financial inclusion program.",
            "eligibility": "All citizens",
        },
        {
            "name": "Startup India",
            "description": "Promotes startup businesses.",
            "eligibility": "Startups",
        },
    ],
    "Services": [
        {
            "name": "e-District Services",
            "description": "Provides various government services online.",
            "eligibility": "Citizens",
        },
        {
            "name": "Digital India",
            "description": "Promotes digital services and infrastructure.",
            "eligibility": "All citizens",
        },
    ],
    "Health": [
        {
            "name": "Ayushman Bharat",
            "description": "Aims to provide health coverage to economically vulnerable families.",
            "eligibility": "Economically vulnerable families",
        },
        {
            "name": "Janani Suraksha Yojana (JSY)",
            "description": "Promotes institutional deliveries for pregnant women.",
            "eligibility": "Pregnant women",
        },
    ],
    # Add more sectors and schemes here
}

# Function to get schemes based on the selected sector
def get_schemes_by_sector(sector):
    return schemes.get(sector, [])

# print(get_schemes_by_sector("Agriculture"))

# # Get user input for the sector
# selected_sector = input("Enter the name of the sector: ")

# # Get schemes for the selected sector
# selected_schemes = get_schemes_by_sector(selected_sector)

# if selected_schemes:
#     print(f"Schemes in the {selected_sector} sector:")
#     for scheme in selected_schemes:
#         print("Name:", scheme["name"])
#         print("Description:", scheme["description"])
#         print("Eligibility:", scheme["eligibility"])
#         print()
# else:
#     print("No schemes found for the selected sector.")
