# Problem #2:
# Complete three different classes, Postman, Client, and Email to imitate email system as below  

#    class Email: 
# """
# Every email object has 3 instance attributes: the message, the sender (their name), and the addressee (the destination's name). 
# """ 
#  		       def __init__(self, msg, sender, addressee): 
# """ Initialize the class members """


#    class Postman: 
# """
# Each Postman has an instance attribute clients, which is a dictionary that associates client names with client objects. 
# """
#        def __init__(self): 
# self.clients = {} 
#       def send(self, email): 
# """
# Take an email and put it in the inbox of the client it is addressed to. """ 

#       def register_client(self, client, client_name): 
# """
# Takes a client object and client_name and adds it to the clients instance attribute. 
# """

#  class Client: 
# """
# Every Client has instance attributes name (which is used for addressing emails to the client), mailman (which is used to send emails out to other clients), and inbox (a list of all emails the client has received). 
# """ 
#       def __init__(self, mailman, name): 
# self.inbox = []
    
#       def compose(self, msg, recipient): 
# """
# Send an email with the given message msg to the given recipient. 
# """ 
#       def receive(self, email): 
# """
# Take an email and add it to the inbox of this client. 
# """


class Email():
    def __init__(self, msg, sender, addressee):
        self.msg = msg
        self.sender = sender
        self.addressee = addressee


class Postman(): #each postman has an instance attribute clients 
    def __init__(self): #which is a dictionary that associates client names with client objects
        self.clients = {}

    def send(self, email): #take an email and put it in the email it is addressed to 
        if (email.addressee in self.clients):
            self.clients[email.addressee].receive(email)
    
    def register_client(self, client, client_name): #takes a client object and client name and adds it to the clients instance attribute
        self.clients[client_name] = client

##
# Every client has instance attribute name (which is used for addressing emails to the client)
# mailman which is used to send emails out to other clients
# and inbox (a list of all emails the client has received)
##

class Client():
    def __init__(self, mailman, name):
        self.inbox = []
        self.outbox = []
        self.name = name
        self.mailman = mailman
        mailman.register_client(self, name)

    def compose(self, msg, recipient): #send an email with the given message msg to the given recipient
        emailToSend = Email(msg, self.name, recipient.name )
        self.outbox.append(emailToSend)
        self.mailman.send(emailToSend)

    def receive(self, email): #take an email and add it to the inbox of this client
        self.inbox.append(email)


#creates a postman instance which tracks all clients
postman = Postman()

#creates a new client user1 and register to postman so it adds to its known clients list
user1 = Client(postman, 'user1@example.com' )

#creates another client instance as sender which sends email to the user1
sender1 = Client(postman, 'sender1@example.com')

# creates a new email with content, sender and receiver name
securityEmailContent = """Hi! \n
There has been some recent security updates made to your account.
If you are unaware of these changes, please reset your password immediately.

Thanks,
Support
"""
# securityEmail = Email(securityEmailContent, 'sender1', 'user1')

sender1.compose(securityEmailContent, user1)

print("senders outbox", sender1.outbox)
print("first user's inbox", user1.inbox)

print("first user's first email - sender =", user1.inbox[0].sender, ", message = ", user1.inbox[0].msg)






