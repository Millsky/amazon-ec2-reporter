from flask import Flask, current_app ,jsonify,request,abort
import boto3

#set up static resources so we can serve the ng front-end
app = Flask(__name__,static_url_path='/static')

@app.route('/api/ec2Info', methods=['POST'])
def retrieveEC2Info():
    #Get the json that came in
    request_data = request.get_json(force=True)
    #set the aws variables 
    user_aws_key = request_data['aws_access_key_id']
    user_secret_key = request_data['aws_secret_access_key']
    #Get all regions per: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions
    regions = ['us-east-1','us-east-2','us-west-1','us-west-2','ca-central-1','eu-west-1','eu-central-1','eu-west-2','ap-northeast-1','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-south-1','sa-east-1']
    ec2Info = []
    try:
        for r in regions:
            ec2 = boto3.resource('ec2',region_name=r,aws_access_key_id= user_aws_key,aws_secret_access_key= user_secret_key)
            #For each region get all instaces active in that region
            for instance in ec2.instances.all():
                #Special function for checking names on tags
                name = "No Name Found"
                if instance.tags != None:
                    for tags in instance.tags:
                        if tags["Key"] == 'Name':
                            name = tags["Value"]
                #Pull all required information
                ec2InstanceInfo = {
                    'Name': str(name),
                    'ID': str(instance.id),
                    'Type': str(instance.instance_type),
                    'Region': str(r),
                    'Zone': str(instance.placement["AvailabilityZone"]),
                    'State': str(instance.state["Name"]),
                    'Public_IP': str(instance.public_ip_address),
                    'Launch_Time': str(instance.launch_time)
                }
                #Append dic as row
                ec2Info.append(ec2InstanceInfo)
    
    
        return jsonify(ec2Info)
    except:
        #Return error 400 if we can't login
        abort(400)

#return front-end
@app.route('/')
def divvy():
    return current_app.send_static_file('index.html')
