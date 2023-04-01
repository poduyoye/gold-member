#Create an empty list
ServiceInventory = []

#Populate the list using the append or insert.
ServiceInventory.append("Cloud9")
ServiceInventory.append("DynamoDB")
ServiceInventory.append("RDS")
ServiceInventory.append("CodeCommit")

#Print the list
print("ServiceInventory")

#Print the lenght of the list
print(len(ServiceInventory))

#Remove two specific services from the list by name or index
ServiceInventory.remove("DynamoDB")
ServiceInventory.remove("RDS")

#Print the new list
print("ServiceInventory")

#Print the new lenght of the list
print(len(ServiceInventory))