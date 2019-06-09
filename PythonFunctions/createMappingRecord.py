# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:58:36 2019

@author: gvandeyk
"""


def createMappingRecord(MappingData):

    # Initialising the MappingRecord dictionary
    MappingRecord = {'Customer': '',
                     'TradingPartner': '',
                     'MessageDirection': '',
                     'SourceMessage': '',
                     'TargetMessage': ''
                     }

    for Lines in MappingData:
        if 'Customer:' in Lines:
            MappingRecord['Customer'] = Lines.split(":")[1:]
        elif 'Trading Partner:' in Lines:
            MappingRecord['TradingPartner'] = Lines.split(":")[1:]
        elif 'Message Direction:' in Lines:
            MappingRecord['MessageDirection'] = Lines.split(":")[1:]
        elif 'Source Standard:' in Lines:
            MappingRecord['SourceMessage'] = Lines.split(":")[1:]
        elif 'Target Standard:' in Lines:
            MappingRecord['TargetMessage'] = Lines.split(":")[1:]
        else:
            pass

    return MappingRecord  # Type dictionary

if __name__ == '__main__':
    
    MappingData = '''
From:	Budhwani, Santosh
Sent:	vrijdag 7 juni 2019 9:25
To:	Van Deyk, Geert
Cc:	Kumar, Ashok; Block, Patrick
Subject:	New Database entry: SKF US: FCA-Delins -XML

Hi Geert,

Could you please create a record and provide me with a name for the translation with the following 
properties: 
  
Customer: FCA

Trading Partner: SKF US

Message Direction: INBOUND

Source Standard: Odette DELINS v3.1

Target Standard: XML Message ProcessSalesDeliverySchedule_3.0

Model
:



Thanks and Regards,
Santosh Budhwani

'''.split('\n')
    for item in createMappingRecord(MappingData).items():
        print(item)
