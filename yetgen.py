import pandas as pd
#gerekli kütüphaneleri indirdim

csvFile='YetGen_Mock_Data.csv'
data= pd.read_csv(csvFile)
#csv dosyası ile verileri okudum

data['Toplam Not'] = data[['Not 1', 'Not 2', 'Not 3']].sum(axis=1)
#her bir kişinin toplam notunu hesapladım 
#data['Toplam Not'] ile yeni sütun oluşturdum 
#bu oluşturduğum sütuna data[['Not 1', 'Not 2', 'Not 3']] bu sütunları seçerek
#sum(axis=1) ile seçili sütunların her bir satırının toplanmasını sağladım

#print(data)
#datayı yazdırarak kontrol ettim

filtered = data[data['Toplam Not'] <= 100]
#yukarıda hesaplanan toplam notları 100den küçük ve eşit olma durumuna göre filtreledim

with pd.ExcelWriter('YetGen_Mock_Data.xlsx',engine='openpyxl',mode='a') as writer:
#with ile pandasın ExcelWriter metodunu kullanarak append modunda dosyayı açtım ve writer olarak adlandırdım 
    filtered.to_excel(writer,sheet_name='Son_Hali',index=False)
    #son_hali isimli aynı dosyada yeni bir sayfa oluşturarak filtrelediğimiz tabloyu ekledim
    #index sütununu index=False parametresi ile yazdırmadım
    


