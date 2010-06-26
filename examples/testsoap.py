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


from smshosting import ManageSmsService, ManagePhoneBookService, ManageUserService, SmsReceivedService


def libTest():
    
    errors = 0
    
    password = 'password'
    username = 'username'
    host = 'http://ws.smshosting.it'
    
    ###---------------------------------------------------------------------
    #print "TEST 1"
    #print "-"*50
    
    #groups = None
    #sender  = 'Giasone'
    #text = 'Ancora un test dalla libreria per vedere se ora tutto funziona'
    # Instantiate with Basic (HTTP) Authentication
    #test1 = ManageSmsService(username, password, host)
    
    #test1.setNumber('393932999555', '')
    #test1.setNumber('393932222255', '')
    #test1result1 = test1.send(text, sender)
    #print test1result1
    
    #test1.setNumber('393932999555', '')
    #test1.setNumber('393932222255', '')
    #test1result2 = test1.testSend(text, sender)
    #print test1result2
    
    #internalId = '14913734'
    #transactionId = 'b1492a45a136862d3022c548708b7a77'
    #test1result3 = test1.cancelSmsById(internalId, transactionId)
    #print test1result3
        
    #dateTime = datetime.datetime.now()
    #fromDate = '201005011351+0100'
    #toDate = dateTime.strftime("%Y%m%d%H%M+0100")
    #test1result4 = test1.getSmsByDate(fromDate, toDate)
    #print test1result4
    
    #internalId = '11274459'
    #transactionId = '2fb612c7d232c1bbfa347c4cdf21c211'
    #test1result5 = test1.getSmsById(internalId, transactionId)
    #print test1result5

    ###---------------------------------------------------------------------
    #print "TEST 2"
    #print "-"*50
    
    # Instantiate with Basic (HTTP) Authentication
    #test2 = ManagePhoneBookService(username, password, host)
    
    #contact = test2.setContact( "SONA s.r.l.", "Carlo", "Alberto", "393932443399", "055456789", "Via col vento 17", "Mesagne", "BR", "72021", "AD", "carlo@alberto.org")
    #test2result1 = test2.addContact(contact)
    #print test2result1
    
    #group = test2.setGroup('gruppoB', 'descrizione del gruppo')
    #test2result2 = test2.addGroup(group)
    #print test2result2
    
    #mobilePhoneNumber = '393932443399'
    #test2result3 = test2.getContact(mobilePhoneNumber)
    #print test2result3
    
    #groupName = 'SONA s.r.l.'
    #test2result4 = test2.getContactsOfGroup(groupName)
    #print test2result4
    
    #test2result5 = test2.getGroups()
    #print test2result5
    
    #mobilePhoneNumber = "393934469999"
    #test2result6 = test2.removeContact(mobilePhoneNumber)
    #print test2result6
    
    #group = 'GruppoX'
    #test2result7 = test2.removeGroup(group)
    #print test2result7
    
    #contact = test2.setContact( "SONA s.r.l.", "Carlo", "Alberto", "393932333399", "0559876543", "Via col vento 34", "Mesagne", "BR", "71021", "IT", "carlo@planet.org")
    #test2result8 = test2.updateContact(contact)
    #print test2result8


    
    ###---------------------------------------------------------------------
    #print "TEST 3"
    #print "-"*50
    
    #email = 'pippo@pluto.org'
    # Instantiate with Basic (HTTP) Authentication
    #test3 = ManageUserService(username, password, host)
    
    #test3result1 = test3.addEmail2Sms(email)
    #print test3result1
    
    #test3result2 = test3.getUserInfo()
    #print test3result2
    
    #test3result3 = test3.removeEmail2Sms(email)
    #print test3result3
    
    ###---------------------------------------------------------------------
    #print "TEST 4"
    #print "-"*50
    
    # timestamp
    #dateTime = datetime.datetime.now()
    #self.now = None #dateTime.strftime("%Y%m%d%H%M+0100")
    
    #fromDate = '201005011351+0100'
    #toDate = dateTime.strftime("%Y%m%d%H%M+0100")
    # Instantiate with Basic (HTTP) Authentication
    #test4 = SmsReceivedService(username, password, host)
    #test4result1 = test4.getSmsByDate(fromDate, toDate)
    #print test4result1

    
    ###---------------------------------------------------------------------
    
    #print "-"*50
    #print '\nFinished: errors=%d' % errors

  
        
if __name__ == '__main__':
    errors = 0
    libTest()
    print '\nFinished: errors=%d' % errors
