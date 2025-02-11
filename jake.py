import json

with open('sample-data.json') as f:
    data = json.load(f)

header = ["DN", "Description", "Speed", "MTU"]
separator = "-" * 80  


print("Interface Status")
print("=" * 80)
print(f"{header[0]:<50} {header[1]:<20} {header[2]:<6} {header[3]:<6}")
print(separator)

for entry in data["imdata"]: 
    attributes = entry["l1PhysIf"]["attributes"]
    
    dn = attributes.get('dn', 'N/A')
    description = attributes.get('descr', 'N/A')
    speed = attributes.get('speed', 'N/A')
    mtu = attributes.get('mtu', 'N/A')
    
    print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")
