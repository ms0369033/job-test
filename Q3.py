userIds = ['U01', 'U02', 'U03'] 
orderIds = ['T01', 'T02', 'T03', 'T04'] 
userOrders = [			
    { 'userId': 'U01', 'orderIds': ['T01', 'T02'] },
 	{ 'userId': 'U02', 'orderIds': [] },
 	{ 'userId': 'U03', 'orderIds': ['T03'] },
]
userData = { 'U01': 'Tom', 'U02': 'Sam', 'U03': 'John' } 
orderData = {						
'T01': { 'name': 'A', 'price': 499 }, 
'T02': { 'name': 'B', 'price': 599 },
'T03': { 'name': 'C', 'price': 699 }, 
'T04': { 'name': 'D', 'price': 799 }
} 
result = []
for userId in userIds:
    order = []
    for userOrder in userOrders:
        if userOrder['userId'] == userId:
            for orderId in userOrder['orderIds']:
                order.append({'id':orderId} | orderData[orderId])
                
    result.append(
        {
            'user':{
                'id':userId,
                'name':userData[userId]
            },
            'orders':order
        })

print(result)
