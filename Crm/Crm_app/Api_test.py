# import requests
# import json




# def api_Data():
#     Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/8469789298/GLUSR_MOBILE_KEY/MTYwMjgzMTEyNS40NDg0IzExMjc0OTQ0/")
#     if Url.status_code == 200:
#         data = Url.json()
#         print("Sanju")
#         for i in range(len(data)):
#             print(i)
#             if i == 5:
#                 print("Sanu")
#                 x = data[5]
#                 print("x")
#                 RN= x["RN"] 
#                 QUERY_ID= x["QUERY_ID"] 
#                 QTYPE= x["QTYPE"]
#                 SENDERNAME= x["SENDERNAME"]
#                 SENDEREMAIL= x["SENDEREMAIL"]
#                 SUBJECT= x["SUBJECT"]
#                 DATE_RE= x["DATE_RE"]
#                 DATE_R= x["DATE_R"]
#                 DATE_TIME_RE= x["DATE_TIME_RE"]
#                 GLUSR_USR_COMPANYNAME= x["GLUSR_USR_COMPANYNAME"] 
#                 READ_STATUS= x["READ_STATUS"]
#                 SENDER_GLUSR_USR_ID= x["SENDER_GLUSR_USR_ID"]
#                 MOB= x["MOB"]
#                 COUNTRY_FLAG= x["COUNTRY_FLAG"]
#                 QUERY_MODID= x["QUERY_MODID"]
#                 LOG_TIME= x["LOG_TIME"]
#                 QUERY_MODREFID= x["QUERY_MODREFID"]
#                 DIR_QUERY_MODREF_TYPE= x["DIR_QUERY_MODREF_TYPE"]
#                 ORG_SENDER_GLUSR_ID= x["ORG_SENDER_GLUSR_ID"]
#                 ENQ_MESSAGE= x["ENQ_MESSAGE"]
#                 ENQ_ADDRESS= x["ENQ_ADDRESS"]
#                 ENQ_CALL_DURATION= x["ENQ_CALL_DURATION"]
#                 ENQ_RECEIVER_MOB= x["ENQ_RECEIVER_MOB"]
#                 ENQ_CITY= x["ENQ_CITY"]
#                 ENQ_STATE= x["ENQ_STATE"]
#                 PRODUCT_NAME= x["PRODUCT_NAME"]
#                 COUNTRY_ISO= x["COUNTRY_ISO"]
#                 EMAIL_ALT= x["EMAIL_ALT"]
#                 MOBILE_ALT= x["MOBILE_ALT"]
#                 PHONE= x["PHONE"]
#                 PHONE_ALT= x["PHONE_ALT"]
#                 IM_MEMBER_SINCE= x["IM_MEMBER_SINCE"]
#                 TOTAL_COUNT = x["TOTAL_COUNT"]
#                 print(TOTAL_COUNT)
            
            
            
# api_Data()
