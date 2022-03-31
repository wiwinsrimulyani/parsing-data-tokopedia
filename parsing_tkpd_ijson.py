#IF SOMEDAY WE ARE APART, I HOPE THAT THIS CODE STILL VALUABLE ~Wiwin. 
# #done in 2 days with two time changing the code.

import csv
import ijson

filename = 'shop_januari_tkpd.json'


f1 = open('parsed_tkpd_january_recovered.csv', 'w', newline='', encoding="utf-8")
multiple_values=True
with f1:
  writer = csv.writer(f1)
  writer.writerow(['id_', 'activeProduct', 'location', 'isAllowManage', 'branchLinkDomain', 'isOpen', 'description', 'domain', 'shopID', 'name', 'tagLine', 'defaultSort', 'openSince', 'totalFavorite', 'alreadyFavorited', 'avatar', 'cover', 'area', 'districtName', 'address_id', 'email', 'phone', 'shippingLoc_districtName', 'shippingLoc_cityName', 'productSold', 'totalTxSuccess', 'totalShowcase', 'shopStatus', 'statusMessage', 'statusTitle', 'closedInfo_closedNote', 'closedInfo_until', 'closedInfo_reason', 'isGold', 'isGoldBadge', 'isOfficial', 'badge', 'shopTier', 'shipping', 'customSEO_title', 'customSEO_description', 'customSEO_buttomContent', 'scraping_date' ])
  
  with open(filename, 'r', encoding="utf-8") as f:
    objects = ijson.items(f, 'item')
    i = 1
    for number in objects:
      shop_list = []
      print('parsing {} th data'.format(i))
      i = i + 1
      try:
        id_ = number['_id']
        shop_list.append(id_['$oid'])

      except:
        shop_list.append(None)    

# yoksiiii my code always been masterpiece
# sedih xixixixi. can i still write kinda this code in daerah :( why i couldnt  hufffffffffft 

      try:
        shop_list.append(number['activeProduct'])
      except:
        shop_list.append(None)      

      try:
        shop_list.append(number['location'])
      except:
        shop_list.append(None)

      try:
        shop_list.append(number['isAllowManage'])
      except:
        shop_list.append(None)

      try:
        shop_list.append(number['branchLinkDomain'])
      except:
        shop_list.append(None)

      try:
        shop_list.append(number['isOpen'])
      except:
        shop_list.append(None)

      #shopCore
      try:
        sc = number['shopCore']
      except:
        'is none'
      try:
        shop_list.append(sc['description'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sc['domain'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sc['shopID'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sc['name'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sc['tagLine'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sc['defaultSort'])
      except:
        shop_list.append(None)

      #createdInfo
      #this code written with tears .... huftttttttttttttttttttttt

      try:
        ci = number['createInfo']
      except:
        'is none'
      try:
        shop_list.append(ci['openSince'])
      except:
        shop_list.append(None)

      #favoriteData
      try:
        fd = number['favoriteData']
      except:
        'is none'
      try:
        shop_list.append(fd['totalFavorite'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(fd['alreadyFavorited']) 
      except:
        shop_list.append(None) 


      #shopAssets
      try:     
        sa = number['shopAssets']
      except:
        'is none'
      try:
        shop_list.append(sa['avatar'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(sa['cover']) 
      except:
        shop_list.append(None)


      #address
      try:
        ad = number['address']
      except:
        'is none'

      try:
        ad_0 = ad[0]
      except:
        ad_0 = ''
      try:
        area = ad_0['area']
        districtName = ad['districtName']
        add_id = ad['id']
        email = ad['email']
        phone = ad['phone']
      except:
        area = None
        districtName = None
        add_id = None
        email = None
        phone = None

      try:        
        shop_list.append(area)      
      except:
        shop_list.append(None)
      try:        
        shop_list.append(districtName)
      except:
        shop_list.append(None)
      try:        
        shop_list.append(add_id)  
      except:
        shop_list.append(None)
      try:        
        shop_list.append(email)
      except:
        shop_list.append(None)
      try:        
        shop_list.append(phone)
      except:
        shop_list.append(None)  

  
        
        #shippingLoc
      try:        
        sl = number['shippingLoc']
      except:
        'is none'
      try:        
        shop_list.append(sl['districtName'])
      except:
        shop_list.append(None)
      try:        
        shop_list.append(sl['cityName'])
      except:
        shop_list.append(None)

  
        
        #shopStats
      try:        
        st = number['shopStats']
      except:
        'is none'
      try:        
        shop_list.append(st['productSold'])
      except:
        shop_list.append(None)
      try:        
        shop_list.append(st['totalTxSuccess'])
      except:
        shop_list.append(None)
      try:        
        shop_list.append(st['totalShowcase'])
      except:
        shop_list.append(None)

  
        
        #statusInfo
      try:        
        si = number['statusInfo']
      except:
        'is none'
      try:        
        shop_list.append(si['shopStatus'])
      except:
        shop_list.append(None)
      try:        
        shop_list.append(si['statusMessage'])
      except:
        shop_list.append(None)
      try:        
        shop_list.append(si['statusTitle'])
      except:
        shop_list.append(None)       


  
        
        #closedInfo
      try:  
        ci = number['closedInfo']
      except:
        'is none'
      try:  
        shop_list.append(ci['closedNote'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(ci['until'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(ci['reason'])
      except:
        shop_list.append(None)

  
        
        #goldOS
      try:  
        go = number['goldOS']
      except:
        'is none'
      try:  
        shop_list.append(go['isGold'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(go['isGoldBadge'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(go['isOfficial'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(go['badge'])
      except:
        shop_list.append(None)
      try:  
        shop_list.append(go['shopTier'])
      except:
        shop_list.append(None)
  
        
        #shipmentInfo
      try:  
        si = number['shipmentInfo']
      except:
        'is none'
      shipment_list = []
      for s in si:
        shipment_list.append(s['name'])
      try:
        shop_list.append(','.join(shipment_list))
      except:
        shop_list.append(None)


      #customSEO
      try:
        cs = number['customSEO']
      except:
        'is none'
      try:
        shop_list.append(cs['title'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(cs['description'])
      except:
        shop_list.append(None)
      try:
        shop_list.append(cs['bottomContent'])
      except:
        shop_list.append(None)

      try:
        shop_list.append(number['scraping_date'])
      except:
        shop_list.append(None)

    
      #write the row
      writer.writerow(shop_list)

f.close()
f1.close()


