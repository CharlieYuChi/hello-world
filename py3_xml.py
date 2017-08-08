import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    """
    data = '''
    <comments>
<comment>
<name>Salter</name>
<count>95</count>
</comment>
<comment>
<name>Natalie</name>
<count>89</count>
</comment>
<comment>
<name>Radmiras</name>
<count>87</count>
</comment>
<comment>
<name>Alveena</name>
<count>84</count>
</comment>
<comment>
<name>Haleema</name>
<count>80</count>
</comment>
<comment>
<name>Samara</name>
<count>73</count>
</comment>
<comment>
<name>Moore</name>
<count>72</count>
</comment>
<comment>
<name>Sohera</name>
<count>72</count>
</comment>
<comment>
<name>Pietro</name>
<count>71</count>
</comment>
<comment>
<name>Courtneylee</name>
<count>70</count>
</comment>
<comment>
<name>Charlize</name>
<count>70</count>
</comment>
<comment>
<name>Kerris</name>
<count>70</count>
</comment>
<comment>
<name>Kashif</name>
<count>69</count>
</comment>
<comment>
<name>Rhiana</name>
<count>69</count>
</comment>
<comment>
<name>Jedd</name>
<count>65</count>
</comment>
<comment>
<name>Annalee</name>
<count>65</count>
</comment>
<comment>
<name>Alistar</name>
<count>61</count>
</comment>
<comment>
<name>Zakaria</name>
<count>57</count>
</comment>
<comment>
<name>Naideen</name>
<count>55</count>
</comment>
<comment>
<name>Leigham</name>
<count>54</count>
</comment>
<comment>
<name>Chi</name>
<count>54</count>
</comment>
<comment>
<name>Aiesha</name>
<count>49</count>
</comment>
<comment>
<name>Ruairi</name>
<count>48</count>
</comment>
<comment>
<name>Zamaar</name>
<count>45</count>
</comment>
<comment>
<name>Kalise</name>
<count>44</count>
</comment>
<comment>
<name>Amos</name>
<count>42</count>
</comment>
<comment>
<name>Holli</name>
<count>41</count>
</comment>
<comment>
<name>Tee</name>
<count>40</count>
</comment>
<comment>
<name>Maddie</name>
<count>37</count>
</comment>
<comment>
<name>Saffa</name>
<count>36</count>
</comment>
<comment>
<name>Gytis</name>
<count>34</count>
</comment>
<comment>
<name>Sammi</name>
<count>33</count>
</comment>
<comment>
<name>Kirk</name>
<count>30</count>
</comment>
<comment>
<name>Kitty</name>
<count>30</count>
</comment>
<comment>
<name>Shannyn</name>
<count>28</count>
</comment>
<comment>
<name>Cadie</name>
<count>23</count>
</comment>
<comment>
<name>Raigen</name>
<count>20</count>
</comment>
<comment>
<name>Krystyna</name>
<count>18</count>
</comment>
<comment>
<name>Mehr</name>
<count>17</count>
</comment>
<comment>
<name>Daymian</name>
<count>16</count>
</comment>
<comment>
<name>Summer</name>
<count>14</count>
</comment>
<comment>
<name>Sabila</name>
<count>14</count>
</comment>
<comment>
<name>Greta</name>
<count>13</count>
</comment>
<comment>
<name>Colt</name>
<count>8</count>
</comment>
<comment>
<name>Danys</name>
<count>7</count>
</comment>
<comment>
<name>Katey</name>
<count>7</count>
</comment>
<comment>
<name>Briana</name>
<count>5</count>
</comment>
<comment>
<name>Zhen</name>
<count>4</count>
</comment>
<comment>
<name>Edwin</name>
<count>4</count>
</comment>
<comment>
<name>Billy</name>
<count>1</count>
</comment>
</comments>'''
"""

    tree = ET.fromstring(data)
    l = tree.findall('comment/count')
    sum = 0
    count = 0
    for i in l:
        sum += int(i.text)
        count += 1
    
    print('sum:', sum)
    print('count:', count)
    