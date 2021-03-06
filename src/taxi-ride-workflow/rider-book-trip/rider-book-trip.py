import datetime
import json
from random import randint

from util import updateTripInfo, getTripInfo, DecimalEncoder

def lambda_handler(event, context):

    #print(event)
    
    #rider_id = 69257
    #rider_mobile = "+11609467790"
    
    rider_id = int(event['queryStringParameters']['rider_id'])
    rider_mobile = event['queryStringParameters']['rider_mobile']

    rider_name = "person" + str(rider_id)
    print("Rider Name=" + rider_name)

    riderid = rider_name + "@example.com"
    rider_email = riderid
    print("Rider ID= " + riderid)

    print("Rider Mobile = " + rider_mobile)

    pickUpDateTime = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    id =  ''.join(["%s" % randint(0, 9) for num in range(0, 7)])
    tripinfo = pickUpDateTime +"," + id 
    print("Trip Info= " + tripinfo)

    status = "Booked"
    print("Status=" + status)

    tripInfo = {
        "riderid" : riderid,
        "tripinfo" : tripinfo,
        "RIDER_ID" : rider_id,
        "RIDER_MOBILE" : rider_mobile,
        "PICKUP_DATETIME" : pickUpDateTime,
        "RIDER_NAME" : rider_name,
        "RIDER_EMAIL" : rider_email,
        "Status" : status
    }

    print("Trip Information =" + json.dumps(tripInfo, indent=2))

    response = updateTripInfo(tripInfo)
    print("Trip information has been updated to Trips table")

    print("Rider Booking Trip Information =" + json.dumps(response['Attributes'], indent = 4, cls=DecimalEncoder))
    
    responseObjects = {}
    responseObjects['statusCode'] = 200
    responseObjects['headers'] = {}
    responseObjects['headers']['Content-Type'] = 'application/json'
    responseObjects['body'] = json.dumps(response['Attributes'], indent = 4, cls=DecimalEncoder)
    
    return responseObjects