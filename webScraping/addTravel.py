import requests
from bs4 import BeautifulSoup

s = requests.Session()
payload = {'username' : 'kajeffr1', 'password' : 'Jflwin500!','lt': 'LT-59727-7u4hczeIKTTCpEXkgoaGuEFjtr2eD2', 'execution' : 'e1s1', '_eventId': 'submit'}



r = s.post('https://my.asu.edu')
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())


#r2 = s.post(r'https://ns-forms.eboces.org/names.nsf?Login', o use your session and get or post:

#r2 = s.get('some other page behind the login page')
#r3 = s.post('some other page with a post method', payload)


'''
import requests
from bs4 import BeautifulSoup
import html5lib
#import urllib3
#from urllib.parse import urlencode

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

login = {
    'Username: kjeffreys',
    'Password: Jflwin100#',
    'RedirectTo: /MileageReimbursement.nsf'
}

with requests.Session() as s:
    # if needed, query the page again for the html, then parse to find ids
    url = "https://ns-forms.eboces.org/splash.nsf/MileageReimbursement.nsf"
    #name="_DominoForm" ...form with the action for login
    r = s.get(url, headers=headers)
   
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.find('input', attrs: {'name': '_DominoForm' })['value']
    #r = s.post(url, login)
    for el in soup:
        print(el)
    
'''
'''

    # START login
    #url = "https://ns-forms.eboces.org/splash.nsf/"
    #r = s.post(url, login)
    #soup = bs4.BeautifulSoup(r.text, 'html.parser')
    #for el in soup.select('td'):
    #    print(el)
    
'''
'''
http = urllib3.PoolManager()
url = "https://ns-forms.eboces.org/MileageReimbursement.nsf/addReimbursement?open&a=add&tn=mileageTable"

'''
'''
data = {"From" : "DO", "To": "Fleetwood", "numMiles": "2.8", "travelPurpose" : "service calls"}
r = requests.post(url, data)
print(r.text)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
'''
'''

data2 = {"user-id" : "kjeffreys", "pw-id" : "Jflwin100#"}
encoded_data = urlencode({"user-id" : "kjeffreys"}, {"pw-id" : "Jflwin100#"}) #, {"pw-id" : "Jflwin100#"})
print(type(encoded_data))
rl = "https://ns-forms.eboces.org/names.nsf?Login?" + encoded_data
r2 = http.request("POST", encoded_data)
soup2 = bs4.BeautifulSoup(r2.text)

#print(soup2.text)

'''
'''
Works, beautifully
for el in soup.select('div'):
    print(el)
'''


'''
import urllib
import urllib2

list1 = ['DO', 'Fleetwood', '2.8']


content = urllib2.urlopen(form method="post" action="\"/MileageReimbursement.nsf/addReimburserment?OpenForm&Seq=1&a=add&tn=mileageTable\" name=\"__addReimbursement\"")
print content.readlines()
'''

'''
<form method="post" action="/MileageReimbursement.nsf/addReimbursement?OpenForm&amp;Seq=1&amp;a=add&amp;tn=mileageTable" name="_addReimbursement">
<input type="hidden" name="__Click" value="0"><div style="display:none;">
	
<input name="Query_String" value="open&amp;a=add&amp;tn=mileageTable">
	
<input name="tste_DialogAction" value="add">
	
<input name="tste_TableName" value="mileageTable">
	
<input name="tste_RowNumber" value="">
</div><br>
<style type="text/css">
@import url(/MileageReimbursement.nsf/jquery-ui-1.7.3.custom.css?OpenCssResource);
</style>
<style type="text/css">
body, td, input, select {
	font: 8pt Verdana, Arial, sans-serif;
}
h3 {
	font-size: 1em;
	font-weight: bold;
	color: navy;
	padding: 8px 0;
	margin: 0;
}
.helpInstructions {
	color: gray;
	font-size: 8pt;
	font-style: italic;
}
.inputTable td {
	padding: 4px;
	border-bottom: 1pt solid #eee;
}
table.inputTable {
	border-top: 1pt solid #eee;
	width: 600px;
}
table.inputTable td.titleCol {
	background: #F7F7F7;
}
.datePickerIcon {
	position: relative;
	top: 2px;
	margin-left: -2px;
}
.namePickerIcon {
	position: relative;
	top: 2px;
	margin-left: -2px;
}
.ui-datepicker-trigger {
	position: relative;
	top: 2px;
	margin-left: 2px;
}
</style>
 
<span style="display:none">
<br>

<table class="inputTable" border="0" cellspacing="0" cellpadding="0">
<tbody><tr valign="top"><td width="133">TravelTo</td><td width="218"> 
<input name="TravelTo" value="" id="TravelTo"> </td></tr>

<tr valign="top"><td width="133"><img width="1" height="1" src="/icons/ecblank.gif" border="0" alt=""></td><td width="218"> 
<input name="Mileage" value="" onchange="Mileage" id="Mileage"> </td></tr>

<tr valign="top"><td width="133">IRS Rates</td><td width="218"> 
<input name="IRSRates" value="01/01/2007-.485; 01/01/2008-.505; 01/01/2009-.55; 01/01/2010-.50; 01/01/2011-.51; 07/01/2011-.555; 01/01/2013-.565; 02/01/2014 -.56; 01/01/2015 -.575; 01/01/2016 -.54; 01/01/2017 -.535; 01/01/2018 -.545; 01/01/2019 -.58; 01/01/2020 -.575"> </td></tr>

<tr valign="top"><td width="133">Mileage Rate</td><td width="218"> 
<input name="MileageRate" value="01/01/2007-.485, 01/01/2008-.505, 01/01/2009-.55, 01/01/2010-.50, 01/01/2011-.51, 07/01/2011-.555, 01/01/2013-.565, 02/01/2014 -.56, 01/01/2015 -.575, 01/01/2016 -.54, 01/01/2017 -.535, 01/01/2018 -.545, 01/01/2019 -.58, 01/01/2020 -.575" id="MileageRate"> </td></tr>
</tbody></table>
</span>
<script> var hols =' 07/04/2016, 09/05/2016, 10/03/2016, 10/04/2016, 10/10/2016, 10/12/2016, 11/24/2016, 11/25/2016, 12/26/2016, 12/27/2016, 12/30/2016, 01/02/2017, 01/16/2017, 02/20/2017, 04/01/2017, 04/14/2017, 05/29/2017, 07/03/2017, 07/04/2017, 09/04/2017, 09/21/2017, 09/22/2017, 10/09/2017, 11/10/2017, 11/23/2017, 11/24/2017, 12/25/2017, 12/26/2017, 12/29/2017, 01/01/2018, 01/15/2018, 02/19/2018, 03/07/2018, 03/21/2018, 03/30/2018, 05/28/2018, 07/04/2018, 09/03/2018, 09/10/2018, 09/11/2018, 09/19/2018, 10/08/2018, 11/12/2018, 11/16/2018, 11/22/2018, 11/23/2018, 12/24/2018, 12/25/2018, 12/26/2018, 12/31/2018, 01/01/2019, 01/21/2019, 01/31/2019, 02/12/2019, 02/13/2019, 02/18/2019, 02/20/2019, 03/01/2019, 03/04/2019, 04/19/2019, 05/27/2019, 07/04/2019, 09/02/2019, 09/30/2019, 10/01/2019, 10/09/2019, 10/14/2019, 11/11/2019, 11/28/2019, 11/29/2019, 12/23/2019, 12/24/2019, 12/25/2019, 12/31/2019, 01/01/2020, 01/20/2020, 02/17/2020, 04/10/2020, 05/25/2020 ';
</script>
<table id="inputTable" class="inputTable" border="0" cellspacing="0" cellpadding="0">
<tbody><tr valign="top"><td width="732" colspan="6"><b>Please enter your travel reimbursement information:</b></td></tr>

<tr valign="top"><td width="144"><center>From: </center></td><td width="210" colspan="2"> 
<input name="From" value="" id="From" style="width:180px"> </td><td width="174"><center>To:</center></td><td width="204" colspan="2"> 
<input name="To" value="" id="To" style="width:180px"> </td></tr>

<tr valign="top"><td width="144"><center>Date:</center></td><td width="132"> 
<input name="travelDate" value="03/05/2020" id="travelDate" size="10" class="hasDatepicker"><img class="ui-datepicker-trigger" src="CalendarWebIcon.gif" alt="..." title="..."> </td><td width="78"><center>Miles:</center></td><td width="174"> 
<input name="numMiles" value="" onclick="holiday();
" id="numMiles" size="10"> </td><td width="96"><center>Tolls/Parking:</center></td><td width="108"> 
<input name="varCosts" value="" id="varCosts" style="width:93px"> </td></tr>

<tr valign="top"><td width="144"><center>Purpose of Trip:</center></td><td width="588" colspan="5"> 
<input name="travelPurpose" value="" id="travelPurpose" style="width:515px"> </td></tr>
</tbody></table>
<span id="tste_span-mileageTable"><div id="bttns-mileageTable"><input type="button" value="Ok" onclick="dlgOk(&quot;mileageTable&quot;);">&nbsp;<input type="button" value="Cancel" onclick="window.close();"></div></span>
<script type="text/javascript">
dlgInit();
</script>  
</form>
'''