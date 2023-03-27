# wireless_monitor
scraping information from on board radio (MST VIP &amp; ACKSYS) for command underground machine and combine with MST WAP information, for easier decision making and automate task to change setting both WAP and on board radio, using selenium, Python, PHP.
first of all thankyou for visiting my page.
this program triggered by web button and executing scanning_loader.py.
then calling function scan_loader.py for identifying only online loaders.
after get the list of online loaders continue to execute selenium scrapping web, there's 2 kind of product VIP and ACKSYS radio, and have diffrent element inside it, my code will identify the ID of button and try to catch what match it.
after able to decicde which radio is, my program will start to scrapping realtime data .
first i got trouble, realtime data can't be get while in current tab browser, need to open in new tab to get the value. 
data stored to array variable such as SSID, Loader, signal_strength, channel.
after stored continue to storing to DB i called fucntion insert_result().
visualize into webbased UI using simple php and html.
