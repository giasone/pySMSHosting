#!/usr/bin/env python

#    Copyright (C) 2010 Gianluca Urgese <g.urgese@jasone.it>    
#    
#	 pySmsHosting is a library for Python that wraps the SmsHosting.it Web Service API.
#	
#	 Questions, comments? g.urgese@jasone.it
#
#    pySmsHosting is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    pySmsHosting is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pySmsHosting.  If not, see <http://www.gnu.org/licenses/>.
#    
#    Require SUDS - a lightweight SOAP python client for consuming Web Services.
#    Download and info  at https://fedorahosted.org/suds/
#


__license__ = 'GPL v.2 http://www.gnu.org/licenses/gpl.txt'
__author__ = "Gianluca Urgese <g.urgese@jasone.it>"
__version__ = '0.4'

import sys
import logging
import traceback as tb
import suds.metrics as metrics
from suds import null, WebFault
from suds.client import Client
import datetime
import time

errors = 0

#setup_logging()

#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.metrics').setLevel(logging.DEBUG)
#logging.getLogger('suds').setLevel(logging.DEBUG)



class pySmsHostingError(Exception):
	def __init__(self, msg, error_code=None):
		self.msg = msg
	def __str__(self):
		return repr(self.msg)
		
            
class ManageSmsService:
    def __init__(self, username, password, host = 'http://ws.smshosting.it'):
        """ManageSmsService( username, password, host = 'http://ws.smshosting.it')

			Instantiates an instance of ManageSmsService.

			Parameters:
				username - Your SmsHosting.it username.
				password - Your SmsHosting.it secret key.
				host - Server address.
        """

        self.username = username
        self.password = password
        if host.endswith('/'):
            self.address = host + 'smsWebService/ManageSms?wsdl'
        else:
            self.address = host + '/smsWebService/ManageSms?wsdl'
        
		# Check and set up authentication
        if self.username is not None and self.password is not None:
			# Assume Basic authentication ritual
            self.client = Client(self.address)

        else:
            raise pySmsHostingError("Authentication failed with your provided credentials. Try again? (%s failure)" % `e.code`, e.code)
            
        self.numbers = self.client.factory.create('sendPayLoad')
        #print self.numbers

    def setNumber(self, number, customerId = None):
        
        phone = self.client.factory.create('msisdn')
        phone.customerId = customerId
        phone.number = number
        self.numbers.numbers.append(phone)
        
        return
        

    def send(self, text, sender = "SMSHosting.it", dateTime = None, groups = None, transactionId = None ):
        """send(xs:string password, xs:string username, xs:string dateTime, xs:string from, xs:string[] groups, msisdn[] numbers, xs:string text, xs:string transactionId, )
        """
        global errors

        try:        
            result = self.client.service.send(self.password, self.username, dateTime, sender, groups, self.numbers.numbers, text, transactionId)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("send() failed with a %s error code." % `e.code`, e.code)
			
            
    def testSend(self, text, sender = "SMSHosting.it", dateTime = None, groups = None, transactionId = None):
        """testSend(xs:string password, xs:string username, xs:string dateTime, xs:string from, xs:string[] groups, msisdn[] numbers, xs:string text, xs:string transactionId, )
        """
        global errors

        try:          
            result = self.client.service.testSend(self.password, self.username, dateTime, sender, groups, self.numbers.numbers, text, transactionId)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("testSend() failed with a %s error code." % `e.code`, e.code)
			

    def cancelSmsById(self, internalId, transactionId):
        """cancelSmsById(xs:string password, xs:string username, xs:int[] internalId, xs:string transactionId, )
        """
        global errors

        try:
            # Check if parameters missing 
            if internalId is not None and transactionId is not None:
                result = self.client.service.cancelSmsById(self.password, self.username, internalId, transactionId)
                sent = self.client.last_sent()
                rcvd = self.client.last_received()
                #print '\nreply(\n%s\n)\n' % result
                return result
            else:
                raise pySmsHostingError("cancelSmsById()'s parameter missing or not valid, check it and go ahead.") 
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("cancelSmsById() failed with a %s error code." % `e.code`, e.code)
			
    
    def getSmsByDate(self, fromDate, toDate ):
        """getSmsByDate(xs:string password, xs:string username, xs:string fromDate, xs:string toDate, )
        """
        global errors

        try:        
            result = self.client.service.getSmsByDate(self.password, self.username, fromDate, toDate)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getSmsByDate() failed with a %s error code." % `e.code`, e.code)
			
    
    def getSmsById(self, internalId, transactionId ):
        """getSmsById(xs:string password, xs:string username, xs:int[] internalId, xs:string transactionId, )
        """
        global errors

        try:        
            result = self.client.service.cancelSmsById(self.password, self.username, internalId, transactionId)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getSmsById() failed with a %s error code." % `e.code`, e.code)

####################################################################################################################

class ManagePhoneBookService:
    def __init__(self, username = None, password = None, host = 'http://ws.smshosting.it'):
        """ManagePhoneBookService( username = None, password = None, host = 'http://ws.smshosting.it')

			Instantiates an instance of ManagePhoneBookService.

			Parameters:
				username - Your SmsHosting.it username.
				password - Your SmsHosting.it secret key.
				host - Server address.
				
        """

        self.username = username
        self.password = password

        if host.endswith('/'):
            self.address = host + 'smsWebService/ManagePhoneBook?wsdl'
        else:
            self.address = host + '/smsWebService/ManagePhoneBook?wsdl'
              
		# Check and set up authentication
        if self.username is not None and self.password is not None:
			# Assume Basic authentication ritual
            self.client = Client(self.address)

        else:
            raise pySmsHostingError("Authentication failed with your provided credentials. Try again? (%s failure)" % `e.code`, e.code)


        
    def setContact(self, groupsName = None, lastname = None, name = None, mobilePhoneNumber = None, homePhoneNumber = None, address = None, city = None, province = None, postCode = None, country = None, email = None):
        
        contact = self.client.factory.create('contact')
        contact.groupsName = groupsName
        contact.lastname = lastname
        contact.name = name
        contact.mobilePhoneNumber = mobilePhoneNumber
        contact.homePhoneNumber = homePhoneNumber
        contact.address = address
        contact.city = city
        contact.province = province
        contact.postCode = postCode
        contact.country = country
        contact.email = email

        return contact
                    

    def addContact(self, contact):
        """addContact(xs:string password, xs:string username, contact contact, )
        """
        global errors

        try:        
            result = self.client.service.addContact(self.password, self.username, contact)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("addContact() failed with a %s error code." % `e.code`, e.code)
            
    def setGroup(self, name, description = None):
        
        group = self.client.factory.create('contactGroup')
        group.name = name
        group.description = description
        
        return group
        
            
    def addGroup(self, group):
        """addGroup(xs:string password, xs:string username, contactGroup group, )
        """
        global errors

        try:
            result = self.client.service.addGroup(self.password, self.username, group)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("addGroup() failed with a %s error code." % `e.code`, e.code)
			

    def getContact(self, mobilePhoneNumber):
        """getContact(xs:string password, xs:string username, xs:string mobilePhoneNumber, )
        """
        global errors

        try:
            result = self.client.service.getContact(self.password, self.username, mobilePhoneNumber)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result 
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getContact() failed with a %s error code." % `e.code`, e.code)
			
    
    def getContactsOfGroup(self, groupName ):
        """getContactsOfGroup(xs:string password, xs:string username, xs:string groupName, )
        """
        global errors

        try:        
            result = self.client.service.getContactsOfGroup(self.password, self.username, groupName)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getContactsOfGroup() failed with a %s error code." % `e.code`, e.code)
			
    
    def getGroups(self):
        """getGroups(xs:string password, xs:string username, )
        """
        global errors

        try:        
            result = self.client.service.getGroups(self.password, self.username)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getGroups() failed with a %s error code." % `e.code`, e.code)
			
    def removeContact(self, mobilePhoneNumber ):
        """removeContact(xs:string password, xs:string username, xs:string mobilePhoneNumber, )
        """
        global errors

        try:        
            result = self.client.service.removeContact(self.password, self.username, mobilePhoneNumber)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getSmsById() failed with a %s error code." % `e.code`, e.code)
			
    def removeGroup(self, name ):
        """removeGroup(xs:string password, xs:string username, xs:string name, )
        """
        global errors

        try:                 
            result = self.client.service.removeGroup(self.password, self.username, name)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("removeGroup() failed with a %s error code." % `e.code`, e.code)
			
    def updateContact(self, contact ):
        """updateContact(xs:string password, xs:string username, contact contact, )
        """
        global errors

        try:
            result = self.client.service.updateContact(self.password, self.username, contact)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("updateContact() failed with a %s error code." % `e.code`, e.code)

################################################################################################################

class ManageUserService:
    def __init__(self, username = None, password = None, host = 'http://ws.smshosting.it'):
        """ManageUserService( username = None, password = None, host = 'http://ws.smshosting.it')

			Instantiates an instance of ManageUserService.

			Parameters:
				username - Your SmsHosting.it username.
				password - Your SmsHosting.it secret key.
				host - Server address.
				
        """

        self.username = username
        self.password = password
        if host.endswith('/'):
            self.address = host + 'smsWebService/ManageUser?wsdl'
        else:
            self.address = host + '/smsWebService/ManageUser?wsdl'
              
		# Check and set up authentication
        if self.username is not None and self.password is not None:
			# Assume Basic authentication ritual
            self.client = Client(self.address)

        else:
            raise pySmsHostingError("Authentication failed with your provided credentials. Try again? (%s failure)" % `e.code`, e.code)


    def addEmail2Sms(self, email):
        """addEmail2Sms(xs:string password, xs:string username, xs:string email, )
        """
        global errors

        try:
            result = self.client.service.addEmail2Sms(self.password, self.username, email)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("addEmail2Sms() failed with a %s error code." % `e.code`, e.code)
            
    def getUserInfo(self):
        """getUserInfo(xs:string password, xs:string username, )
        """
        global errors

        try:
            result = self.client.service.getUserInfo(self.password, self.username)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getUserInfo() failed with a %s error code." % `e.code`, e.code)
			

    def removeEmail2Sms(self, email):
        """removeEmail2Sms(xs:string password, xs:string username, xs:string email, )
        """
        global errors

        try:
            result = self.client.service.removeEmail2Sms(self.password, self.username, email)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
                    
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("removeEmail2Sms() failed with a %s error code." % `e.code`, e.code)
			
    
#####################################################################################################################

class SmsReceivedService:
    def __init__(self, username = None, password = None, host = 'http://ws.smshosting.it'):
        """SmsReceivedService( username = None, password = None, host = 'http://ws.smshosting.it')

			Instantiates an instance of SmsReceivedService.

			Parameters:
				username - Your SmsHosting.it username.
				password - Your SmsHosting.it secret key.
				host - Server address.
            
        """

        self.username = username
        self.password = password
        if host.endswith('/'):
            self.address = host + 'smsWebService/SmsReceived?wsdl'
        else:
            self.address = host + '/smsWebService/SmsReceived?wsdl'
              
		# Check and set up authentication
        if self.username is not None and self.password is not None:
			# Assume Basic authentication ritual
            self.client = Client(self.address)
        else:
            raise pySmsHostingError("Authentication failed with your provided credentials. Try again? (%s failure)" % `e.code`, e.code)

    
    def getSmsByDate(self, fromDate, toDate ):
        """getSmsByDate(xs:string password, xs:string username, xs:string fromDate, xs:string toDate, )
        """
        global errors

        try:        
            result = self.client.service.getSmsByDate(self.password, self.username, fromDate, toDate)
            sent = self.client.last_sent()
            rcvd = self.client.last_received()
            #print '\nreply(\n%s\n)\n' % result
            return result
        
        except WebFault, f:
            errors += 1
            print f
            print f.fault
        except Exception, e:
            errors += 1
            print e
            tb.print_exc()
        except HTTPError, e:
			raise pySmsHostingError("getSmsByDate() failed with a %s error code." % `e.code`, e.code)
			
