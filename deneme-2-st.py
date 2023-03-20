import streamlit as st
import numpy as np
import pandas as pd

#from PIL import Image
#image = Image.open("C:/Users/petro/Desktop/proje4/pngegg.png")

st.set_page_config(
    page_title="DİYABET TAHMİNCİSİ",
    #page_icon=image,
    menu_items={
        "Get help": "mailto:mustafaatak3435@gmail.com",
        "About": "For More Information\n" + "https://github.com/farabiatak"
    }
)
st.title('Diyabet Sınıflandırma Projesi ')
st.markdown("Veri setide 253.680 değer bulunmakla beraber,Veri Amerika Birleşik Devletlerinde toplanmıştır. ")
st.image("https://www.drerolvural.com/wp-content/uploads/2020/07/diyabet-kalp.jpg")

st.header('Bilgilendirme')

st.markdown('Hipertansiyon : Kronik tansiyon teşhisi')
st.markdown('Yaş : 18-24 = 1 , 25-29 = 2 , 30-34 = 3 , 35-39 = 4 , 40-44 = 5 , 45-49 =6')
st.markdown('Yaş : 50-54 = 7 , 55-59 = 8 , 60-64 = 9 , 65-69 =10 , 70-74 =11 , 75-79 =12')

st.markdown('Eğitim : 1 - Okur-Yazar , 2 -İlkokul , 3 - Ortaokul , 4 - Lise , 5 - Yüksekokul , 6-Üniversite')

st.markdown('Gelir : 1 - 8600 ve altı , 2 - 8600 - 13000  , 3 - 13001 - 16000  4 - 16001 - 19000')
st.markdown('Gelir : 5 - 19001 - 22000 , 6 - 22001 - 25000 , 7 - 25001 - 28000 , 8 - 28000 ve üzeri')

st.markdown('Ruhsal : 30 gün içerisinde ruhsal olarak kaç kere kendinizi kötü hissettiniz?')
st.markdown('Fiziksel : 30 gün içerisinde fiziksel olarak kaç kere kendinizi kötü hissettiniz?')

df = pd.read_csv("C:/Users/petro/Desktop/DİYABET/diyabet_veri_tr_2.csv")

st.table(df.sample(5, random_state=13))

st.sidebar.markdown('Bilgilerinizi giriniz')

name = st.sidebar.text_input('İsim', help = 'Lütfen büyük harfle giriniz!')
surname = st.sidebar.text_input('Soyisim',help = 'Lütfen büyük harfle giriniz!')
boy= st.sidebar.number_input('Boy -- m',min_value=1.1)
kilo = st.sidebar.number_input('Kilo -- kg',min_value=20)
vke = (kilo/(boy*boy))
htans= st.sidebar.number_input('Hipertansiyon  --   (1 = VAR) / (0 = YOK)')
kolestrol_kronik = st.sidebar.number_input('Kronik Yüksek Kolestrol  --  (1 = VAR) / (0 = YOK)')
kolestrol_teshis = st.sidebar.number_input('Son 3 Yılda Yüksek Kolestrol Tespiti  --  (1 = VAR)  /(0 = YOK)' )
sigara = st.sidebar.number_input('Sigara Kullanımı  --  (1 = VAR) (0 = YOK)')
inme = st.sidebar.number_input('İnme-Felç-Kısmi Felç  --  (1 = VAR) (0 = YOK)')
chd = st.sidebar.number_input('Damar Tıkanıklığı  --  (1 = VAR) (0 = YOK)')
fizik_ak = st.sidebar.number_input('Fiziksel Aktivite  --  (1 = VAR) (0 = YOK)')
meyve = st.sidebar.number_input('Meyve Tüketimi  --  (1 = VAR) (0 = YOK)')
sebze = st.sidebar.number_input('Sebze Tüketimi  --  (1 = VAR) (0 = YOK)')
alkol = st.sidebar.number_input('Düzenli Alkol Tüketimi  --  (0 = VAR) (1 = YOK)')
saglik_sig =  st.sidebar.number_input('Sağlık Sigortası  --  (1 = VAR) (0 = YOK)')
tedavi_reddi = st.sidebar.number_input('Tedavi Reddi  --  (1 = VAR) (0 = YOK)')
genel_saglik = st.sidebar.number_input('Genel Sağlık  --  (1 - 5) (1 = Harika  / 5 = Kötü)')
merdiven = st.sidebar.number_input('Merdiven İnip Çıkarken Zorluk  --  (1 = VAR) (0 = YOK)')
cins = st .sidebar.number_input('Cinsiyet  -- (1 = Erkek)  (0 = Kadın)')
yas = st.sidebar.number_input('Yaş')
egitim = st.sidebar.number_input ('Eğitim Durumu (1 - 6) - Yukarıdan Eğitim Skorunuzu Görebilirsiniz')
gelir = st.sidebar.number_input ('Gelir Durumu (1 - 8) - Yukarıdan Gelir Skorunuzu Görebilirsiniz')
ruhsal = st.sidebar.number_input ('Ruhsal (30 Gün) (1 - 30) - Yukarıdan Ruhsal Skorunuzu Görebilirsiniz')
fiziksel =  st.sidebar.number_input ('Fiziksel Durum (30 Gün) (1 - 30) - Yukarıdan Fiziksel Skorunuzu Görebilirsiniz')

from joblib import load

logreg_model = load('C:/Users/petro/Desktop/DİYABET/logreg_model.pkl')

input_df = pd.DataFrame({   
    'hipertans': [htans],
    'kolestrol' : [kolestrol_kronik],
    'kolestrol_check': [kolestrol_teshis],
    'vke': [vke],
    'sigara': [sigara],
    'inme' : [inme],
    'chd' : [chd],
    'fiziksel_aktivite' : [fizik_ak],
    'meyve':[meyve],
    'sebze': [sebze],
    'agir_alkol': [alkol],
    'saglik_sigortasi' : [saglik_sig],
    'doktor_vaz': [tedavi_reddi],
    'genel_saglik' : [genel_saglik],
    'ruhsal' : [ruhsal],
    'fiziksel': [fiziksel],
    'yuruyus_merdiven' : [merdiven],
    'cinsiyet' : [cins],
    'yas' : [yas],
    'egitim': [egitim],
    'gelir' : [gelir]    
})



pred = logreg_model.predict(input_df.values)
pred_prob = np.ravel(logreg_model.predict_proba(input_df))
pred_prob_1 =pred_prob[0]
pred_prob_2 = int(pred_prob[1]*100)

st.markdown('SONUÇ')

if st.sidebar.button("Hesapla") :

    st.info("Bilgilerinizi girerek risk hesaplayabilirsiniz")
    
    from datetime import date,datetime
    
    today = date.today()
    time = datetime.now().strftime("%H:%M:%S")
    
    result_df = pd.DataFrame({
    'İSİM' : [name],
    'SOYİSİM' : [surname],
    'TARİH' : [today],
    'SAAT' : [time],
    'TAHMİN' : [pred],
    #'Olasılık'  : [pred_prob_1],
    'Diyabet Riski %'  : [pred_prob_2]   
    })
    
    result_df["TAHMİN"] = result_df["TAHMİN"].apply(lambda x: str(x).replace("0","sağlıklı"))
    result_df["TAHMİN"] = result_df["TAHMİN"].apply(lambda x: str(x).replace("1","hastalıklı"))
    
    st.table(result_df)
    
    if pred == 1:
        st.image('https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-81b7de06-af33-437a-8370-456e0590011f.jpg')
    else:
        st.image('http://www.verita.com.tr/wp-content/uploads/2014/08/girl2.jpg')
else : 
    st.markdown('Hesapla Butonuyla Sonucu Görebilirsiniz')





